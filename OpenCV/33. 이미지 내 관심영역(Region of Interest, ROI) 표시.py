import cv2

src = cv2.imread('image/33.jpg')

# ROI 좌표 지정
x, y = 320, 150
w, h = 50, 50
roi = src[y:y+h, x:x+w]

# roi 영역 복사
src2 = roi.copy()

# roi shape (50, 50, 3)
print(roi.shape)

# roi 영역 사각형 그리기
cv2.rectangle(roi, (0, 0), (h-1, w-1), (0, 255, 0))

# 이미지 출력 함수
cv2.imshow("src", src)
cv2.imshow("src2", src2)

# 키 입력 대기 함수
cv2.waitKey(0)

# 모든 윈도우 창 닫기 함수
cv2.destroyAllWindows()