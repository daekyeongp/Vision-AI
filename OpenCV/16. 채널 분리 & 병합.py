# Import Library
import cv2
import numpy as np

# 채널 분리(Split)과 병합(Merge)은 영상이나 이미지의 색상 공간의 채널을 분리하거나 합치기 위해 사용.
# ps. OpenCV의 가산 혼합의 삼원 색 기본 배열 순서는 BGR임.

# 이미지 경로 설정
src = cv2.imread("image/16.jpg", cv2.IMREAD_COLOR)

# # 채널 분리 함수
# # cv2.split(src) : 입력 이미지(src)에서 채널을 분리해 단일 채널 이미지 배열(mv)을 생성함.
# # mv는 목록(list) 형식으로 반환 되며, b, g, r 등의 형태로 각 목록의 원소 값을 변수로 지정할 수 있음.
# b, g, r = cv2.split(src)
#
# # 채널 병합 함수(cv2.merge)로 채널된 채널을 병합해 하나의 이미지로 합칠 수 있음.
# # cv2.merge(mv)로 단일 채널 이미지 배열(mv)를 병합해 출력 이미지(dst)를 생성.
# inverse = cv2.merge((r, g, b))
#
# # 이미지 출력 함수
# cv2.imshow("b", b)
# cv2.imshow("g", g)
# cv2.imshow("r", r)
# cv2.imshow("inverse", inverse)
#
# # 키 입력 대기 함수
# cv2.waitKey()
#
# # 모든 윈도우 창 제거 함수
# cv2.destroyAllWindows()

# numpy 형식 채널 분리
# 이미지[높이, 너비, 채널]을 이용하여 특정 영역의 특정 채널만 불러올 수 있음.
# :, :, n을 입력할 경우, 이미지 높이와 너비를 그대로 반환하고 n번째 채널만 반환하여 적용.
# src[..., n]의 형태로도 사용 가능.
b = src[:, :, 0]
g = src[:, :, 1]
r = src[:, :, 2]

height, width, channel = src.shape

# 검은색 빈 공간 이미지가 필요할 때는 np.zeros((높이, 너비, 채널), dtype=정밀도)을 이용해 빈 이미지를 생성할 수 있음.
# 특정 색상의 이미지를 생성하려는 경우에는 np.full((높이, 너비, 채널), (b, g, r), dtype=정밀도)을 이용해 특정 색상 이미지를 생성할 수 있음.
zero = np.zeros((height, width, 1), dtype=np.uint8)

bgz = cv2.merge((b, g, zero))

cv2.imshow("bgz", bgz)
cv2.waitKey()
cv2.destroyAllWindows()