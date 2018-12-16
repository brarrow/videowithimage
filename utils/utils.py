import os

import numpy as np
from PIL import Image

from utils.blocks import Block

dop = 5
sized = 256 // dop + 1
bestbuf = np.zeros((sized, sized, sized), int)


def make_blocks(pix2quad):
    pathin = os.getcwd() + '/examples/images/'
    pathout = os.getcwd() + '/examples/blocks/'
    blocks = []
    for filename in os.listdir(pathin):
        try:
            image = Image.open(pathout + str(pix2quad) + filename)
            blocks.append(Block(image, dop))
        except:
            image = Image.open(pathin + filename)
            image = image.resize((pix2quad, pix2quad))
            blocks.append(Block(image, dop))
            image.save(pathout + str(pix2quad) + filename, "JPEG")

    calculate_best(blocks)
    return blocks


def choose_quad(blocks, qimage):
    posn = qimage // dop
    return blocks[bestbuf[posn[0], posn[1], posn[2]] - 1].image


def calculate_best(blocks):
    try:
        global bestbuf
        pathin = os.getcwd() + '/utils/' + str(dop) + 'values.txt'
        file = open(pathin, "r")
        for i in range(sized):
            for j in range(sized):
                for k in range(sized):
                    bestbuf[i, j, k] = int(file.readline())

    except:
        res = np.zeros((sized, sized, sized), int)
        pathin = os.getcwd() + '/utils/' + str(dop) + 'values.txt'
        file = open(pathin, "w")
        for i in range(sized):
            for j in range(sized):
                for k in range(sized):
                    qimg_means = np.array([i, j, k])
                    resbest = np.inf
                    for num, el in enumerate(blocks):
                        # dist = np.sum((qimg_means - el.bl_means) ** 2)
                        dist = np.sum(abs(qimg_means - el.bl_means))
                        if dist < resbest:
                            resbest = dist
                            res[i, j, k] = num + 1
                    file.write(str(res[i, j, k]) + '\n')
            print(i)
        file.close()
        bestbuf = res
