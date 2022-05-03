# Import Library
import cv2

# 이미지 경로 설정
src = cv2.imread("image/21.jpg", cv2.IMREAD_COLOR)

# 회색조
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
binary = cv2.bitwise_not(binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

# 반복문을 사용하여 색인 값과 하위 윤곽선 정보로 반복. 근사치 정확도를 계산 하기 위해 윤곽선 전체 길이의 2%로 활용함.
# cv2.arcLength(윤곽선, 폐곡선)
# 윤곽선 : 검출된 윤곽선들이 저장된 Numpy 배열.
# 폐곡선 : 검출된 윤곽선이 닫혀 있는지, 열려 있는지 설정.

# 다각형 근사는 더글라스-패커(Douglas-Peucker) 알고리즘을 사용함.
# 반복과 끝점을 이용해 선분으로 구성된 윤곽선들을 더 적은 수의 윤곽점으로 동일하거나 비슷한 윤곽선으로 데시메이트(decimate) 함.
# 데시메이트란 일정 간격으로 샘플링 된 데이터를 기존 간격 보다 더 큰 샘플링 간격으로 다시 샘플링하는 것을 의미.
for contour in contours:
    epsilon = cv2.arcLength(contour, True) * 0.02
    approx_poly = cv2.approxPolyDP(contour, epsilon, True)

    for approx in approx_poly:
        cv2.circle(src, tuple(approx[0]), 3, (255, 0, 0), -1)

# 이미지 출력 함수
cv2.imshow("src", src)

# 키 입력 대기 함수
cv2.waitKey(0)

# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()