# Import Library
import cv2

# 이미지 경로 설정
src = cv2.imread("Image/12.jpg", cv2.IMREAD_COLOR)

# 단순 흐림 흐림 효과 함수(cv2.blur)로 입력 이밎에 흐림 효과를 적용 할 수 있다.
# cv2.blur(src, ksize, anchor, borderType)는 입력 이미지(src)를
# 커널 크기(ksize), 고정점(anchor), 테두리 외삽법(borderType)으로 흐림 효과를 적용한 결과 이미지(dst)를 반환.
dst = cv2.blur(src, (9, 9), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)

"""커널 : 이미지(x, y)의 픽셀과 해당 픽셀 주변을 포함한 작은 크기 공간
영역의 형태와 요소가 결합되는 방식을 정의하는 템플릿 의미, 신호 처리 분야에서는 필터라고도 함."""
"""고정점 : 커널을 통해 컨벌루션된 값을 할당한 지점
새로운 픽셀을 만들어 내기 이해 커널 크기의 화소 값을 이용해 어떤 시스템을 통과해 계산 하는 것을 의미."""
"""테두리 외삽법 : 컨벌루션을 적용할 때, 이미지 가장자리 부분의 처리 방식을 의미"""

# 이미지 출력 함수
cv2.imshow("src", src)
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey()

# 윈도우 창 제거 함수
cv2.destroyAllWindows()