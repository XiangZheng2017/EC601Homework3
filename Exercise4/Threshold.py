#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 18:34:20 2017

@author: xiangzheng
"""

import cv2

img=cv2.imread('Test_images/baboon.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

[cv,thr]=cv2.threshold(gray,128,255,2)
cv2.imshow('Threshold',thr)
cv2.imwrite('Threshold image.jpg',thr)

[cv,bi_thr]=cv2.threshold(gray,128,255,cv2.THRESH_BINARY)
cv2.imshow('Binary Threshold',bi_thr)
cv2.imwrite('Binary Threshold image.jpg',bi_thr)

[cv,thr1]=cv2.threshold(gray,27,255,cv2.THRESH_BINARY)
[cv,thr2]=cv2.threshold(gray,125,255,cv2.THRESH_BINARY_INV)
band_thr=cv2.bitwise_and(thr1,thr2)
cv2.imshow('Band Threshold',band_thr)
cv2.imwrite('Band Threshold.jpg',band_thr)

[cv,thr3]=cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
semi_thr=cv2.bitwise_and(gray,thr3)
cv2.imshow('Semi Threshold',semi_thr)
cv2.imwrite('Semi Threshold.jpg',semi_thr)

thr4=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,10)
cv2.imshow('Adaptive Threshold',thr4)
cv2.imwrite('Adaptive Threshold.jpg',thr4)

cv2.waitKey(0)
