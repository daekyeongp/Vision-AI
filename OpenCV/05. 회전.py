# Import Library
import cv2

# 로컬에 있는 이미지 불러 오기
src = cv2.imread("image/5.jpg", cv2.IMREAD_COLOR)

# 해당 이미지의 높이, 너비, 채널의 값을 저장.
height, width, channel = src.shape

# 높이와 너비를 이용하여 회전 중심점을 설정.
# 2×3 회전 행렬 생성 함수(cv2.getRotationMatrix2D)로 회전 변환 행렬을 계산.
# 중심점, 각도, 비율, 매핑 변환 행렬 생성
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)

# 회전 변환 계산
# cv2.warpAffine(src, M, dsize)
# 원본 이미지(src)에 아핀 맵 행렬(matrix)을 적용하고 출력 이미지(dsize) 크기로 변형해서 출력 이미지(dst)를 반환.
dst = cv2.warpAffine(src, matrix, (width, height))

# 이미지 출력
cv2.imshow("src", src)
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey()

# 윈도우 창 제거 함수
cv2.destroyAllWindows()