# Import Library
import cv2

# 이미지 경로 설정
src = cv2.imread("image/22.jpg")

# src Deep Copy
dst = src.copy()

# 회색조
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

""" 코너 검출 함수
cv2.goodFeaturesToTrack(입력 이미지, 코너 최댓값, 코너 품질, 최소 거리, 마스크, 블록 크기, 해리스 코너 검출기 유/무, 해리스 코너 계수)
입력 이미지 : 8비트 또는 32비트의 단일 채널 이미지 사용.
코너 최대값 : 코너 최대 값보다 낮은 개수만 반환함.
코너 품질 : 반환할 코너의 최소 품질 설정.
최소 거리 : 검출된 코너들의 최소 근접 거리를 나타내며, 설정된 최소 거리 이상의 값만 검출.
마스크 : 입력 이미지와 같은 차원을 사용 하며, 마스크 요소값이 0안 곳은 코너로 계산하지 않음.
블록 크기 : 코너를 계산할 때, 고려하는 코너 주변 영역의 크기를 의미함.
해리스 코너 검출기 유/무 : 해리스 코너 검출 방법 사용 여부를 설정.
해리스 코너 계수 : 해리스 알고리즘을 사용할 때 할당하며 해리스 대각합의 감도 계수를 의미함.
"""
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 5, blockSize=3, useHarrisDetector=True, k=0.03)
# print(corners)

# 코너 검출 함수를 통해 corners가 반환되며, 이 배열안에 코너들의 좌표가 저장되어 있다.
# 반복문을 활용해 dst에 빨간색 원으로 지점을 표시함.
for i in corners:
    cv2.circle(dst, tuple(i[0]), 3, (0, 0, 255), 2)

# 이미지 출력 함수
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey(0)

# 모든 윈도우 창 닫기 함수
cv2.destroyAllWindows()