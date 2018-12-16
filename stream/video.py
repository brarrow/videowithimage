import cv2

from utils.quadrants import Quadrants
from utils.utils import choose_quad


def choose_quads(qimage, blocks):
    cen = blocks[0].cen
    p2q = qimage.pix2quad
    xmult = cen
    ymult = cen
    for x in range(qimage.qshape[1]):
        for y in range(qimage.qshape[0]):
            image = choose_quad(blocks, qimage.imageor[ymult, xmult])
            ymult += p2q
            qimage.set_quad(x, y, image)
        ymult = cen
        xmult += p2q
    return qimage


def init_stream(pix2quad, blocks):
    vid_inp = cv2.VideoCapture('examples/videos/sample.mp4')
    # vid_inp = cv2.VideoCapture(0)
    # fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    # vid_out = cv2.VideoWriter('examples/results/out.avi', fourcc, int(vid_inp.get(cv2.CAP_PROP_FPS))
    #                           ,
    #                           (int(vid_inp.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vid_inp.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    width = vid_inp.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = vid_inp.get(cv2.CAP_PROP_FRAME_HEIGHT)
    bufx = (width // pix2quad) + (1 if width % pix2quad != 0 else 0)
    bufy = height // pix2quad + (1 if height % pix2quad != 0 else 0)
    qshape = (int(bufy), int(bufx))
    while (vid_inp.isOpened()):
        ret, frame2 = vid_inp.read()
        frame2 = frame2[:, ::-1, :]
        if (ret):
            # frame2 = cv2.resize(frame2, dsize=(1920, 1080), interpolation=cv2.INTER_CUBIC)
            qres2 = Quadrants(frame2, qshape, pix2quad)
            choose_quads(qres2, blocks)
            res = qres2.image

            cv2.imshow('res', res)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # vid_out.release()
    vid_inp.release()
    cv2.destroyAllWindows()
