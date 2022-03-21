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
import agentframework

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5


num_of_agents = 10
num_of_iterations= 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

#test to see it works
a = agentframework.Agent()
print (f"Agent coordinates before moving: {a.y, a.x}")

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        
#test to see it works
a.move()
print (f"Agent coordinates after moving: {a.y, a.x}")

plt.xlim(0, 99)
plt.ylim(0, 99)
for i in range(num_of_agents):
    plt.scatter(agents[i].x,agents[i].y)
plt.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
        
