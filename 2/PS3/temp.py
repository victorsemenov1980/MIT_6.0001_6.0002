#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:33:50 2020

@author: user
"""
import random

tile={}
width=5
height=5
dirt_amount=10
x=[]
y=[]
for i in range(1,width+1):
            x.append(i)
for i in range(1,height+1):
            y.append(i)
for i in x:
    for j in y:
        tile[i,j]=0

print(tile)

pos=(2,1)
capacity=5
if pos in tile:
    tile[pos]-=capacity

print(tile[pos])
z=list(tile.values())
print(z.count(0))

pos=(1.5,0.8)
x=(round(pos[0]), round(pos[1]))
print(x)
furniture_tiles=[(1,1),(1,5)]
x=random.randint(0,width)
y=random.randint(0,height)
z=(x,y)
if z not in furniture_tiles:
    print(z)

z=list(tile.keys())
z1=random.randint(0,len(z))
z2=z[z1]

x=z2[0]
y=z2[1]
print((x,y))

