import cv2
from utils.utils import get_diff, choose_quad
from utils.quadrants import Quadrants
import numpy as np
from PIL import Image

def skip_frames(cap, count):
    for i in range(count):
        cap.grab()


def all_quads(qimage, qimage2, blocks):
    for x in range(qimage.qshape[1]):
        for y in range(qimage.qshape[0]):
            if qimage.get_bright(x,y) > 1000:
                image = choose_quad(blocks, qimage2)
                qimage2.set_quad(x,y, image)
    return qimage2


def choose_block(image=None):

    return


def init_stream(pix2quad, blocks):
    vid_inp = cv2.VideoCapture('examples/videos/sample.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    vid_out = cv2.VideoWriter('examples/results/out.avi', fourcc, int(vid_inp.get(cv2.CAP_PROP_FPS))
                              ,(int(vid_inp.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vid_inp.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    ret, frame1 = vid_inp.read()
    res = frame1
    while (vid_inp.isOpened()):
        ret, frame2 = vid_inp.read()

        if(ret):
            colordiff, graydiff = get_diff(frame1, frame2)
            qres = Quadrants(graydiff, pix2quad)
            qres2 = Quadrants(res, pix2quad, colordiff)
            all_quads(qres, qres2, blocks)
            res = qres2.image.copy()
            cv2.imshow('res', res)
            frame1 = frame2.copy()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    vid_out.release()
    vid_inp.release()
    cv2.destroyAllWindows()