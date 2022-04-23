# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 17:37:01 2022

This model shows an environment with full breeding population of agents and wolves. 
Agents interact with the environment by eating it, while wolves interact with agents by eating them.
Breeding is added to populate the environment, as both wolves and agents breed with one another.

Version: 1.0.1

@author: 201576424

"""

#import modules and packages to be used
import random
import matplotlib.pyplot as plt
import agentframework
import csv
import matplotlib.animation 
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#matplotlib.use('TkAgg') 
import tkinter 
import requests
import bs4
import sys

#variables declarations for tkinter window
root = tkinter.Tk()     #builds the main tkinter window 'root'
root.wm_title("Agent Based Model") #add a title to the tkinter window

#agents variables declaration
agents = [] #empty list to store the agents coordinates
sheep_pace = 5 # The pace of the sheep
sheep_colour = ['blue', 'pink'] #colours to identify sheep after breeding (male- blue, female- pink)

#wolves variables declaration
wolves = [] #empty list to store the agents predators (wolves) coordinates
wolf_colour = ['black', 'gold'] #colours to identify wolves after breeding (male- black, female- gold)

#gender for both agents and sheep (m- male, f-female)
gender = ["m", "f"]

#eating variables to control control the amount of environment that is eaten
permitted_graze_amount = 60000 
a = 0 # Number of iterations incrementing
grazed_land = 0 # Amount of environment grazed

carry_on = True

#download html data using python through web scraping method
r= requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content= r.text

soup= bs4.BeautifulSoup(content, 'html.parser')
tds_y= soup.find_all(attrs= {"class": "y"})
tds_x= soup.find_all(attrs= {"class": "x"})

#test to see the web scraping works
#print (tds_y) 
#print (tds_y)
#print (len(tds_x))

# Get the user to interact with the model by providing the number of agents and iterations
# use try/exception to catch errors associated with user input, user can quit before model runs too
right_input = False
while(not right_input):
    try:
        print("Press q to QUIT!")
        num_of_agents = input (f'Enter an integer number of agents between 0 and {len(tds_y)}: ')
        if(num_of_agents == "q" or num_of_agents == "Q"):
            sys.exit()
        num_of_iterations = input ('Enter an integer number of iterations between 0 and 200: ')
        if(num_of_iterations == "q" or num_of_iterations == "Q"):
            sys.exit()
        num_of_wolves = input ('Enter an integer to represent number of wolves between 0 and 50: ')
        # Check if the inputs are correct
        if(num_of_wolves == "q" or num_of_wolves == "Q"):
            sys.exit()
        if(num_of_agents.isnumeric() & num_of_iterations.isnumeric() & num_of_wolves.isnumeric()):
            num_of_agents = int(num_of_agents)
            num_of_iterations = int(num_of_iterations)
            num_of_wolves = int(num_of_wolves)
            if(num_of_agents >= 0 and num_of_agents <= len(tds_y) and num_of_iterations > 0 
               and num_of_iterations <= 200 and num_of_wolves >= 0 and num_of_wolves <= 50):
                right_input = True
                break
            else:
                print("Enter a number between 0 and 300 for agents and 0 and 100 for iterations\n\n")
        else:
            print("Enter a valid number\n\n")
    except ValueError:
        print("The input is invalid, please try again!\n\n")


# Read in environment
#open the txt file as csv
file = open('in.txt', newline='') 
dataset = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
environment = [] #create an environment that stores the csv data

# Lines above happen before any data is processed
for row in dataset:
    rowlist=[]
    # Lines above happen before each row is processed
    for values in row:
        rowlist.append(values) #append each row value to a rowlist
    environment.append(rowlist) #this happens after each row is processed and the rowlist is appended to the  environment

#neighbourhood communication
neighbourhood= 20

#set size for plot
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents from the web scrapped data
random.shuffle(agents)
for i in range(num_of_agents):
    y= int(tds_y[i].text)
    x= int(tds_x[i].text)
    agents.append(agentframework.Agent(environment, agents, sheep_pace, gender[i % 2], 
                                       sheep_colour[i % 2], x = x, y = y))
    
# Make the wolves from the web scrapped data
random.shuffle(wolves)
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolf(environment, agents, wolves, 2 * sheep_pace, 
                                      gender[i % 2], wolf_colour[i % 2]))

#test to see it works
# a = agentframework.Agent()
# print (f"Agent coordinates before moving: {a.y, a.x}")

#test to see it works
# b = wolfframework.Wolf()
# print (f"Agent coordinates before moving: {b.y, b.x}")

def update(frame_number):
    '''
    Updates the tkinter window/ frame

    Parameters
    ----------
    frame_number : int (optional)
        
    Returns
    -------
    None.

    '''
    fig.clear()  
    global carry_on 
    global grazed_land # Amount of environment grazed
    food_unit_eaten = 0

    # Agents will move and eat
    for i in range(len(agents)):
        if(grazed_land <= permitted_graze_amount):
            agents[i].move()
            #make the agents eat in the environment
            food_unit_eaten = agents[i].eat()
            #make the agents interact with neighbourhood agents in their environment
            agents[i].share_with_neighbours(neighbourhood)
        # Sheep breeds      
        agents[i].breed()
        grazed_land += food_unit_eaten
    
    
    # Wolves will move and eat
    for i in range(len(wolves)):
        wolves[i].move()
        #make the agents eat in the environment
        wolves[i].eat() # Gets the agents eaten
        wolves[i].breed()
        
    #test to see it works
    # a.move()
    # print (f"Agent coordinates after moving: {a.y, a.x}")

    # plot the newly created environment
    plt.xlim(0, len(environment[0]))
    plt.ylim(0, len(environment))
    plt.imshow(environment)
    # Agents
    for i in range(len(agents)):
        plt.scatter(agents[i].x,agents[i].y, color = agents[i].colour)
        
    # Wolves
    for i in range(len(wolves)):
        plt.scatter(wolves[i].x,wolves[i].y, color = wolves[i].colour)

def gen_function(b = [0]):
    '''
    Function to generate the frame

    Parameters
    ----------
    b : int, optional
        DESCRIPTION. The default is [0].

    Yields
    ------
    int
        value for the frames generated.

    '''
    global a
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
#create a function to run the model
def run():
    """
    Runs the animated model

    Returns
    -------
    Animation is generated from matplotlib function that calls the gen_function

    """
    animation = matplotlib.animation.FuncAnimation(fig, update, frames = gen_function, repeat=False)
    canvas.draw()
    
#create and lay out a matplotlib canvas embedded within our window and associated with fig, our matplotlib figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

menu_bar= tkinter.Menu(root)
button = tkinter.Button(root, text = "Click and Quit", command = root.destroy)
button.pack()
root.config(menu= menu_bar)
model_menu= tkinter.Menu(menu_bar)
menu_bar.add_cascade(label= "Model", menu= model_menu)
model_menu.add_command(label= "Run Model", command= run)

#try/except to catch error associated with two windows opening and code not stopping after iteration ends
try:
    tkinter.mainloop() #wait for user interactions
except KeyboardInterrupt:
    root.destroy()
