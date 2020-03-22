import numpy as np

def color_transform(image):
    print('processing colors ...')
    
    threshold_red = image[:,:,0] > 0.7
    threshold_green = image[:,:,1] > 0.5
    threshold_blue = image[:,:,2] > 0.6
    
    ''' Pick either green or red and blue '''
    #threshold = threshold_green
    threshold = np.logical_or(threshold_red, threshold_blue)
    
    image[:,:,0] = threshold
    image[:,:,1] = threshold
    image[:,:,2] = threshold
    
    return image
    