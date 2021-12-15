import os
import sys

import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
pygame.display.set_caption('myPicture')


def load_image(name, color_key=None):
    full_name = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(full_name):
        raise FileNotFoundError(f"Файл с изображением '{full_name}' не найден")
    image = pygame.image.load(full_name)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


running = True
owl = load_image('sinjiIcari.jpg')
screen.blit(owl, (0, 0, owl.get_width(), owl.get_height()))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
