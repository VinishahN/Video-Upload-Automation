import tweepy

from creds import *
6
class Twitter:
    def __init__(self):
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

    def upload_video(self, file_name, caption_for_twitter):
        try:
            media = self.api.media_upload(file_name, media_category="tweet_video")
            if (caption_for_twitter != 'no'):
                self.api.update_status(status=caption_for_twitter, media_ids=[media.media_id_string])
            else:
                self.api.update_status(status="", media_ids=[media.media_id_string])
            print("Uploaded!")

        except Exception as ex:
            print(ex)

