# Import Library
import cv2

# 이미지 경로 설정
src = cv2.imread("image/23.png")

# src Deep Copy
dst = src.copy()

# 회색조
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

# cv2.moments(배열, 이진화 이미지)
# 배열: 윤곽선 검출 함수에서 반환되는 구조 또는 이미지를 사용.
# 이진화 이미지: 입력된 배열 매개변수가 이미지일 경우, 이미지의 픽셀 값들을 이진화 처리할지 결정.
for i in contours:
    M = cv2.moments(i)
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])

    cv2.circle(dst, (cX, cY), 3, (255, 0, 0), -1)
    cv2.drawContours(dst, [i], 0, (0, 0, 255), 2)

# 이미지 출력 함수
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey(0)

# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()