# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from oauth2client import client
from oauth2client import tools 
from oauth2client.file import Storage 
import json
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main(id):
   
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"


    # Get credentials and create an API client
    credential_path = os.path.join('./', 'credential_sample.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:#to store the creds and don't have to login again
        flow = client.flow_from_clientsecrets(client_secrets_file,scopes)
        credentials = tools.run_flow(flow, store)
        
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials) #You can find this in the doc
    request = youtube.videos().list(
        part="snippet", #I only get the snipet
 
        id=id #id of YT video, I will give it via an external variable from bot.py
    )
    response = request.execute()
    items = response['items'][0] #take item from the dict and become a list if I don't select the first element
    title = items["snippet"]["title"] #I take the title from the snippet item
    print(title)
    return title

if __name__ == "__main__":
    ytidd="dQw4w9WgXcQ"
    main(ytidd)
