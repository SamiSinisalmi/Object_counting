import numpy as np
import cv2

def color_transform(image):
    print('processing colors ...')
    
    threshold_red = image[:,:,0] > 179
    threshold_green = image[:,:,1] > 128
    threshold_blue = image[:,:,2] > 153
    
    ''' Pick either green or red and blue '''
    #threshold = threshold_green
    threshold = np.logical_or(threshold_red, threshold_blue)
    
    image[:,:,0] = threshold
    image[:,:,1] = threshold
    image[:,:,2] = threshold
    image = image*255
    
    return image

def median_filter(image):
    print('applying a median filter ...')
    
    median_image = cv2.medianBlur(image, 7)
    
    return median_image
    