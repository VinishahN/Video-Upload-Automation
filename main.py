from twitter import *
from youtube import *
from instagram import *
from fb import *
import os
from convertToMp4 import *
from sample import *
import time

title = input("Enter the title: ")
description = input("Enter the description: ")
caption_for_twitter = input("Enter the caption for twitter: ")
category_id = int(input("Enter the category ID: "))
access = input("Enter the access type: (private/public) ")
# file_name = "public/sample.mp4"
link = ""
print("List of the files to upload: ")
fl = Files()
files = fl.get_files()

for file in files:
    print(str(file) + ". " + files[file] + "\n")

file = int(input("Which file do you want to upload: "))
file_name = files[file]
print(file_name)

if(file_name.split(".")[1]!="mp4"):
    file_name = "public/" + file_name
    if(os.path.exists(file_name + ".mp4")):
        os.remove(file_name)
        file_name = file_name + ".mp4"
    else:
        convert(file_name)
        os.remove(file_name)
        file_name = file_name + ".mp4"
else:
    file_name = "public/" + file_name
# Twitter
print("---------------Twitter-------------------------")
try:
    tw = Twitter()
    print("Uploading.....")
    tw.upload_video(file_name, caption_for_twitter)
    print("--------------------------------------------------")
except Exception as ex:
    print(ex)
    print("--------------------------------------------------")

#Youtube
print("---------------Youtube-------------------------")
try:
    y = Youtube(title, description, file_name, category_id, access)
    link = y.upload_video()
    print("--------------------------------------------------")
except Exception as e:
    print(e)
    print("--------------------------------------------------")

#Instagram
print("---------------Instagram-------------------------")
try:
    print("Uploading....")
    insta = Instagram(file_name)
    insta.upload_video()
    print("--------------------------------------------------")
except Exception as e:
    print(e)
    print("--------------------------------------------------")

#Facebook
print("---------------Facebook-------------------------")
try:
    print("Uploading...")
    f = Facebook(link)
    f.upload_video()
    print("--------------------------------------------------")
except Exception as e:
    print(e)
    print("--------------------------------------------------")

os.remove(file_name + ".jpg")

