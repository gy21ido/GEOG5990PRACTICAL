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
import time

# =============================================================================
# function that returns number of agents
# =============================================================================
def distance_between(agents_row_a, agents_row_b): 
    """

   This calculates the distance between agents_row_a and agents_row_b and returns the result.

    Parameters
    ----------
    a : agents_row_a
        This is one of the agents.
    b : agents_row_b
        This is one of the agents.
    
    Returns
    -------
    Number
        Distance between agents_row_a and agents_row_b.

    >>> a= agents[0]
    >>> b= agents[1]
    >>> print (a)
    >>> print (b)
    >>> distance_between(a,b)
        [75, 21]
        [26, 19]
        49.040799340956916

    """
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

# =============================================================================
# create a fixed number of agents and number of iterations
# =============================================================================
# num_of_agents= 10
# num_of_iterations= 100

# =============================================================================
# try a variety of different orders of magnitude of agent numbers and iterations 
# =============================================================================
list_num_agents = [_ for _ in range(10, 60, 10)]
num_of_iterations = 100

# =============================================================================
# create lists that hold the time, maximum, minimum and distance for various agent pairs.
# =============================================================================
time_list = []
max_list = []
min_list = []
list_distance = []

# =============================================================================
# loop through the list of number of agents to get each agents pair
# =============================================================================
for num_of_agents in list_num_agents:
    agents= []
    for i in range (num_of_agents):
        agents.append([random.randint(0,99),random.randint(0,99)]) #this makes sure we do not create x0 and y0  
    
# =============================================================================
#     this moves the agents for a number of times within a number of iterations
# =============================================================================
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            # Change y and solve boundary effects
            if random.random() < 0.5:
                agents[i][0] = (agents[i][0] + 1) % 100
            else:
                agents[i][0] = (agents[i][0] - 1) % 100
            # Change x and solve boundary effects
            if random.random() < 0.5:
                agents[i][1] = (agents[i][1] + 1) % 100
            else:
                agents[i][1] = (agents[i][1] - 1) % 100
    
# =============================================================================
#     plot the agents on a scatter plot            
# =============================================================================
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.figure #creates a new figure instance so you can draw a new plot on the figure
    ax = plt.gca() #gets the current figure axes to set the title
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            ax.scatter(agents[i][0], agents[i][1])
    ax.set_title(f"Agents scatter plot: {num_of_agents} agents")
    plt.show()
    
# =============================================================================
#     time code to check for computational effects
# =============================================================================
    start = time.process_time()
    # The code to run, here.
    distance_list= []
    for i in range(num_of_agents):
        for j in range(num_of_agents):
            if (i>j): #this ensures there is no repition amongst the agents pairs
                distance = distance_between(agents[j], agents[i])
                distance_list.append(distance)
                # print ("Agent pairs {0} and {1} are:" .format (j,i), agents[j], agents[i])
                # print ("The distance between agent pairs {0} and {1}  is: " . format(j,i), distance)
    #for the above, if you use i!=j, you get 90 distances in the distance list, it repeats
    end = time.process_time()
    time_list.append(end - start)
    max_list.append(max(distance_list))
    min_list.append(min(distance_list))
    list_distance.append((len(distance_list), distance_list))

# =============================================================================
#     Displays the time, maximum agent pair distance and minimum agent pair distance
# =============================================================================
    print(f"Properties for {num_of_agents} agents:")    
    print(f"time = {str(end - start)}")
    
    #find the maximum and minimum distance between the agent pair distances
    print (f"Maximum agents pairs distance is {max(distance_list)}")
    print (f"Minimum agents pairs distance is {min(distance_list)}\n\n")
    
# =============================================================================
# Plots graphs of the agents against time (at different magnitudes)
# =============================================================================
figure = plt.figure
ax = plt.gca()
ax.scatter(list_num_agents, time_list)
ax.set_title("Number of agents against time")
plt.show()
