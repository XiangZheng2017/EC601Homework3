## Exercise 2

**1. ColorImage.cpp is a program that takes a look at colorspace conversions in OpenCV. Run the code in ColorImage.cpp and comment on the outputs. Implement the same thing in Python and save each image.**

Comments: The outputs of ColorImage.cpp are different color representation of Lenna image. The file display 3 different channels of RGB, YUV, HSL and LAB colorspcae seperately.
Python script and results are stored in exercise2 folder.



**2. Print out the values of the pixel at (20,25) in the RGB, YCbCr and HSV versions of the image. What are the ranges of pixel values in each channel of each of the above mentioned colorspaces?**

RGB:print(lenna[20,25]): [106 122 225]

HSV:print(hsv_lenna[20,25]):[  4 135 225]

YCC:print(YCC_lenna[20,25]):[151 181 103]

The ranges of pixel values in each channel is from 0 to 225.

