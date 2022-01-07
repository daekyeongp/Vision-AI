from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
from keras import layers as L
from keras.models import Model
from keras.regularizers import l2
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
import matplotlib.pyplot as plt

'''
numpy : 딥러닝에 사용되는 모델들은 주로 array 방식으로 데이터 입력을 받고 출력하는데 이를 다루기 위한 lib
ImageDataenerator : 이미지를 발생시키는 일종의 도구 입니다.
                    경로안의 이미지를 입력받아 Image Dataenerator의 속성을 랜덤으로 적용 하여 분류함함
                    폴더 이름에 따라서 Categorical Variable을 자동으로 생성해 주기 때문에 따로 만들 필요 없음.
                    
ModelCheckpoint : 특정 조건을 만족 했을 때 그때 까지의 모델 상황을 저장. 시간이 오래 걸리는 학습에서 중간 포인트를 저장 하여 
                  저장 시점 부터 다시 학습을 시킬 수도 있고, 최종 결과(가장 좋은 부분)을 저장 할 수 있음
ReduceLROnPlateau : 모델 학습시 학습률 개선을 위한 부분. 
EarlyStopping : 학습시 유의미한 변화가 없는 경우 학습 조기 종료. 
                과대 적합과 과소 적합을 방지할 수 있음.
'''

generator = ImageDataGenerator(rotation_range=20, shear_range=10, validation_split=0.2)

train_generator = generator.flow_from_directory('../images/', target_size=(28, 28), subset='training')

validation_generator = generator.flow_from_directory('../images/', target_size=(28, 28), subset='validation')

'''
모델 생성
SeperableConv2D : 3개의 RGB 채널을 전부 convolution 하는 것이 아닌 따로 적용 하여 
                  합치는 방식 으로 기존의 방법과 비교 했을 때 보다 작은 연산을 하게 되고 성능 상의 이득을 볼수 있음.
'''
K.clear_session()

model_checkpoint = ModelCheckpoint('BrailleNet.h5', save_best_only=True)
reduce_lr = ReduceLROnPlateau(patience=8, verbose=0)
early_stop = EarlyStopping(patience=15, verbose=1)

input_data = L.Input(shape=(28, 28, 3))
x = L.SeparableConv2D(64, (3, 3), activation='relu')(input_data)
x = L.MaxPooling2D((2, 2))(x)

x = L.SeparableConv2D(128, (3, 3), activation='relu')(x)
x = L.MaxPooling2D((2, 2))(x)

x = L.SeparableConv2D(256, (2, 2), activation='relu')(x)
x = L.GlobalMaxPooling2D()(x)

x = L.Dense(256)(x)
x = L.LeakyReLU()(x)

x = L.Dense(64, kernel_regularizer=l2(2e-4))(x)
x = L.LeakyReLU()(x)

x = L.Dense(27, activation='softmax')(x)

model = Model(input_data, x)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

history = model.fit_generator(train_generator, validation_data=validation_generator, epochs=500,
                              callbacks=[model_checkpoint, reduce_lr, early_stop], verbose=1)

'''
모델 학습 결과 시각화
'''
fig, loss_ax = plt.subplots(figsize=(10, 5))
acc_ax = loss_ax.twinx()
loss_ax.plot(history.history['loss'], 'y', label='train loss')
loss_ax.plot(history.history['val_loss'], 'r', label='val loss')
acc_ax.plot(history.history['accuracy'], 'b', label='train acc')
acc_ax.plot(history.history['val_accuracy'], 'g', label='val acc')
loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')
loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()

'''
성능 평가
'''
# Epoch 65: Early Stopping
# model accuracy: 0.963
acc = model.evaluate_generator(validation_generator)[1]
print('model accuracy: {}'.format(round(acc, 4)))

'''
모델 저장
'''
model.save('./model_save/')