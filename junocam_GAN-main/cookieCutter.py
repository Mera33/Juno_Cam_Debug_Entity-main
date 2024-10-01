
import os
import numpy as np
from constants import *
from architecture import *
import imageio

# first, raw images:
for imgName in os.listdir('raw_imgs/'):
    img = imageio.imread('raw_imgs/'+imgName, pilmode='RGB')
    for i in range(0, img.shape[0]-image_size, image_size):
        for j in range(0, img.shape[1]-image_size, image_size):
            cut_img = img[i:i+image_size, j:j+image_size]
            if np.mean(cut_img) > 1:
                imageio.imwrite('cookiecut_raw_imgs/'+imgName+'_'+str(i)+'_'+str(j)+'.png', cut_img)


for imgName in os.listdir('user_imgs/'):
    img = imageio.imread('user_imgs/'+imgName, pilmode='RGB')
    for i in range(0, img.shape[0]-image_size, image_size):
        for j in range(0, img.shape[1]-image_size, image_size):
            cut_img = img[i:i+image_size, j:j+image_size]
            if np.mean(cut_img) > 1:
                imageio.imwrite('cookiecut_user_imgs/'+imgName+'_'+str(i)+'_'+str(j)+'.png', cut_img)
