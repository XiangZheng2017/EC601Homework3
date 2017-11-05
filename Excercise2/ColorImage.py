#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 16:14:34 2017

@author: xiangzheng
"""


import cv2

lenna = cv2.imread('Test_images/Lenna.png') #load Lenna image

b,g,r = cv2.split(lenna) #split into color channels
#print(b)
#cv2.imwrite('Test_images/Lenna.png')
cv2.imshow('Blue',b)
cv2.imwrite('Blue.png',b)
cv2.imshow('Red',r)
cv2.imwrite('Red.png',r)
cv2.imshow('Green',g)
cv2.imwrite('Green.png',g)
print(lenna[20,25])

hsv_lenna = cv2.cvtColor(lenna, cv2.COLOR_BGR2HSV) #convert to HSV

h,s,v = cv2.split(hsv_lenna) 

cv2.imshow('Hue',h)
cv2.imwrite('Hue.png',h)
cv2.imshow('Saturation',s)
cv2.imwrite('Saturation.png',s)
cv2.imshow('Value',v)
cv2.imwrite('Value.png',v)
print(hsv_lenna[20,25])

YCC_lenna = cv2.cvtColor(lenna, cv2.COLOR_BGR2YCR_CB) #convert to YCrCb

y,Cb,Cr = cv2.split(YCC_lenna) 

cv2.imshow('Y',y)
cv2.imwrite('Y.png',y)
cv2.imshow('Cb',Cb)
cv2.imwrite('Cb.png',Cb)
cv2.imshow('Cr',Cr)
cv2.imwrite('Cr.png',Cr)
print(YCC_lenna[20,25])


LAB_lenna = cv2.cvtColor(lenna, cv2.COLOR_BGR2LAB) #convert to LAB

L,A,B = cv2.split(LAB_lenna) 

cv2.imshow('Y',y)
cv2.imwrite('L.png',L)
cv2.imshow('Cb',Cb)
cv2.imwrite('A.png',A)
cv2.imshow('Cr',Cr)
cv2.imwrite('B.png',B)
print(LAB_lenna[20,25])

cv2.waitKey(0)