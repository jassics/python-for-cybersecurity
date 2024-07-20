#!/usr/bin/python

# This is the 3rd program from Kunal Chawla's course from udacity
# to run in ubuntu/linux, you need to install python-tk package
# sudo apt-get install apt-get // in ubuntu.

import turtle

def draw_square():
  window = turtle.Screen()
  window.bgcolor("red")
  
  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("yellow")
  brad.speed(2)

  brad.forward(100)
  brad.right(90)
  brad.forward(100)
  brad.right(90)
  brad.forward(100)
  brad.right(90)
  brad.forward(100)
  brad.right(90)
  
  window.exitonclick()

draw_square()
