from svg_backend import SVGBackend
from turtle import Turtle
from grammar import Grammar
from turtle import ThickTurtle
from turtle import NarrowingTurtle

backend = SVGBackend()
turtle = Turtle(backend)

grammar = Grammar()

grammar.add_non_terminal('Forward Right', [
    lambda turtle: turtle.forward(1.0),
    lambda turtle: turtle.turn_right(60)
])
grammar.add_non_terminal('Forward Left', [
    lambda turtle: turtle.forward(1.0),
    lambda turtle: turtle.turn_left(60)
])

grammar.add_non_terminal('Root', [
    'Tree',
    lambda turtle: turtle.turn_left(120),
    'Tree',
    lambda turtle: turtle.turn_left(120),
    'Tree',
])

scale = 0.5
grammar.add_non_terminal('Scale', [
    lambda turtle: turtle.scale(scale),
])
grammar.add_non_terminal('Scale', [])

grammar.add_non_terminal('Tree', [
    lambda turtle: turtle.store(),
    'Forward Left',
    'Scale',
    'Tree',
    lambda turtle: turtle.restore(),
    lambda turtle: turtle.store(),
    'Forward Right',
    'Scale',
    'Tree',
    lambda turtle: turtle.restore(),
], 8)

#for i in range(0, 5):
backend = SVGBackend()
turtle = Turtle(backend)
grammar.expand('Root', turtle, 12)
backend.write('flower2.svg')
