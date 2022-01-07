from keras.models import Model, load_model
from keras.preprocessing.image import ImageDataGenerator
import Image_devide as devide
import Image_predict as predict
import os


def load_image(img_path):
    images_dir = img_path
    datagen = ImageDataGenerator()
    real_generator = datagen.flow_from_directory(images_dir,
                                                 target_size=(28, 28))
    return real_generator


def action(path):
    predict.chk_trans()
    b = predict.Predict()
    a = devide.img_devide(path)

    a.create_dir()
    a.set_image()
    b.reset()

    for i in range(0, a.length):
        a.devide_img()
        real = load_image('./test')
        b.Predict(model, real)
        a.remove_file()

    print(b.result)
    result = ''.join(b.result)
    print(result)


model = load_model('./BrailleNet.h5')
path = './Hello_World.png'

action(path)