import moviepy.editor as moviepy
def convert(file):
    clip = moviepy.VideoFileClip(file)
    clip.write_videofile(file + ".mp4")
