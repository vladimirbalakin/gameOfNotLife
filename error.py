import pygame as pgm


def get_error():
    pgm.init()
    w, h = 640, 480
    root = pgm.display.set_mode((w, h))

    running = True

    font = pgm.font.SysFont(None, 200)
    img = font.render('ERROR', True, 'RED')
    root.blit(img, (20, 20))
    pgm.display.flip()

    while running:
        for e in pgm.event.get():
            if e.type == pgm.QUIT:
                running = False
