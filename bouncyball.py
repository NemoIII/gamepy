from random import *
from turtle import *
from base import vector


def value():
	#this will generate me value from [-5, -3] to [3, 5]
	return (3 + random() * 2) * choice([-1, 1])

	