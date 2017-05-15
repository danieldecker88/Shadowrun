import os
import pygame
import sys

pygame.init()

graphics_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","resources", "graphics"))
joshua_path = os.path.join(graphics_dir, "josh.bmp")
josh = pygame.image.load(joshua_path)
josh_rect = josh.get_rect()

overlays_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","resources", "map"))
redmond_barrens_path = os.path.join(overlays_dir, "RedmondBarrens.png")
redmond_barrens = pygame.image.load(redmond_barrens_path)
redmond_barrens_rect = redmond_barrens.get_rect()


size = tuple([5*x for x in josh.get_size()])
screen = pygame.display.set_mode(redmond_barrens.get_size())

class Character(pygame.sprite.Sprite):

    def __init__(self, image, position = (0,0)):
        pygame.sprite.Sprite.__init__(self)

        self.image = image.convert()
        self.rect = self.image.get_rect()
        self.rect.move_ip(position[0], position[1])

    def move(self, amount=(0,0)):
        self.rect.move_ip(amount[0], amount[1])

class Background(pygame.sprite.Sprite):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)

        self.image = image.convert()
        self.rect = self.image.get_rect()

class NPCs(pygame.sprite.RenderPlain):

    def __init__(self):
        pygame.sprite.Group.__init__(self)
        pass

class Backgrounds(pygame.sprite.RenderPlain):

    def __init__(self):
        pygame.sprite.Group.__init__(self)
        pass


josh_char = Character(image=josh, position=(40,40))
npcs = NPCs()
npcs.add(josh_char)

map = Background(image = redmond_barrens)
layers = Backgrounds()
layers.add(map)

pygame.key.set_repeat(10, 10)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: josh_char.move((5, 0))
            if event.key == pygame.K_LEFT: josh_char.move((-5, 0))
            if event.key == pygame.K_UP: josh_char.move((0, -5))
            if event.key == pygame.K_DOWN: josh_char.move((0, 5))
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP]: josh_char.move((0, -5))
        # if keys[pygame.K_DOWN]: josh_char.move((0, 5))
        # if keys[pygame.K_LEFT]: josh_char.move((-5, 0))
        # if keys[pygame.K_RIGHT]: josh_char.move((5, 0))

    layers.draw(screen)
    npcs.draw(screen)

    pygame.display.flip()