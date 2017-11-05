# EC601Homework3
## Exercise 1
**1.How does a program read the cvMat object, in particular, what is the order of the pixel structure?**

cvMat is a structure type in Opencv. The program can access the data in cvMat by calling cvmGet(cvMatName,i,j) function, which get element (i,j) in matrix cvMatName. Another approach called directly access is to add a parameter a when create a new matrix (eg. CvMat Ma = cvMat(3, 4, CV_64FC1, a); ), which program reads cvMat object by a[i*4+j]. The order of pixel structure is R-G-B order.
