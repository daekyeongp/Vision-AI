import torch
import cv2
import os
from utils import utils_image as util
from models.network_rrdbnet import RRDBNet as net


# 이미지 Path
img_path = 'result/111.jpg'

# GPU 사용
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)

# Model Load
model = net(in_nc=3, out_nc=3, nf=64, nb=23, gc=32, sf=4)
model.load_state_dict(torch.load(os.path.join('model_zoo', 'BSRGAN.pth')), strict=True)
model = model.to(device)
model.eval()

with torch.no_grad():
    img = cv2.imread(img_path)

    # RGB 형태의 3채널 이미지로 변환
    img_L = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

    # 텐서 형태로 변환
    img_L = util.uint2tensor4(img_L)

    # Line 10 device 변수 참조
    img_L = img_L.to(device)

    # 모델을 통해 inference
    img_E = model(img_L)

    # 텐서를 이미지로 변환
    img_E = util.tensor2uint(img_E)

    # 이미지 저장
    util.imsave(img_E, os.path.splitext(img_path)[0] + '_result.png')
