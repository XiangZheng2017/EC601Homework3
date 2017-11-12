import numpy as np
import cv2

def TemplateMatching(src, temp, stepsize): # src: source image, temp: template image, stepsize: the step size for sliding the template
    mean_t = 0;
    var_t = 0;
    location = [0, 0];
    # Calculate the mean and variance of template pixel values
    # ------------------ Put your code below ------------------ 
    for i in range(0,temp.shape[0]):
        for j in range(0,temp.shape[1]):
            mean_t=temp[i,j]+mean_t
    mean_t=mean_t/(temp.shape[0]*temp.shape[1])
    
    for i in range(0,temp.shape[0]):
        for j in range(0,temp.shape[1]):
            var_t=(temp[i,j]-mean_t)**2+var_t
    var_t=var_t/(temp.shape[0]*temp.shape[1])
            
    
    max_corr = 0;
    # Slide window in source image and find the maximum correlation
    for i in np.arange(0, src.shape[0] - temp.shape[0], stepsize):
        for j in np.arange(0, src.shape[1] - temp.shape[1], stepsize):
            mean_s = 0;
            var_s = 0;
            corr = 0;
            sum = 0;
            # Calculate the mean and variance of source image pixel values inside window
            # ------------------ Put your code below ------------------ 
            for ii in range(0,temp.shape[0]):
                for jj in range(0,temp.shape[1]):
                    mean_s=src[ii+i,jj+j]+mean_s
            mean_s=mean_s/(src.shape[0]*src.shape[1])
            
            for ii in range(0,temp.shape[0]):
                for jj in range(0,temp.shape[1]):
                    var_s=(src[ii+i,jj+j]-mean_s)**2+var_s
            var_s=var_s/(src.shape[0]*src.shape[1])
            
                 
            # Calculate normalized correlation coefficient (NCC) between source and template
            # ------------------ Put your code below ------------------ 
            for k in range(0,temp.shape[0]):
                for l in range(0,temp.shape[1]):
                    corr=(temp[k,l]-mean_t)*(src[k+i,l+j]-mean_s)+corr
            corr=corr/(var_t*var_s*temp.size)
            
            
            
            if corr > max_corr:
                max_corr = corr;
                location = [i, j];
    return location

# load source and template images

source_img = cv2.imread('source_img.jpg',0) # read image in grayscale
temp = cv2.imread('template_img.jpg',0) # read image in grayscale
location = TemplateMatching(source_img, temp, 10);
print(location)
match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)

# Draw a red rectangle on match_img to show the template matching result
# ------------------ Put your code below ------------------
(x, y) = location
(h, w) = temp.shape 
cv2.rectangle(match_img,(x,y),(x+w,y+h),(0,255,0),3)
# Save the template matching result image (match_img)
# ------------------ Put your code below ------------------ 
cv2.imwrite('result.jpg',match_img)

# Display the template image and the matching result
cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
cv2.imshow('TemplateImage', temp)
cv2.imshow('MyTemplateMatching',match_img)

cv2.waitKey(0)
cv2.destroyAllWindows()