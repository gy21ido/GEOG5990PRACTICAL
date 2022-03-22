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
import csv

# Read in environment
#open the txt file as csv
file = open('in.txt', newline='') 
dataset = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
#create an environment that stores the csv data
environment = []
# Lines above happen before any data is processed
for row in dataset:
    rowlist=[]
    # Lines above happen before each row is processed
    for values in row:
        rowlist.append(values) #append each row value to a rowlist
    environment.append(rowlist) #this happens after each row is processed and the rowlist is appended to the  environment

# Display environment
plt.xlim(0, len(environment[0]))
plt.ylim(0, len(environment))
plt.imshow(environment)

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

#neighbourhood communication
neighbourhood= 20

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

#test to see it works
# a = agentframework.Agent()
# print (f"Agent coordinates before moving: {a.y, a.x}")

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        #make the agents eat in the environment
        agents[i].eat()
     #make the agents interact with neighbourhood agents in their environment
        agents[i].share_with_neighbours(neighbourhood)   
#test to see it works
# a.move()
# print (f"Agent coordinates after moving: {a.y, a.x}")

#plot the newly created environment
plt.xlim(0, len(environment[0]))
plt.ylim(0, len(environment))
plt.imshow(environment)

for i in range(num_of_agents):
    plt.scatter(agents[i].x,agents[i].y)
plt.show()

#calculate distance between agents
# for agents_row_a in agents:
#     for agents_row_b in agents:
#         distance = distance_between(agents_row_a, agents_row_b) 
        
#write the environment out as a file        
f2 = open('environment.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
    writer.writerow(row)		# List of values.
f2.close()

#write out the total amount stored by all the agents on a line
#Can you get the model to append the data to the file, rather than clearing it each time it runs? 
total = 0
total1 = []
for a in agents:
    print(a.store)
    total+=a.store
    print(total)
    total1.append(total)
f3 = open('total.csv', 'w', newline='') 
writer = csv.writer(f3, delimiter=',')
writer.writerow(total1)
#for row in total1:		
 	#writer.writerow([row])		# List of values.
#print(f"row is {row}")
f3.close()

# print the agents to test for the location and store showing
for agent in agents: 
    print (agent)