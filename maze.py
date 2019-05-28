from random import random
from turtle import *
from base import line


def draw():
    color('black')
    width(5)
    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random()>0.5:
                line(x, y, x+40, y+40)
            else:
                line(x, y+40, x+40, y)


''' Parei no meio do vídeo, continuar depois'''