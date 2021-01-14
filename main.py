import pygame as pgm

from error import get_error

pgm.init()

w, h = 640, 480
root = pgm.display.set_mode((w, h))
need_to_flip = False

running = True
try:
    while running:
        for e in pgm.event.get():
            if e.type == pgm.QUIT:
                running = False
        if need_to_flip:
            pgm.display.flip()
            need_to_flip = False
except:
    get_error()
