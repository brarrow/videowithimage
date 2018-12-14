import numpy as np
import cv2
class Quadrants:
    def __init__(self, image, pix2quad=5, imageor=None):
        self.image = np.array(image)
        self.pix2quad = pix2quad
        width = self.image.shape[0]
        height = self.image.shape[1]
        bufx = (self.image.shape[0] // self.pix2quad) + (1 if self.image.shape[0] % self.pix2quad != 0 else 0)
        bufy = self.image.shape[1] // self.pix2quad + (1 if self.image.shape[1] % self.pix2quad != 0 else 0)
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

    def get_bright(self, xq, yq):
        x1, y1, x2, y2 = self.get_bounds(xq,yq,1,1)
        return self.integral[y2,x2] - self.integral[y1,x2] - self.integral[y2,x1] + self.integral[y1,x1]

    def get_quad(self, x, y):
        x_left, y_up, x_right, y_down = self.get_bounds(x, y, 1, 1)

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
