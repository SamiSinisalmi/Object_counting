import cv2
import numpy as np

def count_blobs(image):
    print('counting blobs ...')
    
    params = cv2.SimpleBlobDetector_Params()
    
    params.filterByColor = True
    params.blobColor = 255
    params.filterByArea = True
    params.minArea = 50
    params.maxArea = 800
    params.filterByInertia = True
    params.minInertiaRatio = 0.1
    params.filterByConvexity = False
    params.filterByCircularity = False
    
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(image)
    
    im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)
    
    blobs = len(keypoints)

    return blobs
    