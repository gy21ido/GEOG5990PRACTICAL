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
# create a fixed number of agents and number of iterations
# =============================================================================
num_of_agents= 10
num_of_iterations= 100

# =============================================================================
# create a list of agents to better store the coordinates
# =============================================================================
agents= []

# =============================================================================
# loop through agents number and append coordinates
# =============================================================================
for i in range(num_of_agents):
    agents.append([random.randint(0,100), random.randint(0,100)])

# =============================================================================
# this moves the agents for a number of times within a number of iterations
# =============================================================================
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        # Change y 
        # use the torus solution to create boundary solutions
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        # Change x
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

# =============================================================================
# print agent list after movement
# =============================================================================
print (agents)

# =============================================================================
# plot the agents on a scatter graoh
# =============================================================================
plt.ylim(0, 100)
plt.xlim(0, 100)
for i in range(num_of_agents):
    plt.scatter(agents[i][1],agents[i][0])
plt.show() 

# =============================================================================
# Calculate the left most, right most, upmost, and downmost agents 
# plot them in different colours
# =============================================================================
for i in range(num_of_agents):
    plt.scatter(agents[i][1],agents[i][0], color='grey')
    # make the most easterly coordinate have red colour
    e = max(agents, key=operator.itemgetter(1))
    plt.scatter(e[1],e[0], color='red')
    #plot the upmost coordinate with black colour
    u = max(agents, key=operator.itemgetter(0))
    plt.scatter(u[1],u[0], color='black')
    #plot the downmost coordinate with blue colour
    d = min(agents, key=operator.itemgetter(0))
    plt.scatter(d[1],d[0], color='blue')
    #plot the most west coordinate with green colour
    w = min(agents, key=operator.itemgetter(1))
    plt.scatter(w[1],w[0], color='green')
plt.show()
