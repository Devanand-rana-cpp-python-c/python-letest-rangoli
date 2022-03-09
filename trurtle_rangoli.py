# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:34:32 2022

@author: devanand
"""
import turtle as t
colors=["green", "red","orange","blue","purple","yellow" ]
t.shape=("turtle")
t.tracer(2)
t.bgcolor('black')

for x in range(150):
    t.pencolor(colors[x%6])
    t.width(x//20)
    t.forward(x)
    t.left(120)
    
    for y in range(2):
        t.fd(x)
        t.rt(90)
        
t.exitonclick()
