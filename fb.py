import facebook
from creds import *

class Facebook:
    def __init__(self, link):
        self.graph = facebook.GraphAPI(FACEBOOK_LONG_LIVED_ACCESSTOKEN)
        self.link = link

    def upload_video(self):
        try:
            self.graph.put_object("me", "feed", message="This is the video I just posted on youtube! Check it out!", link=self.link)
            print("Uploaded!")
        except Exception as e:
            print(e)
