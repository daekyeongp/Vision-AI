# 비트 연산 : 하나 또는 두 이미지에 대해 비트 연산을 수행함. (비트 연산 표현 &, | 등)

# Import Library
import numpy as np
import cv2

# 이미지 경로 설정
# 원본 이미지(src)와 그레이 스케일
# p(gray), 이진화(binary)을 선언함.
# 연산 이미지는 그레이 스케일 이미지와 127 임계값을 갖는 이진화 이미지를 사용함.
src = cv2.imread("image/31.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# cv2.bitwise(연산 이미지1, 연산 이미지2) : 비트 연산을 진행함.
# 논리곱(bitwise_and), 논리합(bitwise_or), 배타적 논리합(bitwise_xor), 부정(bitwise_not) 등으로 연산이 가능함.
_and = cv2.bitwise_and(gray, binary)
_or = cv2.bitwise_or(gray, binary)
_xor = cv2.bitwise_xor(gray, binary)
_not = cv2.bitwise_not(gray)

# 연결 함수(cv2.concatenate) : 이미지를 연결함.
src = np.concatenate((np.zeros_like(gray), gray, binary, np.zeros_like(gray)), axis=1)
dst = np.concatenate((_and, _or, _xor, _not), axis=1)
dst = np.concatenate((src, dst), axis=0)
"""
None : _and / gray : _or / binary : _xor / None : _not
"""


# 이미지 출력 함수
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey(0)

# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()