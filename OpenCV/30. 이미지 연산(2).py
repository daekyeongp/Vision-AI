# Import Library
import numpy as np
import cv2

# 이미지 경로 설정
src = cv2.imread("image/29.jpg")

# 회색조 이미지로 설정
number = np.ones_like(src) * 127

# cv2.Calc(연산 이미지1, 연산 이미지2)를 이용하여 이미지 연산을 진행함.
# 최대값(max), 최소값(min), 절대값 차이(absdiff), 비교(compare) 등으로 연산이 가능함.
# 최대값 함수 : 두 이미지의 요소별 최대값을 계산함.
# 최소값 함수 : 두 이미지의 요소별 최소값을 계산함.
# 절대값 차이 함수 : 두 이미지의 요소별 절대값 차이를 계산함.
# 덧셈 함수나 뺄셈 함수에서는 두 배열의 요소를 서로 뺄셈했을 때 음수가 발생하면 0을 반환했지만 절댓값 차이 함수는 이 값을 절대값으로 변경해서 양수 형태로 반환함.
# 비교 함수 : 두 이미지의 요소별 비교 연산을 수행함.
# 비교 결과가 True면 255 / False면 0
_max = cv2.max(src, number)
_min = cv2.min(src, number)
_abs = cv2.absdiff(src, number)
compare = cv2.compare(src, number, cv2.CMP_GT)

""" 비교 함수 플래그
cv2.CMP_EQ : src1와 src2의 요소가 같음
cv2.CMP_NE : src1와 src2의 요소가 같지 않음
cv2.CMP_GT : src1와 src2의 요소가 큼
cv2.CMP_GE : src1와 src2의 요소가 작음
cv2.CMP_LT : src1와 src2의 요소가 작음
cv2.CMP_LE : src1와 src2의 요소가 작거나 같음
"""

# 연결 함수(np.concatenate)로 이미지를 연결함.
src = np.concatenate((src, src, src, src), axis=1)
number = np.concatenate((number, number, number, number), axis=1)
dst = np.concatenate((_max, _min, _abs, compare), axis=1)

dst = np.concatenate((src, number, dst), axis=0)

# 이미지 출력 함수
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey(0)

# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()