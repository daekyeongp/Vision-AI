# 모폴리지 변환(Perspective Transformation) : 영상이나 이미지를 형태학적 관점에서 접근하는 기법을 의미함.
# 주로 영상 내 픽셀값 대체에 사용됨. 이를 응용해서 노이즈 제거, 요소 결합 및 분리, 강도 피크 검출 등에 이용함.
# 집합의 포함 관계, 이동, 대칭, 여집합, 차집합 등의 성질 사용.
# 팽창과 침식은 이미지와 커널의 컨벌루션 연산이며, 이 두 가지 기본 연산을 기반으로 복잡하고 다양한 모폴리지 연산을 구현 할 수 있다.

# Import Library
import cv2
import numpy as np

# 이미지 경로 설정
src = cv2.imread("image/25.jpg")

# cv2.getStructuringElement(커널의 형태, 커널의 크기, 중심점)로 구조 요소 생성.
# 커널의 형태 : 직사각형(Rect), 십자가(Cross), 타원(Ellipse)이 있다.
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))

# 팽창 연산 : cv2.dilate(원본 배열, 구조 요소, 고정점, 반복 횟수, 테두리 외삽법, 테두리 색상)
dilate = cv2.dilate(src, kernel, anchor=(-1, -1), iterations=5)

# 침식 연산 : cv2.erode(원본 배열, 구조 요소, 고정점, 반복 횟수, 테두리 외삽법, 테두리 색상)
erode = cv2.erode(src, kernel, anchor=(-1, -1), iterations=5)

# 연결 함수 : np.concatenate(연결할 이미지 배열들, 축 방향) 이미지 연결
dst = np.concatenate((src, dilate, erode), axis=1)

# 이미지 출력 함수
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey(0)

# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()