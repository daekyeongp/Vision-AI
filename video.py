import os
import torch
import cv2
from utils import utils_image as util
from models.network_rrdbnet import RRDBNet as net


VIDEO_PATH = '1.mp4'
model_path = os.path.join('model_zoo', 'BSRGAN.pth')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = net(in_nc=3, out_nc=3, nf=64, nb=23, gc=32, sf=4)

model.load_state_dict(torch.load(model_path), strict=True)
model.eval()
for k, v in model.named_parameters():
    v.requires_grad = False
model = model.to(device)

cap = cv2.VideoCapture(VIDEO_PATH)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('%s_output.mp4' % (VIDEO_PATH.split('.')[0]), fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) * 4), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * 4)))

n_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
i = 0

print(n_frames)
cap.set(cv2.CAP_PROP_POS_FRAMES, i)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    # RGB 형태의 3채널 이미지로 변환
    img_L = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 텐서 형태로 변환
    img_L = util.uint2tensor4(img_L)

    # Line 11 device 변수 참조
    img_L = img_L.to(device)

    # 모델을 통해 inference
    img_E = model(img_L)

    # 텐서를 이미지로 변환
    img_E = util.tensor2uint(img_E)

    # RGB 형태의 3채널 이미지로 변환
    img_E = cv2.cvtColor(img_E, cv2.COLOR_RGB2BGR)

    out.write(img_E)

    i += 1
    print('%d/%d' % (i, n_frames))

out.release()
cap.release()
