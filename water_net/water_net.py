import torch
import cv2
import matplotlib.pyplot as plt
import glob
from PIL import Image
from numpy import asarray
import os

from scipy.signal import convolve2d
import numpy as np

# %matplotlib inline

preprocess, postprocess, model = torch.hub.load('tnwei/waternet', 'waternet')

# 워터넷
def water_net(path):
  # 경로설정
  os.chdir(path)
  files = os.listdir(path)
  print(os.getcwd())

  # 폴더 생성
  if not os.path.isdir('C:/Users/Jung/codestates/cp2_project/test_re'):
    os.mkdir('C:/Users/Jung/codestates/cp2_project/test_re')

  # 경로내 jpg파일만 추출
  for image in files:
    if image.endswith(".jpg"):
      print(image)
      
      # 이미지 사이즈
      img = Image.open(image)
      img_size = img.size

      # water_net 적용
      # im = cv2.imread(image)
      # rgb_im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
      # rgb_im = cv2.resize(rgb_im, (img_size))
      # rgb_ten, wb_ten, he_ten, gc_ten = preprocess(rgb_im)
      # out_ten = model(rgb_ten, wb_ten, he_ten, gc_ten)
      # out_im = postprocess(out_ten)
      # result = Image.fromarray(out_im[0])

      # 가끔 에러가 파일들은 건너띄고 적용
      try:
        im = cv2.imread(image)
        rgb_im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        rgb_im = cv2.resize(rgb_im, (img_size))
        rgb_ten, wb_ten, he_ten, gc_ten = preprocess(rgb_im)
        out_ten = model(rgb_ten, wb_ten, he_ten, gc_ten)
        out_im = postprocess(out_ten)
        result = Image.fromarray(out_im[0])
      except ValueError:
        pass
      
      #  저장
      result.save("C:/Users/Jung/codestates/cp2_project/test_re/"+f"{image}")
      

  return




# def rgb_convolve2d(image, kernel):
#     red = convolve2d(image[:,:,0], kernel, 'valid')
#     green = convolve2d(image[:,:,1], kernel, 'valid')
#     blue = convolve2d(image[:,:,2], kernel, 'valid')
#     return np.stack([red, green, blue], axis=2)

# def Enhancement():
#     kernel = np.array([[-1, -1, -1, -1, -1],
#                     [-1, -1, -1, -1, -1],
#                     [-1, -1, 25, -1, -1],
#                     [-1, -1, -1, -1, -1],
#                     [-1, -1, -1, -1, -1]])

#     conv_im1 = (rgb_convolve2d(traffic, kernel[::-1, ::-1])
#                             .clip(0,255)
#                             .astype(np.uint8))


if __name__ == '__main__':
    water_net('C:/Users/Jung/codestates/cp2_project/test')
    
    