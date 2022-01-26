# Import Library
import cv2

# 역상(Reverse Image)은 영상이나 이미지를 반전 된 색상으로 변환하기 위해 사용.
# 픽셀 단위마다 비트 연산(Bitwise Operation)을 적용하는데, 그중 NOT 연산을 적용.

# 로컬에 있는 이미지 불러 오기
src = cv2.imread("image/10.jpg", cv2.IMREAD_COLOR)

# cv2.bitwise_not(src, mask)는 입력 이미지(src), 마스크(mask)로 출력 이미지(dst)을 생성.
# ps. "not" 연산 이외에도 "and", "or", "xor" 연산이 존재.
dst = cv2.bitwise_not(src)

# 이미지 출력 함수
cv2.imshow("src", src)
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey()

# 모든 윈도우 창 삭제 함수
cv2.destroyAllWindows()