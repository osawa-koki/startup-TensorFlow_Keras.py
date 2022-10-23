from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import numpy as np
import keras
import tensorflow
from PIL import Image
from sklearn import model_selection

# 対象のデータを列挙
classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50


def build_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding="same", input_shape=(50, 50, 3)))
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
    model = load_model("./dataware/model/animal_cnn.hs")
    return model

