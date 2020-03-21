import os
import matplotlib.image as img
import matplotlib.pyplot as plt

def get_image_data(dir_name):

    files = os.listdir(dir_name)
    
    i = 0
    image_data = []
    for file in files:
        data = img.imread(dir_name + file)
        
        plt.imshow(data)
        plt.axis('off')
        plt.show(i)
        
        i += 1
        
        image_data.append(data)
    
    return image_data