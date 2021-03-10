##################################################
# Awful program created by Andrew M Evans
# email: evansa@sonoma.edu
#
# Created date: Tues August 5th 3:30:21 PDT 2020
#
# This code creates .gifs from the ./Images folder
# This version is built for Linux file systems
##################################################
import sys
from os import listdir
from PIL import Image
def gifCreate(useri, total, name):
    if useri[0].lower() == "y":
        images = []
        im = ""
        for i in sorted(listdir("./Images")):
            if i[:-4] != str(name):
                im = Image.open("./Images"+"/"+i)
                images.append(im)
        images[0].save("./Images"+"/"+'Output.gif',save_all=True, append_images=images[1:], optimize=True, duration=total, loop=0)

