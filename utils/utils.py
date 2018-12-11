import cv2
import numpy as np
from filters.filters import blur, dilatate, erode


def get_diff(img1, img2, th=20):
    img1buf = img1.copy()
    img2buf = img2.copy()

    img1buf = blur(img1buf, 10)
    img2buf = blur(img2buf, 10)

    img1buf = erode(img1buf, 10, 5)
    img2buf = erode(img2buf, 10, 5)

    diff = cv2.absdiff(img1buf, img2buf)
    diff = dilatate(diff, 5, 3)
    mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    imask = mask > th

    canvas = np.zeros_like(img2, np.uint8)
    canvas[imask] = img2[imask]

    return canvas