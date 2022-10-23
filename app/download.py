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

for i, photo in enumerate(photos["photo"]):
    # 保存対象のURLを取得
    url_q = photo["url_q"]
    # 保存先のパスを作成
    file_path = "{}/{}.jpg".format(DOWNLOAD_TO, photo["id"])
    # 既に存在すればスキップ
    if os.path.exists(file_path):
        continue
    # データの保存
    urlretrieve(url_q, file_path)
    # スリープ処理
    time.sleep(WAIT_TIME)
