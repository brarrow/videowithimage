import stream.video as video
from utils.utils import make_blocks

pix2quad = 10
blocks = make_blocks(pix2quad)
video.init_stream(pix2quad, blocks)
