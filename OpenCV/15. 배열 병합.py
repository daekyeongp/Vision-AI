# Import Library
import cv2

# 이미지 경로 설정
src = cv2.imread("image/14.jpg", cv2.IMREAD_COLOR)
# 이미지 색상을 HSV 변환
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# 채널 분리
h, s, v = cv2.split(hsv)

# 배열 요소의 범위 설정 함수(cv2.inRange)를 사용하여 빨간색 영역의 범위 검출
# 빨간색 영역이 약 0 ~ 5와 약 170 ~ 179 영억의 값을 가짐.
lower_red = cv2.inRange(hsv, (0, 100, 100), (5, 255, 255))
upper_red = cv2.inRange(hsv, (170, 100, 100), (180, 255, 255))

# 색상을 분리한 두 배열을 배열 병합 함수(cv2.addWeighted)로 하나로 병합.
#cv2.addWeighted(src1, src2, beta, gamma, dtype = None): 입력 이미지1(src1)에 대한 가중치1(alpha) 곱과 입력 이미지2(src2)에
# 대한 가중치2(beta) 곱의 합에 추가 합(gamma)을 더해서 계산함.
added_red = cv2.addWeighted(lower_red, 1.0, upper_red, 1.0, 0.0)

red = cv2.bitwise_and(hsv, hsv, mask=added_red)
red = cv2.cvtColor(red, cv2.COLOR_HSV2BGR)

# 이미지 출력 함수
cv2.imshow("red", red)

# 키 입력 대기 함수
cv2.waitKey()


# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()