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

# 各種設定
WAIT_TIME = 1
ANIMAL_NAME = sys.argv[1]
DOWNLOAD_TO = "./dataware/collected/animalai/{}".format(ANIMAL_NAME)

# flickr処理
flickr = FlickrAPI(FLICKR_KEY, FLICKR_SECRET, format="parsed-json")
result = flickr.photos.search(
    text = ANIMAL_NAME,
    per_page = 400,
    media = "photos",
    sort = "relevance",
    safe_search = 1,
    extras = "url_q, license",
)

photos = result["photos"]

# JSON形式で表示
if DEBUG:
    pprint(photos)



