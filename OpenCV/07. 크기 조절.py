# Import Library
import cv2

# 로컬에 있는 이미지 불러 오기
src = cv2.imread("image/7.jpg", cv2.IMREAD_COLOR)

# cv2.resize(src, dstSize, fx, fy, interpolation) 이미지 크기 조절 함수
#  입력 이미지(src), 절대 크기(dstSize), 상대 크기(fx, fy), 보간법(interpolation)으로 출력 이미지(dst)를 생성.
dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

# 이미지 출력 함수
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
# 키 입력 대기 함수
cv2.waitKey()
# 윈도우 창 제거 함수
cv2.destroyAllWindows()