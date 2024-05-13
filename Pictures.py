from PIL import Image, ImageOps
import os
import shutil


def changeFiles(directory, file):
    image = Image.open(directory)
    image = ImageOps.grayscale(image)
    image.save(directory)


def fileSearch():
    for root, dirs, files in os.walk(input()):
        for file in files:
            if file.endswith('.png'):
                changeFiles(os.path.join(root, file), file)


fileSearch()
