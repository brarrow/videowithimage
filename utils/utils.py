import cv2
import numpy as np
from filters.filters import blur, dilatate, erode


def get_diff(img1, img2, th=20):
    img1buf = img1.copy()
    img2buf = img2.copy()


    diff = cv2.absdiff(img1buf, img2buf)
    mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    #
    # imask = mask > th
    #
    # canvas = np.zeros_like(img2, np.uint8)
    # canvas[imask] = img2[imask]

    return mask