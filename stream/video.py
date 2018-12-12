import cv2
from utils.utils import get_diff
from utils.quadrants import Quadrants
import numpy as np
from PIL import Image

def skip_frames(cap, count):
    for i in range(count):
        cap.grab()


def all_quads(qimage, qimage2):
    res = np.array(Image.open("examples/blocks/1.jpg"))
    for x in range(qimage.qshape[1]):
        for y in range(qimage.qshape[0]):
            if np.sum(qimage.get_quad(x, y)) > 4000:
                qimage2.set_quad(x,y, res)
    return qimage2


def choose_block(image=None):

    return


def init_stream():
    vid_inp = cv2.VideoCapture('examples/videos/2.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    vid_out = cv2.VideoWriter('examples/results/out.avi', fourcc, int(vid_inp.get(cv2.CAP_PROP_FPS)//2)
                              ,(int(vid_inp.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vid_inp.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    ret, frame1 = vid_inp.read()
    while (vid_inp.isOpened()):
        ret, frame2 = vid_inp.read()
        if(ret):
            gray = get_diff(frame1, frame2)
            qres = Quadrants(gray,10)
            qres2 = Quadrants(frame2, 10)

            qres = all_quads(qres, qres2)
            cv2.imshow('res', qres.image)
            frame1 = frame2
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    vid_out.release()
    vid_inp.release()
    cv2.destroyAllWindows()