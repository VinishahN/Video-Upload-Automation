import requests
# Authorization:
client_id = {APP_ID}
redirect_uri = {REDIRECT_URI}
state = {ANY_STRING}
url = f"https://www.pinterest.com/oauth/?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=boards:read,pins:read,boards:write,pins:write&state={state}"
response = requests.get(url)

# After going to the above-mentioned url, you will be requested to give access if already logged in!
# After giving access, you will be redirected to the url as mentioned below
# You would get a url like this which has the code and state appended to the redirect uri registered for the app
# Example URL: https://fenixninja.com/?code=1998f857765cda12354298d56373d30c336bf312&state=rct
# Save this code for getting access token
# CODE_GOT_FROM_REDIRECT_URI = "1998f857765cda12354298d56373d30c336bf312"

# Getting an Access Token and refresh token using code received in the url after authorization
import json
endpoint = "https://api.pinterest.com/v5/oauth/token"

request_body = {
                "code": {CODE_GOT_FROM_REDIRECT_URI},
                "redirect_uri": {REDIRECT_URI},
                "grant_type": "authorization_code",
        }

headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic MTQ3OTQwNjplYTI4YzA3YTE3NmZkNDYyZTdmNGI2OTNjZWQ1OGFiNjU5MjU1ZDdi'}
#In headers, Authorization's value would be "Basic" + " " + the base64 encoded string made of client_id:client_secret
access_response = requests.post(endpoint, data=request_body, headers=headers)
print(type(access_response.text))
details = json.loads(access_response.text)
print(type(details))
print(details)
access_token = details["access_token"]
refresh_token = details["refresh_token"]
token_type = details["token_type"]
credentials = {
    "access_token" : access_token,
    "refresh_token": refresh_token,
    "token_type": token_type
}
print(credentials) # Having a dictionary of credentials

# Create a pin
pin_endpoint = "https://api.pinterest.com/v5/pins"
pin_headers = {'Content-Type': 'application/json'}
# Placing all the necessary details to create a pin in a dictionary format to pass to the specififed endpoint
pin_request_body = {
  "link": "https://www.pinterest.com/",
  "title": "string",
  "description": "string",
  "dominant_color": "#6E7874",
  "alt_text": "string",
  "board_id": "string",
  "board_section_id": "string",
  "media_source": {
    "source_type": "image_base64",
    "content_type": "image/jpeg",
    "data": "string"
  },
  "parent_pin_id": "string"
}
pin_response = requests.post(pin_endpoint, data = pin_request_body, headers=pin_headers)
print(pin_response)
