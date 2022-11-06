#We have used multiple negative images which are in grayscale and this command is kind of similar to resizing one, like importing and giving input and all.
#The only change here is the command line for grayscale.

# import opencv
import cv2
import os
import glob

inputFolder = 'AnyFolder'
os.mkdir('New Folder')

i=0

for img in glob.glob(inputFolder + "/*.jpg"):  #format of image.. its jpg right now which could be any
    image = cv2.imread(img)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("Nsd/rsm%04i.jpg" %i, gray_image)

    i +=1
    
cv2.destroyAllWindos()
