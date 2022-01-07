import os
import shutil


word = 'zb_space'
# os.mkdir('../images/' + word)
j = '../Braille Dataset/zb_space.png'

for i in range(0, 20):
    print(i, j, '../images/' + word)
    shutil.copy(j, '../images/zb_space/' + word + str(i) + '.jpg')
