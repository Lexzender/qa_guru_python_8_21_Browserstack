import os

from dotenv import load_dotenv

load_dotenv()

username = os.getenv('USER_NAME')
access_key = os.getenv('ACCESS_KEY')
