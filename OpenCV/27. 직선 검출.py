# 직선 검출 알고리즘 : 허프 변환(Hough Transform)을 활용해 직선을 검출함.
# 허프 선 변환은 이미지 내의 어떤 점이라도 선 집합의 일부일 수 있다는 가정하에 직선의 방정식을 이용해 직선을 검출함.
# 표준 허프 변환(Standard Hough Transform) : 이미지 (x, y 평면) 내의 점 p를 지나는 직선의 방정식을 구함.
# 멀티 스케일 허프 변환(Multi-Scale Hough Transform) : 검출한 직선의 값이 더 정확한 값으로 반환 되도록, 거리(p)와 각도(θ)의 값을 조정해 사용함.

# Import Library
import numpy as np
import cv2

# 이미지 경로 설정
src = cv2.imread("image/27.jpg")

# src Deep Copy
dst = src.copy()

# 회색조
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 전처리를 진행하기 위해 그레이 스케일 이미지(gray)와 케니 엣지 이미지(canny)를 사용함.
# 케니 엣지 알고리즘의 임계 값은 각각 5000과 1500으로 주요한 가장 자리만 남긴다.
canny = cv2.Canny(gray, 5000, 1500, apertureSize=5, L2gradient=True)

# cv2.HoughLines(검출 이미지, 거리, 각도, 임계값, 거리 약수, 각도 약수, 최소 각도, 최대 각도)를 이용해서 직선 검출을 진행함.
# 거리와 각도 : 누산 평면에서 사용되는 해상도를 나타냄.
# 임계값 : 하프 변환 알고리즘이 직선을 결정 하기 위해 만족 해야하는 누산 평면의 값을 의미함.
# 누산 평면 : 각도 × 거리의 차원을 갖는 2차원 히스토그램
# 거리 약수와 각도와 각도 약수는 거리와 각도에 대한 약수(divisor)을 의미함.
# 두 값 모두 0의 값을 인수로 활용할 경우, 표준 허프 변환이 적용 되며, 하나 이상의 값이 0이 아니라면 멀티 스케일 허프 변환이 적용됨.
# 최대 각도와 최소 각도는 검출할 각도의 범위를 설정함.
# lines = cv2.HoughLines(canny, 0.8, np.pi / 180, 150, srn=100, stn=200, min_theta=0, max_theta=np.pi)
lines = cv2.HoughLinesP(canny, 0.8, np.pi / 180, 90, minLineLength = 10, maxLineGap = 100)

# 검출을 통해 반환 되는 line 변수는 (N, 1, 2)차원 형태를 가짐.
# 내부 차원 요소는 검출된 거리(rho)와 각도(theta)가 저장 되어있음.
for i in lines:
    # rho, theta = i[0][0], i[0][1]
    # a, b = np.cos(theta), np.sin(theta)
    # x0, y0 = a*rho, b*rho
    #
    # scale = src.shape[0] + src.shape[1]
    #
    # x1 = int(x0 + scale * -b)
    # y1 = int(y0 + scale * a)
    # x2 = int(x0 - scale * -b)
    # y2 = int(y0 - scale * a)
    #
    # cv2.line(dst, (x1, x2), (x2, y2), (0, 0, 255), 2)
    # cv2.circle(dst, (x0, y0), 3, (255, 0, 0), 5, cv2.FILLED)
    cv2.line(dst, (i[0][0], i[0][1]), (i[0][2], i[0][3]), (0, 0, 255), 2)

# 이미지 출력 함수
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey(0)

# 모든 윈도우 창 닫기 함수
cv2.destroyAllWindows()