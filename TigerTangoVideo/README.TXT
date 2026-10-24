TIGERTANGO VIDEO C - SONG AND EVENT TEXT SHARE A LEFT MARGIN
Updated: 2026-10-24

This ZIP contains revision C of the video overlay for VirtualDJ. Song details
appear at the top. The event name is larger and bold at the bottom. Song
details and event text are left-aligned at the same fixed margin.
Use your existing TigerTango main interface to control the video options.

Download the release asset TigerTangoVideo-C.zip, not GitHub's automatic
"Source code (zip)" archive. Select the entry
with C in its name so an older installed overlay is not used accidentally.

INSTALL / UPDATE

1. Find the VirtualDJ home folder:
   Open VirtualDJ > Settings > Options and click the folder/cog icon in
   the lower-right corner. Open the VideoSkins folder inside it.

   Another way: Settings > Interface > Video Overlay > select an overlay
   > Edit this Skin. In the folder that opens, go up to VideoSkins.

   Common locations (your installation may use a different home folder):
   Windows: C:\Users\YOUR-NAME\AppData\Local\VirtualDJ\VideoSkins
   Windows, older installations:
            C:\Users\YOUR-NAME\Documents\VirtualDJ\VideoSkins
   macOS:   ~/Library/Application Support/VirtualDJ/VideoSkins
   macOS, older installations: ~/Documents/VirtualDJ/VideoSkins

2. Close VirtualDJ. Move your old TigerTangoVideo folder or ZIP somewhere
   outside VideoSkins as a backup. Keep any customized Logo.png.

3. Create a folder named TigerTangoVideo-C INSIDE VideoSkins.
   Unpack ALL files from this ZIP directly into that folder.
   The finished layout must be:

   VideoSkins/
     TigerTangoVideo-C/
       TigerTangoVideo.xml
       TigerTangoVideo.png
       Logo.png
       preview.png
       README.TXT

   Avoid an extra nested folder. The XML and image files
   must be together. This overlay goes in VideoSkins, not the Skins folder
   used for VirtualDJ's main interface.

   Alternative: copy TigerTangoVideo-C.zip directly into VideoSkins without
   unpacking it. Choose ONE installation method so there is only one copy.

4. If you have a customized Logo.png, restore it into the unpacked folder.

5. Restart VirtualDJ. Open Settings > Interface > Video Overlay and select
   the TigerTangoVideo entry with C in its name. An unpacked version may
   also have (edit) in its name. Do not select the old TigerTangoVideo entry.
   Click the video preview in the TigerTango main interface to turn video on.

SET THE EVENT NAME

1. Load a song. In TigerTango, right-click the music/pen (lyrics) button
   beneath the video preview, enter the event name, and click OK.
   This uses the song's Comments field. You can also edit Comments in the
   song information panel. Use the same comment on each song if the event
   name should stay the same when tracks change.

2. Turn on SHOW LYRICS with the music/pen button or the video options gear.
   The text appears after the existing initial 10-second album-art interval.
   Songs with an empty Comments field show artwork instead of event text.

3. Under the video options gear, set LYRICS SIZE to MEDIUM for the new
   default-size appearance (64px on a 1920x1080 screen). SMALL, LARGE, and
   LARGER use 48px, 80px, and 96px. Choose SMALL for a long event name.
   All sizes are bold and left-aligned at the bottom. This edition keeps
   the event text at the song text's left margin regardless of LYRICS POS.

The text area supports multiple lines. Larger fonts fit fewer lines; check
the full event name in the video preview. TITLE SIZE changes the song
header and can remain NORMAL or LARGE.

If you enter the event name with VirtualDJ's separate Text video effect,
use that effect's own editor to enlarge and position its text at the bottom.
This skin's event-name formatting applies to the Comments display.

TROUBLESHOOTING

Make sure you downloaded TigerTangoVideo-C.zip. TigerTango.zip contains
the main DJ interface; installing it does not update this video layout.

Old layout still showing: remove duplicate ZIP/folder copies from VideoSkins,
restart VirtualDJ, and select the updated overlay again.
Use the VirtualDJ home folder opened by Settings > Options; an older
Documents/VirtualDJ folder might not be the active location. A ZIP and an
extracted folder are separate selectable copies, so replacing one does not
update the other. In Settings > Interface > Video Overlay, select No Overlay
and then explicitly select the updated overlay. Check the actual video
output, rather than relying on the thumbnail in the picker.
Revision C also has an updated thumbnail and a description starting with
"Revision C" in the overlay picker. If those are missing, the old copy is
still selected or the ZIP was copied into the wrong home folder.

No cache deletion was needed in our test. Keep your database and other
VirtualDJ settings intact. If the event name comes from the separate Text
video effect, adjust that effect's own settings instead of LYRICS SIZE.

No event name: check the current song's Comments, enable SHOW LYRICS, and
wait for the initial album-art interval to finish.

Original project: https://github.com/sericson0/TigerTango
VirtualDJ home folder help:
https://virtualdj.com/wiki/How%2Bto%2BTransfer%2BTo%2BA%2BNew%2BComputer.html
