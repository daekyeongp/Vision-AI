# Import Library
import cv2

# 이미지 경로 설정
src = cv2.imread("image/23.png")

# src Deep Copy
dst = src.copy()

# 회색조로 바꾸기
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

# cv2.convexHull(윤곽선, 방향)을 사용해 윤곽선에서 블록 껍질을 검출.
# 윤곽선 : 윤곽선 검출 함수에서 반환되는 구조를 사용함.
# 방향 : 검출된 블록 껍질의 볼록점들의 인덱스 순서를 의미함. 방향이 True라면 시계 방향, False라면 반시계 방향으로 정렬.
for i in contours:
    hull = cv2.convexHull(i, clockwise=True)
    cv2.drawContours(dst, [hull], 0, (0, 0, 255), 2)

# 이미지 출력 함수
cv2.imshow("dst", dst)
# 키 입력 대기함수
cv2.waitKey(0)
# 모든 윈도우 창 닫기
cv2.destroyAllWindows()