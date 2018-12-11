import cv2
from utils.utils import get_diff


def skip_frames(cap, count):
    for i in range(count):
        cap.grab()

def init_stream():
    vid_inp = cv2.VideoCapture('examples/videos/1.avi')
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    vid_out = cv2.VideoWriter('examples/results/out.avi', fourcc, int(vid_inp.get(cv2.CAP_PROP_FPS)//2)
                              ,(int(vid_inp.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vid_inp.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    ret, frame1 = vid_inp.read()
    while (vid_inp.isOpened()):
        skip_frames(vid_inp, 1)
        ret, frame2 = vid_inp.read()
        if(ret):
            result = get_diff(frame1, frame2)
            vid_out.write(result)
            cv2.imshow('res', result)
            frame1 = frame2
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    vid_out.release()
    vid_inp.release()
    cv2.destroyAllWindows()