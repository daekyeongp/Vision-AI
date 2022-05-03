# Import Library
import cv2

# 이미지 경로 설정
src = cv2.imread("Image/20.png", cv2.IMREAD_COLOR)

# 윤곽선(컨투어)를 검출하는 주된 요소는 하얀색의 객체를 검출
# 즉, 흑백화 시켜 배경은 검정 물체는 하얀색의 성질을 띄게끔 변형.
gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)

# cv2.findContours : 이진화 처리 후 반전 시켜서 이미지에 검출하려는 물체를 하얀색의 성질을 띄도록 변환.
# cv2.findContours(이진화 이미지, 검색 방법, 근사화 방법) : 반환 값으로 윤곽선, 계층 구조를 반환함.
contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
# 윤곽선은 Numpy 구조의 배열로 윤곽선의 지점들이 담겨있음, 계층 구조는 윤곽선의 계충 구조를 의미함.

# cv2.drawContours() : 검출된 윤곽선을 그림.
# cv2.drawContours(이미지, [윤곽선], 윤곽선 인덱스, (B, G, R), 두께, 선형 타입)
for i in range(len(contours)):
    cv2.drawContours(src, [contours[i]], 0, (0, 0, 255), 2)
    cv2.putText(src, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
    print(i, hierarchy[0][i])
    cv2.imshow("src", src)
    cv2.waitKey(0)

cv2.destroyAllWindows()
