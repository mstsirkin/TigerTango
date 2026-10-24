TIGERTANGO VIDEO - SONG DETAILS AT THE TOP
Package revision: 2026-10-24.1

This ZIP keeps revision C's layout and restores the original overlay name.
Song details appear at the top. The skin's Comments/lyrics display is larger
and bold at the bottom, sharing the song details' fixed left margin.
An event name entered in VirtualDJ's separate Text effect uses that effect's
own size and position controls; see SET THE EVENT NAME below.
Use your existing TigerTango main interface to control the video options.

Download the release asset TigerTangoVideo.zip, not GitHub's automatic
"Source code (zip)" archive. The ZIP, folder, and overlay keep the same
TigerTangoVideo name for future updates. The revision is recorded here.

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
   outside VideoSkins as a backup. Also move any TigerTangoVideo-C folder
   or ZIP outside VideoSkins if you installed that edition.
   Keep any customized Logo.png.

3. Create a folder named TigerTangoVideo INSIDE VideoSkins.
   Unpack ALL files from this ZIP directly into that folder.
   The finished layout must be:

   VideoSkins/
     TigerTangoVideo/
       TigerTangoVideo.xml
       TigerTangoVideo.png
       Logo.png
       preview.png
       README.TXT

   Avoid an extra nested folder. The XML and image files
   must be together. This overlay goes in VideoSkins, not the Skins folder
   used for VirtualDJ's main interface.

   Alternative: copy TigerTangoVideo.zip directly into VideoSkins without
   unpacking it. Choose ONE installation method so there is only one copy.

4. If you have a customized Logo.png, restore it into the unpacked folder.

5. Restart VirtualDJ. Open Settings > Interface > Video Overlay and select
   TigerTangoVideo. An unpacked version may also have (edit) in its name.
   Click the video preview in the TigerTango main interface to turn video on.

SET THE EVENT NAME

Using the separate Text video effect (as in the reported screenshots):

1. Open the TEXT effect editor from TigerTango's video options.
   Enter the event name and date, removing empty lines added for spacing.

2. In the small preview on the right of the TEXT editor, drag the outlined
   text box down to the bottom. Use this box to position the text instead
   of adding empty lines in the editor.

3. Drag the box's edges to resize it and adjust the font size. Allow enough
   height for both the event name and date. The reported shrinking with
   extra empty lines is consistent with text being fitted into a fixed box.

4. Move the box horizontally while watching the full video output until
   the event name's first letter lines up below the song title's first
   letter. This alignment is manual: the skin does not position Text effects.
   Leave Visible checked and Scroll unchecked for a static event name.

LYRICS SIZE and LYRICS POS do not control the Text effect. SHOW LYRICS can
stay off when the event name is supplied by Text. The screenshots already
show song details at the top, so the skin update has taken effect; the Text
effect needs its own adjustment. These observations do not indicate a
Windows 11-specific problem or a need to delete caches.

Optional alternative: using the song's Comments field:

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

TROUBLESHOOTING

Make sure you downloaded TigerTangoVideo.zip. TigerTango.zip contains
the main DJ interface; installing it does not update this video layout.

Old layout still showing: remove duplicate ZIP/folder copies from VideoSkins,
restart VirtualDJ, and select the updated overlay again.
Use the VirtualDJ home folder opened by Settings > Options; an older
Documents/VirtualDJ folder might not be the active location. A ZIP and an
extracted folder are separate selectable copies, so replacing one does not
update the other. In Settings > Interface > Video Overlay, select No Overlay
and then explicitly select the updated overlay. Check the actual video
output, rather than relying on the thumbnail in the picker.
The updated thumbnail shows the shared-left-margin layout. Check the
package revision at the top of the installed README.TXT when identifying
your copy; the overlay name stays TigerTangoVideo.

No cache deletion was needed in our test. Keep your database and other
VirtualDJ settings intact. If the event name comes from the separate Text
video effect, adjust that effect's own settings instead of LYRICS SIZE.

No event name: for Text, check that the effect is active, Visible is checked,
and its box is on-screen. For Comments, check the current song's Comments,
enable SHOW LYRICS, and wait for the initial album-art interval to finish.

Original project: https://github.com/sericson0/TigerTango
VirtualDJ home folder help:
https://virtualdj.com/wiki/How%2Bto%2BTransfer%2BTo%2BA%2BNew%2BComputer.html
Text effect and sizing help:
https://virtualdj.com/plugins/?addonid=80895
https://virtualdj.com/forums/216802/VirtualDJ_Plugins/Text_on_screen.html
