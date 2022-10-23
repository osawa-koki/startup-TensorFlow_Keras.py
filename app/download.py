from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
from dotenv import load_dotenv

DEBUG = True

# .envファイルのロード
load_dotenv()

# flickrのAPIキーとシークレットを取得
FLICKR_KEY = os.getenv("FLICKR_KEY")
FLICKR_SECRET = os.getenv("FLICKR_SECRET")

if DEBUG:
  print("FLICKR_KEY -> {}".format(FLICKR_KEY))
  print("FLICKR_SECRET -> {}".format(FLICKR_SECRET))
  
