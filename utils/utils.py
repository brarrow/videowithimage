import cv2
import numpy as np
from PIL import Image
from utils.blocks import Block
import os
import random


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

def choose_quad(blocks, quadorig):
    blocks_size = len(blocks)
    return blocks[random.randint(0,blocks_size-1)].image

# do your stuff


def get_diff(img1, img2):
    colordiff = cv2.absdiff(img1, img2)
    graydiff = cv2.cvtColor(colordiff, cv2.COLOR_BGR2GRAY)
    return colordiff, graydiff