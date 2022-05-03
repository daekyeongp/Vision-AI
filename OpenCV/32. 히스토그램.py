# 히스토그램 : 도수 분포표 중 하나로 데이터의 분포를 몇 개의 구간으로 나누고 각 구간에 속하는 데이터를 시각적으로 표현한 막대그래프이다.
# 빈도 수 (BINS) : 히스토그램 그래프의 X축 간격
# 차원 수 (DIMS) : 히스토그램을 분석할 이미지의 차원
# 범위 (RANGE) : 히스토그램 그래프의 X축 범위

# Import Library
import cv2
import numpy as np

# 이미지 경로 설정
src = cv2.imread("image/32.jpg")

# 그레이 스케일
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 히스토그램 이미지
result = np.zeros((src.shape[0], 256), dtype=np.uint8)

# 히스토그램 계산 함수(cv2.calcHist)
# cv2.calcHist(연산 이미지, 특정 채널, 마스크, 히스토그램 크기, 히스토그램 범위) : 히스토그램 계산
# 특정 채널 : 차원 수 설정
# 마스크 : 특정 영역 연산 / 해당 영역은 없으므로, None 할당
# 히스토그램 크기 : 빈도 수 설정 / 픽셀의 범위 - 0 ~ 255
# 히스토그램 범위 : 범위 설정 / 범위의 범위 - 0 ~ 255
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# 정규화 함수(cv2.normalize)
# cv2.normalize(입력 배열, 결과 배열, alpha beta, 정규화 기준) : 정규화 함.
# cv2.NORM_MINMAX : 정규화 기준을 최소값 - alpha / 최대값 - beta
cv2.normalize(hist, hist, 0, result.shape[0], cv2.NORM_MINMAX)
# 결과를 시각적으로 확인하기 위해 hist 값을 result에 표시함.
# gray와 result는 이미지 높이가 같으므로 병합 함수(np.hstack)로 이미지를 연결함.
for x, y in enumerate(hist):
    cv2.line(result, (x, result.shape[0]), (x, result.shape[0] - int(y)), 255)

dst = np.hstack([gray, result])

# 이미지 출력 함수
cv2.imshow("dst", dst)

# 키 입력 대기 함수
cv2.waitKey(0)

# 모든 윈도우 창 닫기 함수
cv2.destoryAllWindows()