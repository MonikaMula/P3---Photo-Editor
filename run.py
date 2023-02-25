from PIL import Image, ImageColor, ImageOps
from urllib import request


# First Step - Insert Picture or will be done automatically
a = input("Insert Photo, photo path You wish to Edit \n Insert/Paste Here: ")
try:
    request.urlretrieve(
    a, "rework.png")
    image = Image.open("rework.png")
    print("Picture was insert")
    image_uploaded = True
except:
    image = Image.open('Maxi.jpg')
    print("Picture wasn't insert, automatic upload picture as an example")
    
    
# Image_Cropping
cropping = input('Crop image? \n Yes/No: ')  
if cropping.lower().startswith("y"):
    left_x = input("left: ")
    top_y = input("top: ")
    right_x = input("right: ")
    bottom_y = input("bottom: ")
    
# width, height =.size
try:
    left_x = int(left_x)
    top_y = int(top_y)
    right_x = int(right_x)
    bottom_y = int(bottom_y)
    image_crop = image.crop((left_x, top_y, right_x, bottom_y))
    image = image_crop
except:
    print("Wrong Input")