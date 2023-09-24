from config import TRANSCRIPT_PATH, SCREENSHOT_PATH, VOICE_PATH
import os
from moviepy import editor

def make_post_video(id, durations):
    title_duration = durations[-1]
    durations.remove(durations[-1])

    with open(os.path.join(TRANSCRIPT_PATH, id, "ts.txt")) as f:
        transcript = f.read()

    with open(os.path.join(TRANSCRIPT_PATH, id, "title.txt")) as f:
        title = f.read()

    # base_vid = editor.VideoFileClip("subway.mp4")

    clips = []
    i = 0
    for img, audio in zip(os.listdir(os.path.join(SCREENSHOT_PATH, id)), os.listdir(os.path.join(VOICE_PATH, id))):
        if img != "title.png" and audio != "title.mp3":
            img = editor.ImageClip(os.path.join(SCREENSHOT_PATH, id, img), duration=durations[i])
            img = img.set_audio(audio)
            clips.append(img)
            i+= 1


    text_vid_clip = editor.concatenate_videoclips(clips, method="compose")
    text_vid_clip.write_videofile("test.mp4", fps=24)



    # end_video = editor.CompositeVideoClip([base_vid, txt_clip])
    # end_video.write_videofile(os.path.join(EXPORT_FOLDER, id, "video.mp4"))

# make_post_video("16qnjgf")