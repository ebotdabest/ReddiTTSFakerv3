from config import TRANSCRIPT_PATH, SCREENSHOT_PATH, EXPORT_FOLDER
import os
from moviepy import editor

def make_post_video(id):
    with open(os.path.join(TRANSCRIPT_PATH, id, "ts.txt")) as f:
        transcript = f.read()


    base_vid = editor.VideoFileClip("subway.mp4")

    txt_clip = (editor.TextClip("Super idol", fontsize=70, color='white')
                .set_position('center')
                .set_duration(10))

    end_video = editor.CompositeVideoClip([base_vid, txt_clip])
    end_video.write_videofile(os.path.join(EXPORT_FOLDER, id, "video.mp4"))

make_post_video("16p8nrx")