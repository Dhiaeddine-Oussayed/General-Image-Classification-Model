import os
import cv2
import numpy as np
from tqdm import tqdm
from pickle import dump
from random import shuffle
from datetime import datetime
from tensorflow.keras import Sequential
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import TensorBoard
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten


MAIN_DIRECTORY = '/content/drive/MyDrive/pic_data'
image_shape = (100, 100, 1)
img_size = image_shape[0]
img_dimension = image_shape[-1]



ALL_DATA = []
LABELS = []
for classes in os.listdir(MAIN_DIRECTORY):
  class_path = os.path.join(MAIN_DIRECTORY, classes)
  for picture in tqdm(os.listdir(class_path)):
    picture_path = os.path.join(class_path, picture)
    image = cv2.imread(picture_path, cv2.IMREAD_GRAYSCALE)
    resized = cv2.resize(image, image_shape[:2])
    ALL_DATA.append([resized, classes])
    if classes not in LABELS:
      LABELS.append(classes)
shuffle(ALL_DATA)
number_of_classes = len(LABELS)

x, y = map(list, zip(*ALL_DATA))
x = np.array(x)/255.0

le = LabelEncoder()
encoder = le.fit(y)
y = encoder.transform(y)
y = to_categorical(y, num_classes=number_of_classes)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=image_shape))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Flatten())

model.add(Dense(32, activation='relu'))
model.add(Dense(64, activation='relu'))

model.add(Dense(number_of_classes, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])

%load_ext tensorboard
log_dir = "logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

model.fit(x_train, y_train, epochs=5, validation_split=0.2, 
          callbacks=[tensorboard_callback])
%tensorboard --logdir logs/fit

print("Evaluate on test data")
results = model.evaluate(x_test, y_test)
print("test loss, test acc:", results)

model.save('classification_model')
with open('encoder.pkl', 'wb') as f:
    dump(encoder, f)
