from PIL import Image, ImageColor, ImageOps

# First Step - Insert Picture or will be done automatically
a = input("Insert Photo, photo path You wish to Edit \n Insert/Paste Here: ")
try:
    request.urlretrieve(
    a, "rework.png")
    image = Image.open("rework.png")
    print("Picture was insert")
    image_uploaded = True
