import numpy as np


class Block:

    def __init__(self, image, dop):
        self.image = np.array(image)[:, :, ::-1]
        self.cen = (len(self.image) - 1) // 2
        self.bl_means = np.array(
            [int(np.mean(self.image[:, :, 0])) // dop, int(np.mean(self.image[:, :, 1])) // dop,
             int(np.mean(self.image[:, :, 2])) // dop])
