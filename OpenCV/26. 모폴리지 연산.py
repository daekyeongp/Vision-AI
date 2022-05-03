# 모폴리지 연산(Perspective Calculate) : 모폴리지 변환의 팽창(dilate)과 침식(erosion)을 기본 연산으로 사용해 고급 형태학을 적용하는 변환 연산임.
# 열림(Opening) : 팽창 연산자와 침식 연산자의 조합이며, 침식 연산을 적용한 다음, 팽창 연산을 적용함.
# 닫힘(Closing) : 팽창 연산자와 침식 연산자의 조합이며, 열림과 반대로 팽창 연산을 적용한 다음, 침식 연산을 적용함.
# 그레이디언트(Gradient) : 팽창 연산자와 침식 연산자의 조합이며, 열림 연산이나 닫힘 연산과 달리 입력 이미지에 각각 팽창 연산과 침식 연산을 적용하고 감산을 진행함.
# 탑햇(TopHat) : 입력 이미지(src)와 열림(Opening)의 조합이며, 그레이디언트 연산과 비슷하게 입력 이미지에 열림 연산을 적용한 이미지를 감산함.
# 블랙햇(BlackHat) : 입력 이미지(src)와 닫힘(Closing)의 조합이며, 탑햇 연산과 비슷하게 닫힘 연산을 적용한 이미지에 입력 이미지를 감산함.
# 히트미스(HitMiss) : 이미지 전경이나 배경 픽셀의 특정 패턴을 찾는데 사용하는 이진 형태학으로서 구조 요소의 형태에 큰 영향을 받음.

# Import Library
import numpy as np
import cv2

# 이미지 경로 설정
src = cv2.imread("image/26.jpg")

# cv2.getStructuringElement(커널의 형태, 커널의 크기, 중심점)로 구조 요소 생성.
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))

# cv2.morphologyEx(원본 배열, 연산 방법, 구조 요소, 고정점, 반복 횟수, 테두리 외삽법, 테두리 색상)로 모폴로지 연산 진행
# 아래 코드는 열림 연산 방법임.
dst = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel, iterations=9)

# 이미지 경로 설정
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey(0)

# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()