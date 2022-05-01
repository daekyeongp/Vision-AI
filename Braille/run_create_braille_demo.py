import glob
import streamlit as st
from PIL import Image


# 이미지 사이즈 확인
def image_size(files, sentence_len):
    x_size = []
    y_size = []
    for file in files:
        image = Image.open(file)
        x_size.append(image.size[0])
        y_size.append(image.size[1])

    x_min = min(x_size)
    y_min = min(y_size)
    total_length_size = x_min * sentence_len

    return x_min, y_min, total_length_size


# 이미지 병합
def image_merge(x_size, x_min, y_min, sentence ,sentence_join):
    file = []
    new_image = Image.new("RGB", (x_size, y_min), (256, 256, 256))

    for files in sentence:
        image = Image.open('./example_images/' + files + '.png')
        image_file = image.resize((x_min, y_min))
        file.append(image_file)

    for idx in range(len(file)):
        # 시작점 가로, 시작점 세로, 이미지의 가로 크기, 이미지의 세로 크기
        area = ((idx * x_min), 0, (x_min * (idx + 1)), y_min)
        new_image.paste(file[idx], area)
    st.image(new_image, width=700)
    # new_image.show()
    new_image.save('./create_braille/' + sentence_join + '.png', 'PNG')


st.title("Braille Test Data Create")
st.subheader("Input Sentence")
sentence = st.text_input(label='Sentence', key='sentence')
# 입력된 문장 list 변환
sentence = list(st.session_state.sentence)
sentence_len = len(sentence)
sentence_join = ''.join(sentence)

# braille 이미지 glob
image_dir = "./example_images/"
files = glob.glob(image_dir + "*.png")

for i in range(len(sentence)):
    if ' ' in sentence:
        sentence_replace = sentence.index(' ')
        sentence[sentence_replace] = 'zb_space'

# 입력된 단어에 해당하는 사진 분리
files = [file for file in files if file.split('\\')[1].split('.')[0] in sentence]

# print(type(files))
# print(files)

# 이미지 각 사이즈 확인
x_min, y_min, x_size = image_size(files, sentence_len)
image_merge(x_size, x_min, y_min, sentence, sentence_join)