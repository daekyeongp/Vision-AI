import os
from shutil import copyfile

'''
os, shutil : 파일복사, dir 생성 삭제 등을 다루기 위한 lib
'''

''' 이미지 저장을 위한 이미지 폴더 경로를 만듬. '''
os.mkdir('../images')
word = 'a'
for i in range(0, 26):
    os.mkdir('../images/' + word)
    word = chr(ord(word) + 1)

'''
root 경로에 있는 데이터 세트(Braille) 이미지를 단어에 해당하는 폴더로 나누어 복사
file로 각각의 이미지 이름과 확장자명을 불러오고 alpha_word로 파일의 첫번째 알파벳을 확인
데이터 셋의 모든 파일이 (알파벳)+(구분)+(확장자)로 저장됨
'''
# root = '../Braille Dataset/'
root = '../Example_images/Example_images2/'
for file in os.listdir(root):
    alpha_word = file[0]
    copyfile(root + file, '../images/' + alpha_word + '/' + file)