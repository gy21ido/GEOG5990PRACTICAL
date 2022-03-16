# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 17:37:01 2022

This practical begins the building of the Model program. 
Variables representing two agents' locations (y and x coordinates) were created. 
The agents move around through a random walk, and the distance between them was calculated.

@author: IYANULOLUWA
"""
import random
# =============================================================================
# set first set of variables (agents)
# =============================================================================
x0= 50
y0= 50

# =============================================================================
# random walk one step for the first set of agents
# =============================================================================
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0, x0) 

# =============================================================================
# make new sets of agents and move them once as previous agents
# =============================================================================
y1= 50
x1= 50

# =============================================================================
# random walk for new agents set
# =============================================================================
if random.random() < 0.5:
    y1+=1
else:
    y1-=1

if random.random() < 0.5:
    x1+=1
else:
    x1-=1
print (y1,x1)

# =============================================================================
# Find the distance between the coordinates
# =============================================================================
distance= (((y0-y1)**2) + ((x0-x1)**2))**0.5
print (distance)