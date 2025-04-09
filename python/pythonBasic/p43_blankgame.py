#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello PyGame World!!")



while True:
    for event in pygame.event.get():
        if type(event) == QUIT:
            pygame.quit()
            sys.exit()