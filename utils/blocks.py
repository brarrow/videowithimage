import numpy as np
import cv2
class Block:

    def __init__(self, image):
        self.image = np.array(image)
        self.rsum = np.mean(self.image[:,:,0])
        self.gsum = np.mean(self.image[:, :,1])
        self.bsum = np.mean(self.image[:, :,2])
