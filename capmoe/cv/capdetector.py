# -*- coding: utf-8 -*-
"""
    capmoe.cv.capdetector
    ~~~~~~~~~~~~~~~~~~~~~

    :synopsis: Provides function to detect a beer cap from an image

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules
import time
from os.path import basename

# 3rd party modules
import cv2

# original modules
import capmoe.util.logger


# global variables
logger = capmoe.util.logger.factory(__file__)


def capdetector(imgpath, max_candidates, loglevel='WARNING'):
    """Detect circles from an image
    """
    logger.setLevel(loglevel)

    im = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)
    im_height, im_width = im.shape[0:2]
    logger.debug('%s: size=(%d,%d)' % (basename(imgpath), im_width, im_height))

    im = cv2.GaussianBlur(im, ksize=(5, 5), sigmaX=0)

    # circles => [(x, y, r), ...] ; left one is most voted
    t0 = time.time()
    circles = cv2.HoughCircles(
        im, cv2.cv.CV_HOUGH_GRADIENT,
        dp=1,
        minDist=1,
        param1=85, param2=40,
        minRadius=int(min(im_width, im_height) * 0.2),
        maxRadius=int(min(im_width, im_height) * 0.6))
    t1 = time.time()
    logger.debug('cv2.HoughCircles(): %d circles detected in %f sec' %
                 (circles.size, t1 - t0))

    # filter beer cap candidates from circles (at most `max_caididates`)
    center_x, center_y = (im_width / 2, im_height / 2)
    near_center_r = min(im_width, im_height) * 0.2
    caps = []
    t0 = time.time()
    for x, y, r in circles[0, :]:
        # only see near-center circle
        if (x - center_x) ** 2 + (y - center_y) ** 2 > near_center_r ** 2:
            continue

        caps.append({'x': int(x), 'y': int(y), 'r': int(r)})
        if len(caps) >= max_candidates:
            break
    t1 = time.time()
    logger.debug('finding top-%d possible circles: %f sec' %
                 (max_candidates, t1 - t0))

    return caps
