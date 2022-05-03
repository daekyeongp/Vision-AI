"""기하학적 변환(Geometric Transform)
: 이미지를 인위적으로 확대, 축소, 위치 변경, 회전, 왜곡하는 등 이미지의 형태를 변환하는 것을 의미함."""
# 아핀 변환(Affine Transformation): 2X3 행렬을 사용하며, 행렬 곱셈에 벡터 합을 이용하여 표현할 수 있는 변환을 의미.
# 원근 변환(Perspective Transformation): 3X3 행렬을 사용하며, 호모그래피(Homofraphy)로 모델링 할 수 있는 변환을 의미.

# Import Library
import cv2
import numpy as np

# 이미지 경로 설정
src = cv2.imread("image/18.jpg", cv2.IMREAD_COLOR)
height, width, channel = src.shape

"""원근 변환 
: 매핑에 사용할 변환 전 원본 이미지의 픽셀 좌표(srcPoint)과 변환 후 결과 이미지의 픽셀 좌표(dstPoint) 선언."""
srcPoint = np.array([[300, 200], [400, 200], [500, 500], [200, 500]], dtype=np.float32)
dstPoint = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

"""원근 맵 행렬 생성 함수 : 매핑 좌표에 대한 원근 맵 행렬을 생성 할 수 있다.
cv2.GetPerspectiveTransform(src, dst)
: 변환 전 네 개의 픽셀 좌표(src)과 변환 후 네 개의 픽셀 좌표(dst)를 기반으로 원근 맵 행렬(M)을 생성함."""
matrix = cv2.getPerspectiveTransform(srcPoint, dstPoint)

"""원근 변환 함수 : 원근 맵 행렬에 대한 기하학적 변환을 수행 할 수 있다.
cv2.warpPerspective(src, M, dsize, dst, flags, borderMode, borderValue)
: 입력 이미지(src)에 원근 맵 행렬(M)을 적용하고, 출력 이미지 크기(dsize)로 변형해서 출력 이미지(dst)를 반환함.
이미지를 변환하기 때문에 보간법(flags)과 테두리 외삽법(borderMode), 테두리 색상(borderValue)을 적용 가능."""
dst = cv2.warpPerspective(src, matrix, (width, height))

# 이미지 출력 함수
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey()

# 윈도우 제거 함수
cv2.destroyAllWindows()