import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg) #open file
    images.append(image) #add to array

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0 #save all frames, append next image to this image, duration set, loop infinitely
)
