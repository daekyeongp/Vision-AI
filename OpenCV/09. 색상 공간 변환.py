# Import Library
import cv2

# 로컬에 있는 이미지 불러 오기
src = cv2.imread("image/9.jpg", cv2.IMREAD_COLOR)

# 색상 공간 변환 함수: cv2.cvtcolor(src, code, dstCn)
# 입력 이미지(src), 색상 변환 코드(code), 출력 채널(dstCn)으로 출력 이미지(dst)를 생성.
# 색상 변환 코드는 원본 이미지, 색상 공간 결과 이미지 색상 공간을 의미.
# 원본 이미지 색상 공간은 원본 이미지와 일치 해야함.
# BGR2GRAY는 Blue, Green, Red 채널 이미지를 단일 채널, 그레이 스케일 이미지로 변경
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 이미지 출력 함수
cv2.imshow("src", src)
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey()

# 윈도우 창 제거 함수
cv2.destroyAllWindows()