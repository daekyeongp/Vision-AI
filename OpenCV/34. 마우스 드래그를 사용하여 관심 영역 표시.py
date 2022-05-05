import cv2


isDragging = False                                  # 마우스 드래그 상태 저장
x0, y0, w, h = -1, -1, -1, -1                       # 영역 선택 좌표 저장
blue, red = (255, 0, 0), (0, 0, 255)                # 색상 값


def mouse_drag(event, x, y, flag, param):           # 마우스 이벤트 함수
    global isDragging, x0, y0, img                  # 전역 변수 참조
    if event == cv2.EVENT_LBUTTONDOWN:              # 왼쪽 마우스 버튼 다운 (드래그 시작)
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv2.EVENT_MOUSEMOVE:              # 마우스 움직임 인식
        if isDragging:                              # 드래그 진행 중
            img_draw = img.copy()                   # 사각형 그림 표현을 위한 이미지 복제
            cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2)  # 드래그 진행 영역 표시
            cv2.imshow('img', img_draw)             # 사각형 표시된 그림 화면 출력
    elif event == cv2.EVENT_LBUTTONUP:              # 왼쪽 마우스 버튼 업 ---④
        if isDragging:                              # 드래그 중지
            isDragging = False                      # 드래그 판단 변수 False 변환
            w = x - x0                              # 드래그 영역 폭 계산
            h = y - y0                              # 드래그 영역 높이 계산
            print("x:%d, y:%d, w:%d, h:%d" % (x0, y0, w, h))
            if w > 0 and h > 0:                     # 폭과 높이가 0 보다 크면 드래그 방향이 정상
                img_draw = img.copy()               # 선택 영역에 사각형 그림을 표시할 이미지 복제
                # 선택 영역에 빨간 사각형 표시
                cv2.rectangle(img_draw, (x0, y0), (x, y), red, 2)
                cv2.imshow('img', img_draw)         # 빨간 사각형 그려진 이미지 화면 출력
                roi = img[y0:y0+h, x0:x0+w]         # 원본 이미지에서 선택 영영만 ROI로 지정
                cv2.imshow('cropped', roi)          # ROI 지정 영역을 새 창으로 이미지 출력
                cv2.moveWindow('cropped', 0, 0)     # 새 창을 화면 좌측 상단에 이동
                cv2.imwrite('image/' + roi + '.jpg', roi)   # ROI 영역만 파일로 저장
                print("croped.")
            else:
                cv2.imshow('img', img)              # 드래그 방향이 잘못된 경우 영역 표시 X
                print("좌측 상단에서 우측 하단으로 영역을 드래그 하시오.")


img = cv2.imread('image/33.jpg')

cv2.imshow('img', img)                   # 이미지 출력 함수
cv2.setMouseCallback('img', mouse_drag)  # 마우스 이벤트 등록
cv2.waitKey(0)                           # 키 입력 대기 함수
cv2.destroyAllWindows()                  # 모든 윈도우 창 닫기 함수