import pygame
import sys
import os
path = sys.argv[0]
rootpath = os.path.dirname(path) + "\\img\\"
def load_image(name):
    try:
        image = pygame.image.load(rootpath + name)
    except pygame.error:
        print 'Cannot load image:', rootpath + name
        raise SystemExit
    return image