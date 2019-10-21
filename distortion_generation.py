import os
import sys
from skimage.util import random_noise
import random
import cv2
import numpy as np

def motion_blur(image, degree):
    if degree != 0:
        angle = random.randint(1,360)
        M = cv2.getRotationMatrix2D((degree / 2, degree / 2), angle, 1)
        motion_blur_kernel = np.diag(np.ones(degree))
        motion_blur_kernel = cv2.warpAffine(motion_blur_kernel, M, (degree, degree))

        motion_blur_kernel = motion_blur_kernel / degree
        blurred = cv2.filter2D(image, -1, motion_blur_kernel)
        cv2.normalize(blurred, blurred, 0, 255, cv2.NORM_MINMAX)
        blurred = np.array(blurred, dtype=np.uint8)
    else: 
        blurred = image
    if blurred.mean()>1:
    	blurred = blurred/255
    return blurred

def gaussion_noise(image,degree):
    image = random_noise(image, mode="gaussian", var = degree)
    if image.mean()>1:
        image/255
    return image

def gaussion_blur(image,degree):
    if degree!=0:
        image = cv2.GaussianBlur(image,(degree,degree),0)
    if image.mean()>1:
        image = image/255
    return image



def gci(filepath): 
    files = os.listdir(filepath)  
    for fi in files:    
        fi_d = os.path.join(filepath,fi)    
        if os.path.isdir(fi_d):
            # print(fi_d)
            folder = os.path.exists(os.path.join(sys.argv[2]+"-"+sys.argv[3]+fi_d))
            if not folder:
              os.makedirs(os.path.join(sys.argv[2]+"-"+sys.argv[3]+fi_d))
            gci(fi_d)    
        else:      
            print(os.path.join(fi_d))
            images = cv2.imread(fi_d)
            images = cv2.resize(images,(224,224))
            if sys.argv[2] == 'MB':
              images = motion_blur(images,int(sys.argv[3]))
            elif sys.argv[2] == 'GB':
              images = gaussion_blur(images,int(sys.argv[3]))
            elif sys.argv[2] == 'GN':
              images = gaussion_noise(images,float(sys.argv[3]))
            cv2.imwrite(os.path.join(".\\"+sys.argv[2]+"-"+sys.argv[3]+fi_d[1:]), images*255)
gci(sys.argv[1])

