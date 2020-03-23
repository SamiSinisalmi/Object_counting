import os
import cv2

def get_image_data(dir_name):

    print('reading images ...')
    
    files = os.listdir(dir_name)
    
    image_data = []
    for file in files:
        data = cv2.imread(dir_name + file)
        image_data.append(data)
    
    return image_data