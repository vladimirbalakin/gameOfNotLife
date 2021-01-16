import pygame as pgm


def get_dead():
    pgm.init()

    w, h = 640, 480
    root = pgm.display.set_mode((w, h))

    running = True

    font = pgm.font.SysFont(None, 120)
    img = font.render('You dead', True, 'RED')
    root.blit(img, (20, 20))
    pgm.display.flip()

    while running:
        for e in pgm.event.get():
            if e.type == pgm.QUIT:
                running = False


def get_win():
    pgm.init()

    w, h = 640, 480
    root = pgm.display.set_mode((w, h))

    running = True

    font = pgm.font.SysFont(None, 120)
    img = font.render('You win', True, 'RED')
    root.blit(img, (20, 20))
    pgm.display.flip()

    while running:
        for e in pgm.event.get():
            if e.type == pgm.QUIT:
                running = False
