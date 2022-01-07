import streamlit as st
import os
from PIL import Image
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import operator
import Image_predict as predict


def load_my_model():
    model = load_model('./BrailleNet.h5')
    model.summary()

    return model


def load_image(image_file):
    img = Image.open(image_file)

    return img


def set_image(img):
    img = Image.open(img)
    width = img.size[0]
    height = img.size[1]
    length = int(width / height)

    return width, height, length


def remove_file(call_num):
    try:
        os.remove('./test/a/' + str(call_num-1) + '.jpg')
    except:
        pass


def alpha(num):
    if num == 26:
        return ' '
    else:
        num_tr = num + 97
        return chr(num_tr)


def action(model, imagefile):
    predict.chk_trans()
    b = predict.Predict()

    width, height, length = set_image(imagefile)
    b.reset()
    result = []
    call_num = 0
    for i in range(0, length):
        img = Image.open(imagefile)
        area = (0 + call_num * height, 0, width / length * (call_num + 1), height)
        cropped_img = img.crop(area)
        cropped_img.save('./test/a/' + str(call_num) + '.jpg')
        datagen = ImageDataGenerator()
        real_generator = datagen.flow_from_directory('./test',
                                                     target_size=(28, 28))

        my_list = model.predict(real_generator)
        # print('my_list: ', my_list[0])

        index, value = max(enumerate(my_list[0]), key=operator.itemgetter(1))
        print(index, alpha(index))
        result.append(alpha(index))
        call_num += 1
        remove_file(call_num)

    print(result)
    result = ''.join(result)

    return result


# 모델 로드
model = load_my_model()
st.title("Braille Predict Test")
st.subheader("Image")

# 이미지 업로더
image_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if image_file is not None:
    # # 이미지 세부 정보
    # file_details = {"filename": image_file.name, "filetype": image_file.type,
    #                 "filesize": image_file.size}
    load_image = load_image(image_file)

    # 업로드 이미지 시각화
    st.image(load_image, width=700)
    st.subheader('Model Predict')

    # 모델 추론
    st.markdown("""
    <style>
    .big-font {
        font-size: 35px !important;
        text-align: center;
    }
    </style
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">' + action(model=model, imagefile=image_file) + '</p>', unsafe_allow_html=True)
