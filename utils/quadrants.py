import cv2
import numpy as np


class Quadrants:
    def __init__(self, image, pix2quad=5, imageor=None):
        self.image = np.array(image)
        self.pix2quad = pix2quad
        width = self.image.shape[0]
        height = self.image.shape[1]
        bufx = (width // self.pix2quad) + (1 if width % self.pix2quad != 0 else 0)
        bufy = height // self.pix2quad + (1 if height % self.pix2quad != 0 else 0)
        self.qshape = (bufx, bufy)
        self.integral = np.zeros((height + 1, width + 1, 3))
        self.integral = cv2.integral(self.image, self.integral, -1)
        if not(imageor is None):
            self.imageor = np.array(imageor)
            self.integralr = np.zeros((height+1, width+1,3))
            self.integralr = cv2.integral(self.imageor[:,:,0], self.integralr, -1)
            self.integralg = np.zeros((height+1, width+1,3))
            self.integralg = cv2.integral(self.imageor[:,:,1], self.integralg, -1)
            self.integralb = np.zeros((height+1, width+1,3))
            self.integralb = cv2.integral(self.imageor[:,:,2], self.integralb, -1)

    def get_bright(self, xq, yq, ch=0):
        ch_integral = []
        if ch == 0:
            ch_integral = self.integral
        elif ch == 1:
            ch_integral = self.integralr
        elif ch == 2:
            ch_integral = self.integralg
        elif ch == 3:
            ch_integral = self.integralb
        x1, y1, x2, y2 = self.get_bounds(xq,yq,1,1)
        return ch_integral[y2, x2] - ch_integral[y1, x2] - ch_integral[y2, x1] + ch_integral[y1, x1]

    def get_quad(self, x, y, orig=False):
        x_left, y_up, x_right, y_down = self.get_bounds(x, y, 1, 1)
        if orig:
            return self.imageor[y_up:y_down, x_left:x_right]
        else:
            return self.image[y_up:y_down, x_left:x_right]

    def set_quad(self, x, y, image):
        x_left, y_up, x_right, y_down = self.get_bounds(x, y, 1, 1)

        if x_right - x_left != self.pix2quad\
                or y_down - y_up != self.pix2quad:
            image = image[:y_down - y_up:,:x_right - x_left:]
        self.image[y_up:y_down, x_left:x_right] = image

    def get_bounds(self, x, y, valx, valy):
        if(x > self.qshape[1]):
            x = self.qshape[1] - valx

        if(y > self.qshape[0]):
            y = self.qshape[0] - valy

        x_left = (x)* self.pix2quad
        y_up = (y)* self.pix2quad
        x_right = (x + valx)* self.pix2quad
        y_down = (y + valy) * self.pix2quad
        if (x_right > self.image.shape[1]):
            x_right = self.image.shape[1]-1
        if (y_down > self.image.shape[0]):
            y_down = self.image.shape[0] - 1

        return x_left, y_up, x_right, y_down
