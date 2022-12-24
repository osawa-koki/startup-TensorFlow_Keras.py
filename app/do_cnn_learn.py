from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import numpy as np
import keras
import tensorflow

# 対象のデータを列挙
classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50

# メイン処理
def main():
    x_train, x_test, y_train, y_test = np.load("./dataware/array_converted/animal.npy", allow_pickle=True)
    # 「0-256」から「0-1」の範囲へ変換 
    x_train = x_train.astype("float") / 256
    x_test = x_test.astype("float") / 256
    # 「one-hot-vector」に変換(正解値は1で、それ以外は0)
    # 例えば「monkey」「boar」「crow」を対象に、それがmonkeyであれば[1, 0, 0]、それがboarであれば「0, 1, 0」、それがcrowであれば、「0, 0, 1」
    y_train = np_utils.to_categorical(y_train, num_classes)
    y_test = np_utils.to_categorical(y_test, num_classes)

    model = model_train(x_train, y_train)
    model_eval(model, x_test, y_test)

def model_train(x, y):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding="same", input_shape=x.shape[1:]))
    model.add(Activation("relu"))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    
    model.add(Conv2D(64, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    
    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation("relu"))
    model.add(Dropout(0.5))
    model.add(Dense(3))
    model.add(Activation("softmax"))

    opt = tensorflow.keras.optimizers.RMSprop(lr = 0.0001, decay = 1e-6)
    model.compile(loss = "categorical_crossentropy", optimizer = opt, metrics = ["accuracy"])
    model.fit(x, y, batch_size = 32, epochs = 100)
    model.save("./dataware/model/animal_cnn.hs")
    return model

def model_eval(model, x, y):
    scores = model.evaluate(x, y, verbose = 1)
    print("Test loss: {}".format(scores[0]))
    print("Test accuracy: {}".format(scores[1]))
    
if __name__ == "__main__":
    main()
