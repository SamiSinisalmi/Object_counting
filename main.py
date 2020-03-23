from read_image import get_image_data
from processing import color_transform
from blob_detection import count_blobs
import matplotlib.pyplot as plt

import cv2
import numpy as np

DIRECTORY_NAME = 'images/'

def main():
    image_data = get_image_data(DIRECTORY_NAME)
    
    test_image = image_data[2]
    
    plt.figure(1, figsize=(150,150))
    plt.subplot(211)
    plt.imshow(test_image)
    plt.axis('off')
    
    processed_image = color_transform(test_image)
    
    plt.subplot(212)
    plt.imshow(processed_image)
    plt.axis('off')
    
    plt.show()
    
    blobs = count_blobs(processed_image)
    
if __name__ == "__main__":
    main()
