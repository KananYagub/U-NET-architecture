!pip install opencv-python
!pip install imutils
import argparse
import imutils
import numpy as np
import cv2
import os, shutil
from PIL import Image
from matplotlib.pyplot import imsave
import matplotlib.pyplot as plt
import imghdr

#Defining data that we are going to use
or_dir = 'Data/case_9_kesz_marc/'  #original directory for images
le = len(os.listdir(or_dir))       #number of elements in the original directory
li = os.listdir(or_dir)            #elements in original directory
li2 = []
for i in li:
    if 'jpg' in  i:
        li2.append(i)
        
nam_num = 0
#This part we deal with files extenstions because they are in the same directory
for i in li2:   #list of original pics
    im_nam = i.split(".")
    nam = im_nam [0]
    for j in li:                    #list of every file in the dir
        im_nam2 = j.split(".")      #main name of file
        if nam in im_nam2[0]:  
            if 'png' in im_nam2:
                im_nam2_num = 0
                for el in li:       #list of every file in the dir 
                    if (im_nam2[0] in el):
                        print(el)
                        img = 'Data/case_9_kesz_marc/' + el 
                        print(type(img))
                        im = cv2.imread(img)
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
                        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)[1]
                        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
                        cnts = imutils.grab_contours(cnts)
                        na = 0 
                        for c in range(0,len(cnts)):
                            cnt = cnts[c]
                            M = cv2.moments(cnt)
                            cx = int(M['m10']/M['m00'])
                            cy = int(M['m01']/M['m00'])
                            imag_jpg = 'Data/case_9_kesz_marc/' + nam +'.jpg'
                            imag_png = 'Data/case_9_kesz_marc/' + im_nam2[0] + '.png'
                            print(type(imag_jpg))
                            print(type(imag_png))
                            image_jpg = cv2.imread(imag_jpg)
                            image_png = cv2.imread(imag_png)
                            y1 = cx-100
                            y2 = cx+100
                            x1 = cy-100
                            x2 = cy+100
                            if x2 > 2000:
                                x2 = 2000
                                x1 = 1800
                            if y2 > 2000:
                                y2 = 2000 
                                y1 = 1800
                            if x1 < 0:
                                x1 = 0
                                x2 = 200
                            if y1 <0:
                                y1 = 0
                                y2 = 200
                        
                            crop_imag_jpg = image_jpg[x1:x2, y1:y2].copy()
                            crop_imag_png = image_png[x1:x2, y1:y2].copy()
                            
                            ima_name_jpg = 'Data/Train data/Labels/'+ nam +str(nam_num)+'_'+str(im_nam2_num)+'_'+str(na)+'.jpg' 
                            ima_name_png = 'Data/Train data/Mask/'+ nam +str(nam_num)+'_'+str(im_nam2_num)+'_'+str(na)+'.png'
                            
                            cv2.imwrite(ima_name_jpg,crop_imag_jpg)
                            cv2.imwrite(ima_name_png,crop_imag_png)
                            na = na +1 
                    im_nam2_num = im_nam2_num + 1
    nam_num = nam_num + 1                     
                            
                            
                            
                            
                            
                            



