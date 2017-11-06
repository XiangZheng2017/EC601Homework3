## Exercise 2

**1.Look at Threshold.cpp and implement the code in Python, and observe the results for different threshold values. Comment on the results.**

Comment: Different threshold methods generate different result. The output of semi-threshold is not as good as the rest of three.

**2.What are the disadvantages of binary threshold?**

Limited application: as the representation is only a silhouette, application is restricted to tasks where internal detail is not required as a distinguishing characteristic.
Does not extend to 3D: the 3D nature of objects can rarely be represented by silhouettes. (The 3D equivalent of binary processing uses voxels, spatial occupancy of small cubes in 3D space).
Specialised lighting is required for silhouettes: it is difficult to obtain reliable binary images without restricting the environment. The simplest example is an overhead projector or light box.

**3.When is Adaptive Threshold useful?**

Image thresholding is a simple, yet effective, way of partitioning an image into a foreground and background. This image analysis technique is a type of image segmentation that isolates objects by converting grayscale images into binary images.




