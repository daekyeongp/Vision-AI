from keras.preprocessing.image import img_to_array
from keras import backend as K
from keras import layers as L
from keras.models import Model, load_model
from keras.regularizers import l2
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os


def braille_predict(path):
    img = Image.open(path).convert('RGB')
    img = img.resize((28, 28))
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    return x


def decode_predict(result, lables):
    max = np.max(result)
    index = np.where(result == max)
    # print('index: ', index)
    return lables[index[1][0]]


model = load_model('./BrailleNet.h5')

'''
모델 테스트
'''
# test_img = braille_predict('../images/a/a_0_376.jpg')
# result = model.predict(test_img)
#
# max = np.max(result)
# index = np.where(result == max)
#
# # 0.999683 0
# print(max, *index[1])
# exit(0)

'''
Label 사용하여 예측
'''
os.chdir('../example_images')
example_word = os.listdir()
print(dir)

tmp = []
for file in example_word:
    tmp.append(file.split('.')[0])
example_word = tmp
example_word.sort()
example_word[example_word.index('zb_space')] = ' '
print(example_word)

test_img = braille_predict('a.png')
result = model.predict(test_img)

print(f'Model Predict: {decode_predict(result, example_word)}')