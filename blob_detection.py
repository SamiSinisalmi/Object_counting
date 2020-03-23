import cv2
import numpy as np

def count_blobs(image):
    print('counting blobs ...')
    
    #image = cv2.imread('color_threshold_images/suburb_red_and_blue')
    detector = cv2.SimpleBlobDetector()
    keypoints = detector.detect(image)
    
    image_with_keypoints = cv2.drawKeypoints(image,
                                          keypoints,
                                          np.array([]),
                                          (0,0,255),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('keypoints', image_with_keypoints)
    cv2.waitKey(0)
    