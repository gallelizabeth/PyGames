import os
import random

import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 500, 500
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


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image_boom = load_image("boom.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self, *args):
        # self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(args[0].pos):
            self.image = Bomb.image_boom


all_sprites = pygame.sprite.Group()

for _ in range(50):
    Bomb(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        all_sprites.update(event)
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
