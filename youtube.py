from youtube_functions import *


class Youtube:
    def __init__(self, title, description, file_name, category_id, access):
        self.title = title
        self.description = description
        self.privacyStatus = access
        self.categoryId = category_id
        self.args = {
            "file": file_name,
            "title": self.title,
            "description": self.description,
            "privacyStatus": self.privacyStatus,
            "categoryID": self.categoryId
        }
    def upload_video(self):
        try:
            youtube = get_authenticated_service()
            print("Initializing Upload....")
            video_id = initialize_upload(youtube, self.args)
            link = "https://www.youtube.com/watch?v=" + video_id
            return link
        except HttpError as e:
            print(f'An HTTP error {e.resp.status} occurred:\n{e.content}')
        except Exception as ex:
            print(ex)
