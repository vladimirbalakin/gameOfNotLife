from time import sleep

import pygame as pgm

from error import get_error

pgm.init()

w, h = 640, 480
root = pgm.display.set_mode((w, h))
need_to_flip = False


class Image:
    x, y = 0, 0
    img = pgm.image.load(r"images/level1.png")

    def draw(self):
        global need_to_flip
        root.blit(self.img, (self.x, self.y))
        need_to_flip = True
        pgm.display.flip()


class Polygon(Image):
    step, step_up = 10, 30
    speed = 1
    going = 0
    going_up = 0

    def right(self):
        global need_to_flip
        self.going = -self.speed
        need_to_flip = True
        self.draw(self)

    def left(self):
        global need_to_flip
        self.going = self.speed
        need_to_flip = True
        self.draw(self)

    def up(self):
        global need_to_flip
        self.going_up = 2
        need_to_flip = True
        self.draw(self)

    def rebuilt(self):
        if self.going > 0:
            self.going = self.speed
        if self.going < 0:
            self.going = -self.speed

    def speed_up(self):
        self.speed += 1

    def stop_moving(self):
        self.going = 0

    def stop_moving_up(self):
        self.going_up = 0

    def speed_down(self):
        self.speed -= 1

    def go(self):
        self.x += self.going
        self.y += self.going_up
        self.draw(self)
        pgm.display.flip()


poly = Polygon
running = True
#try:
while running:
    for e in pgm.event.get():
        if e.type == pgm.QUIT:
            running = False
        if e.type == pgm.KEYDOWN:
            if e.key == pgm.K_d:
                poly.right(poly)
            if e.key == pgm.K_a:
                poly.left(poly)
            if e.key == pgm.K_w:
                poly.up(poly)
            if e.key == pgm.K_LSHIFT:
                poly.speed_up(poly)
                poly.rebuilt(poly)
        if e.type == pgm.KEYUP:
            if e.key == pgm.K_d:
                poly.stop_moving(poly)
            if e.key == pgm.K_a:
                poly.stop_moving(poly)
            if e.key == pgm.K_w:
                poly.stop_moving_up(poly)
            if e.key == pgm.K_LSHIFT:
                poly.speed_down(poly)
                poly.rebuilt(poly)
    root.fill((255, 255, 255))
    poly.go(poly)
    sleep(0.01)
    if need_to_flip:
        pgm.display.flip()
        need_to_flip = False
#except:
#    get_error()
