from instagrapi import Client
from creds import *

class Instagram:
    def __init__(self, file_name):
        self.cl = Client()
        self.cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        self.file_name = file_name


    def upload_video(self):
        try:
            media = self.cl.igtv_upload(
                self.file_name,
                "Sample Video", "Check out the new video I just posted on youtube!!",
                extra_data={
                    "custom_accessibility_caption": "alt text example",
                    "like_and_view_counts_disabled": 1,
                    "disable_comments": 1,
                }
            )
            print("Uploaded!")
        except Exception as e:
            print(e)
# i = Instagram("public/cartoon.mp4")
# i.upload_video()