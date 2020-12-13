import cv2
import os
import random
import string
nameofimage = (random.choice(string.ascii_uppercase))

print("Convert jpg to png")

imagepath = input("Enter the Path of Photo e.g:'path/photoname.jng': ")

foldername = 'output'
try:
    os.makedirs(foldername)
except:
    if os.path.exists(foldername):
        new = os.path.join(os.getcwd(), foldername)
        os.chdir(new)
finally:
    imag = cv2.imread(imagepath)
    cv2.imwrite("{}.png".format(nameofimage), imag)
    print("Enter Any Key.....")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#    "D:\Data\Azhar.jpg"