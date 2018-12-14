import numpy as np


class Block:

    def __init__(self, image):
        self.image = np.array(image)
        self.bl_means = np.array(
            [np.mean(self.image[:, :, 0]), np.mean(self.image[:, :, 1]), np.mean(self.image[:, :, 2])])
