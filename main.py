from read_image import get_image_data
from processing import color_transform
import matplotlib.pyplot as plt

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
    
if __name__ == "__main__":
    main()
