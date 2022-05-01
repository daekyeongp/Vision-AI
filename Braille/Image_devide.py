from PIL import Image
import os
import operator


class img_devide():
    def __init__(self, img_path):
        self.img_path = img_path
        self.path = ''
        self.call_num = 0
        self.length = 0
        self.width = 0
        self.height = 0
        self.img = ''

    def create_dir(self):
        try:
            os.mkdir('./test/sentence')
            print('create dir')
        except:
            print('already exist')
            pass
        self.path = './test/sentence'

    def devide_img(self):
        self.img = Image.open(self.img_path)
        area = (0 + self.call_num * self.height, 0, self.width / self.length * (self.call_num + 1), self.height)
        cropped_img = self.img.crop(area)
        cropped_img.save(self.path + '/' + str(self.call_num) + '.jpg')

        self.call_num += 1


    def set_image(self):
        self.img = Image.open(self.img_path)
        self.width = self.img.size[0]
        self.height = self.img.size[1]
        self.length = int(self.width / self.height)

    def remove_file(self):
        try:
            os.remove(self.path + '/' + str(self.call_num-1) + '.jpg')
        except:
            pass

    def remove_dir(self):
        try:
            os.rmdir(self.path)
        except :
            print('fail')
