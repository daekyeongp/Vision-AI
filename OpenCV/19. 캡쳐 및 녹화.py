# Import Library
import datetime
import cv2

# 비디오 경로 설정 함수
cap = cv2.VideoCapture("image/3.mp4")

# 디지털 미디오 포맷 코드 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 녹화 유/무 설정
record = False

while True:
    # 영상 무한 재생
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.open("image/3.mp4")

    # ret : 카메라 작동 유/무
    # frame = 이미지 읽어 저장 하기
    ret, frame = cap.read()
    cv2.imshow("VideoFrame", frame)

    # now에 파일의 제목을 설정함 : 날짜_시간-분-초 형식
    now = datetime.datetime.now().strftime("%d_%H-%M-%S")

    # 33ms 마다 키보드 키의 값이 저장 된다.
    key = cv2.waitKey(33)

    """ 3 = ESC, 2.5 = CNTL + Z, 2 = CTRL + X, 1 = CTRL + C를 의미.
    ESC : 프로그램 종류
    CTRL + Z : 현재 화면을 캡처.
    CTRL + X : 녹화를 시작.
    CTRL + C : 녹화를 중지."""
    if key == 3:
        break

    elif key == 2.5:
        print('캡쳐')
        cv2.imwrite("image/" + str(now) + ".png", frame)

    elif key == 2:
        print("녹화 시작")
        record = True
        video = cv2.VideoWriter("image/" + str(now) + ".avi", fourcc, 20.0, (frame.shape[1], frame.shape[0]))

    elif key == 1:
        print("녹화 중지")
        record = False
        video.release()

    if record == True:
        print("녹화 중..")
        video.write(frame)

# 메모리 할당 해제
cap.release()

# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()