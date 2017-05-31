#!/usr/bin/python

# This is the 5th program from Kunal Chawla's course from udacity
# to run in ubuntu/linux, you need to install python-tk package
# sudo apt-get install apt-get // in ubuntu.
# This is an enhancement to the 4th program i.e. squre-turtle.py

import turtle

def draw_square(some_turtle_name):
  for i in range(1,5):
    some_turtle_name.forward(100)
    some_turtle_name.right(90)

def draw_art():
  window = turtle.Screen()
  window.bgcolor("red")

  # Create the turtle Brad - Draws a square
  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("yellow")
  brad.speed(2)
  for i in range(1,37):
    draw_square(brad)
    brad.right(10)

  window.exitonclick()

draw_art()
