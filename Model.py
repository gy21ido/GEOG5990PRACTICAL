# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 17:37:01 2022

This practical begins the building of the Model program. 
Variables representing two agents' locations (y and x coordinates) were created. 
The agents move around through a random walk, and the distance between them was calculated.

@author: IYANULOLUWA
"""
import random
import operator
import matplotlib.pyplot as plt

# =============================================================================
# set first set of variables (agents)
# =============================================================================
# x0= 50
# y0= 50

# =============================================================================
# create a list of agents to better store the coordinates
# =============================================================================
agents= []

# =============================================================================
# random walk one step for the first set of agents
# =============================================================================
# if random.random() < 0.5:
#     y0 += 1
# else:
#     y0 -= 1

# if random.random() < 0.5:
#     x0 += 1
# else:
#     x0 -= 1

# print(y0, x0) 

# =============================================================================
# make new sets of agents and move them once as previous agents
# =============================================================================
# y1= 50
# x1= 50


# =============================================================================
# append the coordinates to the agents list, this adds the first set of coordinates
# =============================================================================
agents.append([random.randint(0,99),random.randint(0,99)])
print (agents) #prints first set of agents list

# =============================================================================
# append new set of coordinates to the list
# =============================================================================
agents.append([random.randint(0,99),random.randint(0,99)])
print (agents) #prints the whole list of first and second coordinates

# =============================================================================
# random walk for new agents set
# =============================================================================
# if random.random() < 0.5:
#     y1+=1
# else:
#     y1-=1

# if random.random() < 0.5:
#     x1+=1
# else:
#     x1-=1
# print (y1,x1)

# =============================================================================
# take first random walk with first set of coordinates
# =============================================================================
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

# =============================================================================
# take first random walk with second set of coordinates
# =============================================================================
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

# =============================================================================
# print agent list after movement
# =============================================================================
print (agents)

# =============================================================================
# print maximum agent
# =============================================================================
print (max(agents))

#this gets the second element in the list using index
print(max(agents, key=operator.itemgetter(1)))    

#Plot the agents on a graph
plt.ylim(0, 100)
plt.xlim(0, 100)
plt.scatter(agents[0][1],agents[0][0])
plt.scatter(agents[1][1],agents[1][0])
plt.show()

# make the most easterly coordinate have red colour
m = max(agents, key=operator.itemgetter(1))
plt.scatter(m[1],m[0], color='red')
plt.show()

# =============================================================================
# Find the distance between the coordinates
# =============================================================================
# distance= (((y0-y1)**2) + ((x0-x1)**2))**0.5
# print (distance)

