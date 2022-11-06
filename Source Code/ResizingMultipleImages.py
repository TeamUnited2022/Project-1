import cv2
import glob
import os

inputFolder = 'n' #the folder where all the images are stored to be resized
os.mkdir('neg')  #new folder creation to keep the resized images

i=0

for img in glob.glob(inputFolder + "/*.jpg"):
    image = cv2.imread(img)                     #reading images
    imgResized = cv2.resize(image, (600, 600))  #resizing images
    cv2.imwrite("neg/negative%04i.jpg" %i, imgResized) #writing resized images to new folder and re-naming the images

    i +=1

cv2.destroyAllWindos()
