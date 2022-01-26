# HSV(Hue, Saturation, Value)공간은 색상을 표현하기에 간편한 색상 공간
# 색상(Hue) : 빨간색, 노란색 파란색 등으로 인식되는 색상 중 하나 또는 둘의 조합과 유사한 것처럼 보이는
# 시각적 감각의 속성
# 채도(Saturation) : 이미지의 색상 깊이로, 색상이 얼마나 선명한(순수한) 색인지 의미
# 명도(value) : 색의 밝고 어두운 정도

# Import Library
import cv2

""" Main Code
# 이미지 경로 설정
src = cv2.imread("image/14.jpg", cv2.IMREAD_COLOR)
# 색상 공간 변환 함수(cv2.cvtColor)로 이미지 색상 공간을 BGR에서 HSV로 변경.
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# cv2.split : 채널 분리 함수
h, s, v = cv2.split(hsv)
# ps. cv2.threshold(src)는 입력 이미지(src)의 채널을 분리하여 배열의 형태로 변환

# 이미지 출력 함수
cv2.imshow("src", src)
cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)
# 키 입력 대기 함수
cv2.waitKey()
# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()"""


# 이미지 경로 설정
src = cv2.imread("image/14.jpg", cv2.IMREAD_COLOR)
# 색상 공간 변환 함수(cv2.cvtColor)로 이미지 색상 공간을 BGR에서 HSV로 변경.
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# cv2.split : 채널 분리 함수
h, s, v = cv2.split(hsv)

# Hue의 범위를 조정해서 특정 색상의 범위만 출력 할 수 있음.
# cv2.inRange(src, lowerb, upperb) : 입력 이미지(src)의 낮은 범위(lowerb)에서 높은 범위(upperb) s사이의 요소를 추출.

h = cv2.inRange(h, 8, 20)
# 비트연산 AND(cv2.bitwise_and)로 간단하게 마스크를 덧 씌울 수 있다.
# cv2.bitwise_and(src1, src2, mask) : 입력 이미지1(src1)과 입력 이미지2(src2)의 픽셀의 이진값이 동일한 영역만 AND 연산하여 반환.
orange = cv2.bitwise_and(hsv, hsv, mask = h)
orange = cv2.cvtColor(orange, cv2.COLOR_HSV2BGR)

# 이미지 출력 함수
cv2.imshow("orange", orange)
# 키 입력 대기 함수
cv2.waitKey()
# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()