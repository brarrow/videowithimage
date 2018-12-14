from PIL import Image
from utils.quadrants import Quadrants
from utils.utils import make_blocks
import matplotlib.pyplot as plt
import stream.video as video

pix2quad = 10
blocks = make_blocks(pix2quad)
video.init_stream(pix2quad, blocks)
# image = Image.open('examples/images/1.jpg')
# image = image.resize((10, 10))
# image.save('examples/blocks/1.jpg', "JPEG")
# qimage = Quadrants(image, 10)
# quad = qimage.get_quad(5,4)
# qimage.set_quad(100,100, quad)
# plt.imshow(qimage.image)
# plt.show()