class Quadrants:
    def __init__(self, image, qshape, pix2quad=5):
        self.image = image
        self.pix2quad = pix2quad
        self.qshape = qshape
        self.imageor = image.copy()

    def set_quad(self, x, y, image):
        x_left, y_up, x_right, y_down = self.get_bounds(x, y, 1, 1)

        if x_right - x_left != self.pix2quad \
                or y_down - y_up != self.pix2quad:
            image = image[:y_down - y_up:, :x_right - x_left:]
        self.image[y_up:y_down, x_left:x_right] = image

    def get_bounds(self, x, y, valx, valy):
        if (x > self.qshape[1]):
            x = self.qshape[1] - valx

        if (y > self.qshape[0]):
            y = self.qshape[0] - valy

        x_left = (x) * self.pix2quad
        y_up = (y) * self.pix2quad
        x_right = (x + valx) * self.pix2quad
        y_down = (y + valy) * self.pix2quad
        if (x_right > self.image.shape[1]):
            x_right = self.image.shape[1] - 1
        if (y_down > self.image.shape[0]):
            y_down = self.image.shape[0] - 1

        return x_left, y_up, x_right, y_down
