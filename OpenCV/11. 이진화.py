# Import Library
import cv2

# 이진화 : 어느 지점을 기준으로 값이 높거나 낮은 픽셀의 값을 대상으로 특정 연산을 수행할 때 사용.
# 기준값에 따라 이분법적으로 구분해 픽셀을 참 혹은 거짓으로 나눈다.
# 일반적으로 값이 높거나 낮은 픽셀을 검은색 또는 흰색의 값으로 변경.

# 이미지 경로 설정
src = cv2.imread("image/11.jpg", cv2.IMREAD_COLOR)

# 그레이로 설정
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 이진화 함수(cv2.threshold) : 그레일 스케일 이미지에 이진화를 적용 할 수 있다.
# cv2.threshold(src, thresh, maxval, type)는 입력 이미지(src)를 임곗값 형식(type)에 따라
# 임곗값(thresh)과 최댓값(maxval)을 활용하여 설정 임곗값(retval)과 결과 이미지(dst)를 반환
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# 예제에서는 임곗값을 100, 최댓값을 255, 임곗값 형식을 cv2.THRESH_BINARY로 사용하였으므로,
# 픽셀의 값이 100을 초과하는 경우에는 255의 값으로 변경되며, 100 이하의 값은 0으로 변경됩니다.

# 이미지 출력 함수
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey()

# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()