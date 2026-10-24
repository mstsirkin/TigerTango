#!/usr/bin/env python3
"""Check the event footer's geometry and its main-interface controls."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def parse(source):
    # VirtualDJ accepts upstream's bare script ampersands. Normalize in memory.
    return ET.fromstring(re.sub(r"&(?!#\d+;|#x[0-9a-fA-F]+;|\w+;)", "&amp;", source))


def number(value):
    assert re.fullmatch(r"[+\-\d]+", value), value
    return sum(map(int, re.findall(r"[+-]?\d+", value)))


def boxes(element, x=0, y=0, groups=()):
    groups += (element.get("name", element.tag),)
    attrs = dict(element.attrib)
    for tag in ("pos", "size"):
        child = element.find(tag)
        if child is not None:
            attrs.update(child.attrib)
    for key in ("x", "y"):
        if key in attrs:
            value = attrs[key]
            parent = x if key == "x" else y
            offset = parent if value.startswith(("+", "-")) else 0
            if key == "x":
                x = offset + number(value)
            else:
                y = offset + number(value)
    if element.tag in ("text", "textzone", "cover", "visual", "logo", "blockwave"):
        if "width" in attrs and "height" in attrs:
            yield groups, element, (x, y, x + number(attrs["width"]), y + number(attrs["height"]))
        return
    for child in element:
        if child.tag not in ("pos", "size", "define"):
            yield from boxes(child, x, y, groups)


video = parse((ROOT / "TigerTangoVideo/TigerTangoVideo.xml").read_text(encoding="utf-8-sig"))
main_source = (ROOT / "TigerTango/TigerTango.xml").read_text(encoding="utf-8-sig")
rects = list(boxes(video))
for path, element, rect in rects:
    x1, y1, x2, y2 = rect
    assert 0 <= x1 < x2 <= 1920 and 0 <= y1 < y2 <= 1080, (path, rect)

headers = [r for path, _, r in rects if "track_text" in path]
events = [(e, r) for path, e, r in rects if "event_footer" in path]
assert len(headers) == 6 and len(events) == 8
assert all(r[0] == 75 and r[3] <= 450 for r in headers)
for element, rect in events:
    assert rect[0] == 75 and 810 <= rect[1] < rect[3] <= 1050
    assert rect[3] - rect[1] >= int(element.get("fontsize")) * 1.25, "Allow font line height at LARGER size"
    assert rect[2] < 1570, "Event must stay clear of the right-hand logos"
    assert element.get("align") == "left" and element.get("multiline") == "yes"
    assert element.get("action") in ("get_var '@$ttEventName'", "get_var '@$ttEventDate'")
assert sorted(int(e.get("fontsize")) for e, _ in events) == [48, 48, 64, 64, 80, 80, 96, 96]

comments = video.findall(".//group[@name='lyrics_panel']")
assert len(comments) == 2
assert "'@$ttShowEvent' 1 ? false" in comments[0].get("visibility")
assert "'@$ttShowEvent' 1 ?" in comments[1].get("visibility")
assert all(e.get("height") == "320" for e in comments[1].findall("text"))
event_covers = [r for _, e, r in rects if e.tag == "cover"
                and e.get("visibility", "").startswith("var_equal '@$ttShowEvent' 1 ?")
                and not e.get("visibility").startswith("var_equal '@$ttShowEvent' 1 ? false")]
assert len(event_covers) == 2
assert all(r[3] <= 800 for r in event_covers), "Artwork must stay above the event footer"

# Parse the new section separately: upstream has duplicate XML attributes
# elsewhere that VirtualDJ tolerates but strict XML parsers reject.
controls = parse(re.search(r'<group name="event_settings".*?</group>', main_source, re.S).group())
buttons = controls.findall("button")
by_label = {button.get("text"): button for button in buttons}
assert "set_var_dialog '@$ttEventName'" in by_label["EDIT NAME"].get("action")
assert "set_var_dialog '@$ttEventDate'" in by_label["EDIT DATE"].get("action")
assert "deck master effect_active 'text' off" in by_label["SHOW EVENT"].get("action")
assert "set '@$ttShowEvent' 0" in by_label["CLEAR EVENT"].get("action")
assert re.search(r'<onload action="[^\"]*ttEventInitialized', main_source)
assert all(number(b.get("y")) + number(b.get("height")) <= 190 for b in buttons)
assert all(number(b.get("x")) + number(b.get("width")) <= 380 for b in buttons)
assert "LOAD TEST TRACK" not in (ROOT / "TigerTango/TigerTango.xml").read_text()
print("PASS: canvas bounds, shared left margin, event sizes, reserved footer, persistent entry controls, and Text-effect handoff")
