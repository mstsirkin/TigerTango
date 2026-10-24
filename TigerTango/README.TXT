TIGERTANGO - GLOBAL EVENT NAME AND DATE
Package revision: 2026-10-24.2

Song details appear at the top. Enter your event name and date once in
TigerTango's video options; they appear at the bottom, sharing the song
information's LEFT MARGIN. EVENT SIZE sets their font size. No dragging,
blank lines, or per-song Comments are needed.

IMPORTANT: UPDATE BOTH SKINS

Download BOTH release assets: TigerTango.zip and TigerTangoVideo.zip.
TigerTango.zip supplies the new entry buttons. TigerTangoVideo.zip draws
the event name/date. Updating only one ZIP will not provide the feature.
Use the release assets, not GitHub's automatic "Source code" archives.
Both ZIPs include this README.TXT and retain their original skin names.

INSTALL / UPDATE

1. Find the active VirtualDJ home folder:
   Open VirtualDJ > Settings > Options and click the folder/cog icon in
   the lower-right corner. Use the Skins and VideoSkins folders inside it.

   Common home locations (your installation may use a different folder):
   Windows: C:\Users\YOUR-NAME\AppData\Local\VirtualDJ
   Windows, older installations: C:\Users\YOUR-NAME\Documents\VirtualDJ
   macOS: ~/Library/Application Support/VirtualDJ
   macOS, older installations: ~/Documents/VirtualDJ

2. Close VirtualDJ. Move previous TigerTango and TigerTangoVideo ZIP/folder
   copies outside their Skins/VideoSkins folders as backups. Also move any
   TigerTangoVideo-C copy out. Keep your customized Logo.png, if any.

3. Unpack TigerTango.zip directly into Skins/TigerTango.
   Unpack TigerTangoVideo.zip directly into VideoSkins/TigerTangoVideo.
   The result must look like this, without an extra nested folder:

   VirtualDJ home/
     Skins/
       TigerTango/
         TigerTango.xml
         graphics.png
         icons.png
         icons_daylight.png
         preview.png
         README.TXT
     VideoSkins/
       TigerTangoVideo/
         TigerTangoVideo.xml
         TigerTangoVideo.png
         Logo.png
         preview.png
         README.TXT

   Alternative: put TigerTango.zip directly in Skins and TigerTangoVideo.zip
   directly in VideoSkins without unpacking. Choose ONE installation method
   for each skin, so there are no duplicate ZIP and unpacked copies.

4. Restore your custom Logo.png into the unpacked TigerTangoVideo folder.

5. Restart VirtualDJ. Under Settings > Interface, select:
   Main interface: TigerTango
   Video Overlay:  TigerTangoVideo
   Unpacked copies may have (edit) appended to their names.

WHERE TO ENTER THE EVENT NAME AND DATE

1. In the TigerTango main screen, find the VIDEO preview near the top.
   Click the GEAR button immediately beneath it. This opens
   VIDEO CONFIGURATION OPTIONS.

2. At the bottom of that window, find EVENT NAME / DATE.
   Click EDIT NAME. Type the milonga/event name, for example Milonga Zorro,
   and click OK in the entry dialog.

3. Click EDIT DATE. Type the date exactly as you want it displayed, for
   example 24/10/2026, and click OK. Leave it empty if no date is needed.
   This is the event's date, not an automatically updating clock.

4. Click SHOW EVENT so it lights up. Click the VIDEO preview to turn on
   video output if needed. The event appears immediately at the bottom,
   independent of the song and the initial album-art interval.

5. Click the button under EVENT SIZE to choose SMALL, MEDIUM, LARGE, or
   LARGER. The sizes are 48, 64, 80, and 96 pixels on the skin's 1920x1080
   canvas and scale with the video output. Right-click cycles backwards.
   This control changes both the name and date. LYRICS SIZE still controls
   song Comments only; TITLE SIZE controls the song information.

The name, date, size, and SHOW EVENT choice are shared by all songs and
saved across normal VirtualDJ restarts. Edit them when the event changes.
SHOW EVENT hides/shows the footer without clearing your entries.
CLEAR EVENT clears both entries and hides the footer.

Use one line per entry. Do not add blank lines to position the text.
Long names wrap within the reserved area; use SMALL or shorten the name if
it does not fit. The font size is selected explicitly instead of shrinking
the entire event to fit additional blank lines.

SWITCHING FROM THE OLD TEXT EFFECT

Turning SHOW EVENT on switches OFF the separate master Text effect to
prevent duplicate event names. Its saved text/presets are not deleted.
Enter your name/date with EDIT NAME / EDIT DATE; old Text effect contents
are not imported automatically. Leave the separate Text effect off while
using the new footer. Hiding the footer does not re-enable the old effect.

SHOW LYRICS is optional and still displays each song's Comments. With the
event visible, artwork and Comments use a shorter area above the footer.
When the event is hidden, they return to the previous full-height area.

TROUBLESHOOTING

No EVENT NAME / DATE buttons: update TigerTango.zip in Skins, restart, and
select the updated MAIN interface. Updating the video ZIP alone is not enough.

Buttons exist but no event on video: update TigerTangoVideo.zip in VideoSkins,
select it as the Video Overlay, enter a name, enable SHOW EVENT, and turn
video output on. Check the live video output rather than just the thumbnail.

Old layout still selected: use the ACTIVE home folder opened by Options.
Move duplicate ZIP/folder copies out of Skins/VideoSkins, restart VirtualDJ,
and reselect the updated skins. For the video, select No Overlay and then
TigerTangoVideo if necessary. No cache/database deletion is required by
this update. Check the revision at the top of this installed README.TXT.

Duplicate event text: turn the separate master Text effect off, or toggle
SHOW EVENT off and on to switch it off automatically. If the event name is
also in song Comments, turn SHOW LYRICS off or edit those Comments.

TESTING.TXT is a separate release asset with the VirtualDJ download,
isolated Wine setup, completed checks, and testing limitations.

Original project: https://github.com/sericson0/TigerTango
This fork and releases: https://github.com/mstsirkin/TigerTango/releases
VirtualDJ home folder help:
https://virtualdj.com/wiki/How%2Bto%2BTransfer%2BTo%2BA%2BNew%2BComputer.html
