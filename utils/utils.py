import os

import cv2
import numpy as np
from PIL import Image

from utils.blocks import Block


def make_blocks(pix2quad):
    pathin = os.getcwd()+'\\examples\\images\\'
    pathout = os.getcwd()+'\\examples\\blocks\\'
    blocks = []
    for filename in os.listdir(pathin):
        image = Image.open(pathin + filename)
        image = image.resize((pix2quad, pix2quad))
        blocks.append(Block(image))
        image.save(pathout+filename, "JPEG")
    return blocks


def choose_quad(blocks, qimage):
    qimg_means = np.array([np.mean(qimage[:, :, 0]), np.mean(qimage[:, :, 1]), np.mean(qimage[:, :, 2])])
    ibest = 0
    resbest = np.inf
    for i, el in enumerate(blocks):
        dist = np.sqrt(np.sum(np.abs(qimg_means - el.bl_means) ** 2))
        if dist < resbest:
            resbest = dist
            ibest = i
    return blocks[ibest].image

# do your stuff


def get_diff(img1, img2):
    colordiff = cv2.absdiff(img1, img2)
    graydiff = cv2.cvtColor(colordiff, cv2.COLOR_BGR2GRAY)
    return colordiff, graydiff