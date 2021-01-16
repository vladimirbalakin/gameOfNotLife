from time import sleep

import pygame as pgm

from error import get_dead, get_win

pgm.init()

w, h = 640, 480
root = pgm.display.set_mode((w, h))
root.fill((255, 255, 255))
pgm.display.flip()
need_to_flip = False
running = True


class Image:
    x, y = 0, 0
    img = pgm.image.load(r"images/level1.png")

    def draw(self):
        global need_to_flip
        root.blit(self.img, (self.x, self.y))
        need_to_flip = True
        # pgm.display.flip()


class Polygon(Image):
    step, step_up = 10, 30
    speed = 1
    going = 0
    going_up = 0

    def right(self):
        global need_to_flip
        self.going = -self.speed
        need_to_flip = True
        self.draw()

    def left(self):
        global need_to_flip
        self.going = self.speed
        need_to_flip = True
        self.draw()

    def up(self):
        global need_to_flip
        self.going_up = 2
        need_to_flip = True
        self.draw()

    def down(self):
        global need_to_flip
        if self.going_up <= 0:
            self.going_up = -3
            need_to_flip = True
            self.draw()

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

    def stop_moving_down(self):
        if self.going_up <= 0:
            self.going_up = 0

    def speed_down(self):
        self.speed -= 1

    def go(self):
        self.x += self.going
        self.y += self.going_up
        self.draw()
        # pgm.display.flip()


poly = Polygon()
poly.go()


class Hero(Image):
    img = pgm.image.load(r"images/hero.png")

    def __init__(self):
        color = (255, 255, 255, 255)
        while color == (255, 255, 255, 255):
            color = root.get_at((self.x + self.img.get_size()[0] // 2, self.y + self.img.get_size()[1] + 1))
            if color == (255, 255, 255, 255):
                self.y += 2
            root.fill((255, 255, 255, 255))
            poly.draw()
            self.draw()
            pgm.display.flip()
            sleep(0.01)

    def draw(self):
        pgm.draw.circle(root, (200, 0, 200),
                        (self.x + self.img.get_size()[0] // 2, self.y + self.img.get_size()[1] // 2),
                        self.img.get_size()[0] // 2)

    def is_good_place(self):
        global running
        color = root.get_at((self.x + self.img.get_size()[0] // 2, self.y + self.img.get_size()[1] + 1))
        if color == (255, 255, 255, 255):
            if poly.going_up <= 0:
                poly.down()
            return False
        good = True
        while True:
            color = root.get_at((self.x + self.img.get_size()[0] // 2, self.y + self.img.get_size()[1] + 1))
            if color == (255, 255, 255, 255) and poly.going_up <= 0:
                if good:
                    poly.down()
                else:
                    self.y += 1
                break
            if color == (0, 0, 0, 255):
                poly.stop_moving_down()
                good = False
                self.y -= 1
                continue
            if color == (255, 0, 0, 255):
                get_dead()
                running = False
            if color == (0, 0, 255, 255):
                get_win()
                running = False

            # pgm.display.flip()
            return True

        color = root.get_at((self.x + self.img.get_size()[0] // 2, self.y + self.img.get_size()[1] + 1))
        if color == (255, 255, 255, 255):
            self.y += 1
        return True
        return Trueddd


hero = Hero()
could_start_up = True
while running:
    for e in pgm.event.get():
        if e.type == pgm.QUIT:
            running = False
        if e.type == pgm.KEYDOWN:
            if e.key == pgm.K_d:
                poly.right()
            if e.key == pgm.K_a:
                poly.left()
            if e.key == pgm.K_w and could_start_up:
                poly.up()
            if e.key == pgm.K_LSHIFT:
                poly.speed_up()
                poly.rebuilt()
        if e.type == pgm.KEYUP:
            if e.key == pgm.K_d:
                poly.stop_moving()
            if e.key == pgm.K_a:
                poly.stop_moving()
            if e.key == pgm.K_w:
                poly.stop_moving_up()
            if e.key == pgm.K_LSHIFT:
                poly.speed_down()
                poly.rebuilt()
    root.fill((255, 255, 255))
    poly.go()
    hero.draw()
    pgm.display.flip()
    if not hero.is_good_place():
        could_start_up = False
    else:
        could_start_up = True
    sleep(0.01)
