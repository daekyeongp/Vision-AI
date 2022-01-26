# Import Library
import cv2

# 로컬에 있는 이미지 불러 오기
src = cv2.imread("image/6.jpg", cv2.IMREAD_COLOR)

# 높이, 너비, 채널 값 저장
height, width, channel = src.shape

# 이미지 2배 확대
# cv2.pyrUp(src, dstSize, borderType): 입력 이미지(src), 출력 이미지 크기(dstSize),
# 테두리 외삽법(borederType)로 출력 이미지(dst)을 생성.
dst = cv2.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)

# 이미지 2배 축소
dst2 = cv2.pyrDown(src)

# 이미지 출력
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)

# 키 입력 대기 함수
cv2.waitKey()

# 윈도우 창 제거 함수
cv2.destroyAllWindows()