# Import Library
import numpy as np
import cv2

# 이미지 경로 설정
# 원본 이미지(src)와 연산 값(number1, number2)를 선언함.
# 연산 이미지는 회색 이미지(127, 127, 127)와 검은색 이미지(2, 2, 2)를 사용함.
src = cv2.imread("image/29.jpg")
number1 = np.ones_like(src) * 127
number2 = np.ones_like(src) * 2

# 결과값이 0보다 작다면, 0으로 반환되며, 결과값이 255보다 크다면, 255로 반환됨.
# 만약, 대수적 표현(+, - 등)을 통해 연산을 진행 한다면, 오버플로우(Overflow)나 언더플로우(Underflow)가 발생함.
# 즉, 0 - 2를 진행 한다면 -1이 아닌, 255값이 됩니다.
# 이미지는 uint8로, 256개의 공간(0 ~ 255)을 갖고 있음.
# 더하기
add = cv2.add(src, number1)

# 빼기
sub = cv2.subtract(src, number1)

# 곱하기
mul = cv2.multiply(src, number2)

# 나누기
div = cv2.divide(src, number2)

# 연결 함수(np.concatenate)로 이미지를 연결함.
src = np.concatenate((src, src, src, src), axis=1)
number = np.concatenate((number1, number1, number2, number2), axis=1)
dst = np.concatenate((add, sub, mul, div), axis=1)

dst = np.concatenate((src, number, dst), axis=0)

# 이미지 출력 함수
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey(0)

# 모든 윈도우 창 닫기 함수
cv2.destroyAllWindows()