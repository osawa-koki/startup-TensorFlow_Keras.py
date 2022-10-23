from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

# 対象のデータを列挙
classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50

# 画像の読み込み
X = []
Y = []
for index, _class in enumerate(classes):
    # 対象のディレクトリ
    photos_dir = "./dataware/collected/animalai/{}".format(_class)
    # 対象の画像一覧を取得
    files = glob.glob(photos_dir + "/*.jpg")
    # 画像を一枚ずつ走査
    for i, file in enumerate(files):
        # 画像を開いて
        image = Image.open(file)
        # 画像をRGB形式に変換して
        image = image.convert("RGB")
        # 画像をリサイズ
        image = image.resize((image_size, image_size))
        # 画像を配列形式に変換して
        data = np.asarray(image)
        # 用意してある配列にプッシュ
        X.append(data)
        Y.append(index)

# scikit-learnで扱いやすい形に変換
X = np.array(X)
Y = np.array(Y)

# 機械学習のトレーニング用と評価用に分類
x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (x_train, x_test, y_train, y_test)
np.save("./dataware/array_converted/animal.npy")
