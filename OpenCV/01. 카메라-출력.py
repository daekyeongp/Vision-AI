# 카메라 출력

# Import Library
import cv2

# 웹캠 로드
# cv2.VideoCapture(index) index: 0번은 내장 카메라 1번부터 순서 대로 외장 카메라
cap = cv2.VideoCapture(0)

# capture.set(propid, value)
# propid: 변경하려는 카메라 설정, value: 카메라 설정의 속성 값
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)

# cv2.waitKey(delay) delay: delay 시간 동안 키 입력을 기다린다.
# 계속 카메라 프레임을 받아온다.
# while cap.isOpened():
while cv2.waitKey(33) < 0:
    # read() 카메라의 상태와 프레임을 받아온다.
    # ret은 카메라의 상태를 받아오면 정상 : True / 비정상 : False 반환
    # Frame은 현재 시점의 프레임을 저장한다.
    ret, frame = cap.read()
    # imshow(윈도우 이름, 이미지) : 윈도우 창의 제목(win name)과 이미지(mat)
    cv2.imshow("VideoFrame", frame)

# 카메라 장치에서 받아온 메모리 해제
cap.release()
# 모든 윈도우 창 제거
cv2.destroyAllWindows()
# 특정 윈도우 창만 닫기
# cv2.destroyAllWindows(winname)
