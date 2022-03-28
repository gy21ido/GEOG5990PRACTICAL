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
import matplotlib.animation 

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
# plt.xlim(0, len(environment[0]))
# plt.ylim(0, len(environment))
# plt.imshow(environment)

# def distance_between(agents_row_a, agents_row_b):
#     return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

# Get the user to interact with the model by providing the number of agents and iterations
right_input = False
while(not right_input):
    try:
        num_of_agents = input ('Enter an integer number of agents between 0 and 300: ')
        num_of_iterations = input ('Enter an integer number of iterations between 0 and 100: ')
        # Check if the inputs are correct
        if(num_of_agents.isnumeric() and num_of_iterations.isnumeric()):
            num_of_agents = int(num_of_agents)
            num_of_iterations = int(num_of_iterations)
            if(num_of_agents > 0 and num_of_agents < 300 and num_of_iterations > 0 and num_of_iterations < 100):
                right_input = True
                break
            else:
                print("Enter a number between 0 and 300 for agents and 0 and 100 for iterations\n\n")
        else:
            print("Enter a valid number\n\n")
    except ValueError:
        print("The input is invalid, please try again!\n\n")

agents = []

#neighbourhood communication
neighbourhood= 20

#set size for plot
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

# Make the agents.
random.shuffle(agents)
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

#test to see it works
# a = agentframework.Agent()
# print (f"Agent coordinates before moving: {a.y, a.x}")

carry_on = True

def update(frame_number):
    fig.clear()  
    global carry_on

# Move the agents.
# for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        #make the agents eat in the environment
        agents[i].eat()
     #make the agents interact with neighbourhood agents in their environment
        agents[i].share_with_neighbours(neighbourhood)  
        #print ('Number of iterations is ',num_of_iterations)
        
    # if random.random() < 0.1:
    #     carry_on = False
    #     print("stopping condition") 
        
#test to see it works
# a.move()
# print (f"Agent coordinates after moving: {a.y, a.x}")

    # plot the newly created environment
    plt.xlim(0, len(environment[0]))
    plt.ylim(0, len(environment))
    plt.imshow(environment)
    for i in range(num_of_agents):
        plt.scatter(agents[i].x,agents[i].y)
    plt.show()

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
#create a function to run the model
# def run():
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
# canvas.draw()
plt.show()
    
