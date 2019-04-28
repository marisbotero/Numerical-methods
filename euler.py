# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:50:48 2019

@author: maris
"""

from vpython import *

ball = sphere(pos=vector(-5,0,0), radius=0.5,color=color.cyan)
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)
ball.velocity = vector(25,0,0)
deltat = 0.005
t = 0
ball.pos = ball.pos + ball.velocity*deltat
while t < 3:
    rate(100)
    if ball.pos.x > wallR.pos.x:
        ball.velocity.x = -ball.velocity.x
        ball.pos = ball.pos + ball.velocity*deltat 
        t = t + deltat
   
