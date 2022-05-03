# 도형 그리기 : 영상이나 이미지 위에 그래픽을 그려 검출 결과를 시각적으로 표시함.
# 선형 타입(Line Types) : 도형을 그릴 때 어떤 유형의 선으로 그릴지 결정.
# 비트 쉬프트(bit Shift) : 서브 픽셀(Sub Pixel) 정렬을 지원해서 소수점 이하 자리수를 표현 가능.

# Import Library
import cv2
import numpy as np

# 그림판 만들기
src = np.zeros((768, 1366, 3), dtype=np.uint8)

"""직선 그리기 함수(cv2.line)
cv2.line(src, pt1, pt2, color, thickness, lineType, shift)
: 입력 이미지(src)에 시작 좌표(pt1)부터 도착 좌표(pt2)를 지나는 특정 색상(color)과 두께(thinkness)의 직선을 그림."""
src = cv2.line(src, (100, 100), (1200, 100), (0, 0, 255), 3, cv2.LINE_AA)

"""원 그리기 함수(cv2.circle)
cv2.circle(src, center, radius, color, thickness, lineType, shift)
: 입력 이미지(src)에 중심점(center)으로 부터 반지름(radius) 크기의 특정 색상(color)과 두께(thickness)의 원을 그림."""
src = cv2.circle(src, (300, 300), 50, (0, 255, 0), cv2.FILLED, cv2.LINE_4)

"""사각형 그리기 함수(cv2.rectangle)
cv2.rectangle(src, pt1, pt2, color, thickness, lineType, shift)
입력 이미지(src)에 좌측 상단 모서리 좌표(pt1)부터 우측 하단 모서리 좌표(pt2)로 
구성된 특정 색상(color), 두께(thickness)의 사각형을 그림."""
src = cv2.rectangle(src, (500, 200), (1000, 400), (255, 0, 0), 5, cv2.LINE_8)

"""호 그리기 함수(cv2.ellipse)
cv2.ellipse(src, center, axes, angle, startAngle, endAngle, color, lineType, shift)
: 입력 이미지(src)에 중심점(center)으로 부터 장축과 단축(axes) 크기를 갖는 
특정 색상(color)과 두께(thickness)의 호를 그림."""
src = cv2.ellipse(src, (1200, 300), (100, 50), 0, 90, 180, (255, 255, 0), 2)

# poly 함수를 사용하는 경우, numpy 형태로 저장된 위치 좌표들이 필요함.
# n개의 점이 저장된 경우, n각형을 그릴 수 있음.
pst1 = np.array([[100, 500], [300, 500], [200, 600]])
pts2 = np.array([[600, 500], [800, 500], [700, 600]])

"""내부가 채워지지 않은 다각형 그리기 함수(cv2.polylines)
cv2.ellipse(src, pts, isClosed, color, thickness, lineType, shift)
: 입력 이미지(src)에 선들의 묶음(pts)이 이뤄진 N개의 내구가 채워지지 않은 다각형을 그림.
닫힘 여부(isClosed)를 설정해 처음 좌표와 마지막 좌표의 연결 여부를 설정 하며, 
설정한 색상(color)과 두께(thickness)의 다각형이 그려짐."""
src = cv2.polylines(src, [pst1], True, (0, 255, 255), 2)

"""내부가 채워진 다각형 그리기 함수(cv2.fillPoly)
cv2.ellipse(src, pts, color, thickness, lineType, shift, offset)
: 입력 이미지(src)에 선들의 묶음(pts)이 이뤄진 N개의 내부가 채워지지 않은 다각형을 그림.
설정한 색상(color)과 두께(thickness)의 다각형이 그려짐."""
src = cv2.fillPoly(src, [pts2], (255, 0, 255), cv2.LINE_AA)

"""문자 그리기 함수(cv2.putText)
cv2.putText(src, text, org, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin)
: 입력 이미지(src)에 문자열(text)을 텍스트 박스의 좌측 상단 모서리(org)를 기준으로 문자가 그려짐.
설정한 글꼴(fontFace)과 글자 크기(fontScale), 색상(color)과 두께(thickness)의 다각형이 그려짐."""
src = cv2.putText(src, "DaeKyeong", (900, 600), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)

""" 선형 타입 종류
cv2.FILLED	내부 채우기
cv2.LINE_4	4점 이웃 연결
cv2.LINE_8	8점 이웃 연결
cv2.LINE_AA	AntiAlias
"""

""" 글꼴 종류
cv2.FONT_HERSHEY_SIMPLEX    	보통 크기의 산세리프 글꼴
cv2.FONT_HERSHEY_PLAIN          작은 크기의 산세리프 글꼴
cv2.FONT_HERSHEY_DUPLEX         보통 크기의 산세리프 글꼴
cv2.FONT_HERSHEY_COMPLEX	    보통 크기의 세리프 글꼴
cv2.FONT_HERSHEY_TRIPLEX	    보통 크기의 세리프 글꼴
cv2.FONT_HERSHEY_COMPLEX_SMALL	작은 크기의 손글씨
cv2.FONT_HERSHEY_SCRIPT_SIMPLEX	보통 크기의 손글씨
cv2.FONT_HERSHEY_SCRIPT_COMPLEX	보통 크기의 손글씨
cv2.FONT_ITALIC	                기울임 꼴
"""

# 이미지 출력 함수
cv2.imshow("src", src)

# 키 입력 대기 함수
cv2.waitKey()

# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()