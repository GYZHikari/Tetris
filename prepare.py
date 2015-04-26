import pygame


def load_image(name):
    try:
        image = pygame.image.load(name)
    except pygame.error:
        print 'Cannot load image:', name
        raise SystemExit
    return image