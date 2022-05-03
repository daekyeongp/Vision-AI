# Import Library
import cv2

# 이미지 경로 설정
src = cv2.imread("image/28.jpg")

# src Deep Copy
dst = src.copy()

# 회색조
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# cv2.HoughCircles(검출 이미지, 검출 방법, 해상도 비율, 최소 거리, 캐니 엣지 임곗값, 중심 임곗값, 최소 반지름, 최대 반지름)을 이용해 원검출.
# 검출 방법 : 2단계 허프 변환 방법(21HT, 그레이디언트)
# 해상도 비율 : 원의 중심을 검출하는데 사용되는 누산 평면의 해상도
# 최소 거리 : 일차적으로 검출된 원과 원 사이의 최소 거리
# 캐니 엣지 임곗값 : 허프 변환에서 자체적으로 캐니 엣지를 적용하게 되는데, 이때 사용되는 상위 임곗값
# 중심 임계값 : 그레이디언트 방법에 적용된 중심 히스토그램에 대한 임계값임. 이 값이 낮을수록 더 많은 원이 검출됨.
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=250, param2=10, minRadius=80, maxRadius=120)


# 검출을 통해 반환되는 circles 변수는 (1, N, 3)차원 형태를 가짐.
# 반복문을 통해 circles 배열에서 중심점과 반지름을 반환할 수 있음.
for i in circles[0]:
    cv2.circle(dst, (int(i[0]), int(i[1])), int(i[2]), (255, 255, 255), 5)

# 이미지 출력 함수
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey(0)

# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()