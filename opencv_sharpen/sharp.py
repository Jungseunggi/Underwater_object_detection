import numpy as np
import cv2
from os import sys, listdir

file_list = listdir('/Users/kcoo/Desktop/dataset/data_re/images/val')
print(file_list)
for image in file_list:
    src = cv2.imread(f'/Users/kcoo/Desktop/dataset/data_re/images/val/{image}')

    if src is None:
        print('Image load failed!')
        sys.exit()
        
    src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb) 

    src_f = src_ycrcb[:, :, 0].astype(np.float32)
    blr = cv2.GaussianBlur(src_f, (0, 0), 2.0)
    src_ycrcb[:, :, 0] = np.clip(2. * src_f - blr, 0, 255).astype(np.uint8)

    dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)


    cv2.imwrite(f'/Users/kcoo/Desktop/dataset/data_re_sharp/images/val/{image}.jpg', dst)