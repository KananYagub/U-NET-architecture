import os, shutil
import cv2

or_dir = 'Data/Test_data/Images/' #original directory for images
le = len(os.listdir(or_dir)) 
li = os.listdir(or_dir)

number = 0
for el in li:
    name = el.split(".")
    image_name = 'Data/Test_data/Images/' + el
    image = cv2.imread(image_name)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    saved_image_name = 'Data/Test_data/Gray scaled Images/' + str(number) + '.png'
    cv2.imwrite(saved_image_name,gray)
    number = number+ 1

