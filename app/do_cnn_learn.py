from keras.model import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import numpy as np

# 対象のデータを列挙
classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50

# メイン処理
def main():
    x_train, x_test, y_train, y_test = np.load("./dataware/array_converted/animal.npy")
    # 「0-256」から「0-1」の範囲へ変換 
    x_train = x_train.astype("float") / 256
    x_test = x_test.astype("float") / 256
    # 「one-hot-vector」に変換(正解値は1で、それ以外は0)
    # 例えば「monkey」「boar」「crow」を対象に、それがmonkeyであれば[1, 0, 0]、それがboarであれば「0, 1, 0」、それがcrowであれば、「0, 0, 1」
    y_train = np_utils.to_categorical(y_train, num_classes)
    y_test = np_utils.to_categorical(y_test, num_classes)

    model = model_train(x_train, y_train)
    model_eval(model, x_test, y_test)



