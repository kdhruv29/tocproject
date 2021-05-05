from svg_backend import SVGBackend
from turtle import Turtle
from grammar import Grammar

backend = SVGBackend()
turtle = Turtle(backend)

grammar = Grammar()

grammar.add_non_terminal('RS', [
    lambda turtle: turtle.forward(2), 
    lambda turtle: turtle.turn_right(89.9),
    lambda turtle: turtle.scale(1.00001),
    'RS'])

grammar.expand('RS', turtle, 300)
backend.write('rect_spiral.svg')
