import Tkinter as tk
from random import *
from turtle import *
from base import vector

ball = vector(-200, -200)
speed(0, 0)
targets = []


def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200


def tap(x, y):
    #responde to the screen
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200)/ 25
        speed.y = (y + 200)/ 25


def draw():
    #draw the ball and targets
    clear()
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'pink')
    update()


def move():
    #movement of ball and target
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)
    
    for target in targets:
        target.x -= 0.5
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        #I'd stop in video 5, minute: 15:17


setup(420, 420, 370, 0)