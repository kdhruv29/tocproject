from svg_backend import SVGBackend
from turtle import Turtle
from grammar import Grammar
from turtle import ThickTurtle
from turtle import NarrowingTurtle

backend = SVGBackend()
turtle = Turtle(backend)
grammar = Grammar()

right_segment = [
    lambda turtle: turtle.forward(0.1),
    lambda turtle: turtle.turn_right(5)
]

left_segment = [
    lambda turtle: turtle.forward(0.1),
    lambda turtle: turtle.turn_left(5)
]

#grammar.add_non_terminal('Left', left_segment * 7)
#grammar.add_non_terminal('Left', left_segment * 10)
grammar.add_non_terminal('Left', left_segment * 13)

#grammar.add_non_terminal('Right', right_segment * 7)
#grammar.add_non_terminal('Right', right_segment * 10)
grammar.add_non_terminal('Right', right_segment * 13)


scale = 0.5

grammar.add_non_terminal('Tree', [
    lambda turtle: turtle.store(),
    'Left',
    lambda turtle: turtle.scale(scale),
    'Tree',
    lambda turtle: turtle.restore(),
    'Right',
    lambda turtle: turtle.scale(scale),
    'Tree',
])

grammar.expand('Tree', turtle, 15)
backend.write('tree.svg')

