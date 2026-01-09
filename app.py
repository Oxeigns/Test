import os

def get_credentials():
    api_id = input("Enter your API ID: ")
    api_hash = input("Enter your API HASH: ")
    session_string = input("Enter your Pyrogram Session String (optional, press enter to login via phone): ")
    return api_id, api_hash, session_string

WORDS_TO_SEND = ["Hello", "Kaise ho?", "Automated Message" ]
DELAY = 2 
