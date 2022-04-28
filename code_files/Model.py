# -*- coding: utf-8 -*-10
"""
Created on Mon Jan 31 17:37:01 2022
This model shows an environment with full breeding population of agents and wolves. 
Agents interact with the environment by eating it, while wolves interact with agents by eating them.
Breeding is added to populate the environment, as both wolves and agents breed with one another.

Version: 1.1.0

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
# matplotlib.use('TkAgg') 
import tkinter 
import requests
import bs4
import sys
import time

#function that updates the tkinter plot window with required variables
def update(frame_number):
    '''
        Updates the tkinter window/ frame
    
        Parameters
        ----------
        frame_number : int (optional)
            
        Returns
        -------
            A change in the plot within tkinter.
        
        >>> update(0)
    

    '''
    fig.clear()  
    global carry_on 
    global grazed_land # Amount of environment grazed
    food_unit_eaten = 0

    # Agents will move and eat
    for i in range(len(agents)):
        if(grazed_land <= permitted_graze_amount):
            #agents move
            agents[i].move()
            #make the agents eat in the environment
            food_unit_eaten = agents[i].eat()
            #make the agents interact with neighbourhood agents in their environment
            agents[i].share_with_neighbours(neighbourhood)
        # Agent breeds      
        agents[i].breed()
        grazed_land += food_unit_eaten
    
    
    # Wolves will move and eat
    for i in range(len(wolves)):
        wolves[i].move()
        #make the agents eat in the environment
        wolves[i].eat() # Gets the agents eaten
        wolves[i].breed()
        
    #test to see it works
    # agent.move()
    # print (f"Agent coordinates after moving: {agent.get_y, agent.get_x}")

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

#define function that generates the tkinter frame
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
    global start_time
    start_time = time.time()
    animation = matplotlib.animation.FuncAnimation(fig, update, frames = gen_function, repeat=False)
    canvas.draw()

#guard for the module names
if __name__ == "__main__":
    #agents variables declaration
    agents = [] #empty list to store the agents coordinates
    sheep_pace = 5 # The pace of the sheep
    sheep_colour = ['blue', 'blue'] #colours to identify sheep after breeding (male and female are blue)

    #wolves variables declaration
    wolves = [] #empty list to store the agents predators (wolves) coordinates
    wolf_colour = ['black', 'black'] #colours to identify wolves, both black

    #gender for both agents (m- male, f-female)
    gender = ["m", "f"]

    # List to hold the distance between any two agents and any two wolves
    max_distance = []
    wolf_max_distance = []

    #neighbourhood communication
    neighbourhood= 20

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
            #check if inputs are correct for agents
            print("Press q to QUIT!")
            num_of_agents = input (f'Enter an integer number of agents between 0 and {len(tds_y)}: ')
            if(num_of_agents == "q" or num_of_agents == "Q"):
                sys.exit()
            num_of_iterations = input ('Enter an integer number of iterations between 0 and 200: ')
            if(num_of_iterations == "q" or num_of_iterations == "Q"):
                sys.exit()
            num_of_wolves = input ('Enter an integer to represent number of wolves between 0 and 50: ')
            
            # Check if the inputs are correct for wolves
            if(num_of_wolves == "q" or num_of_wolves == "Q"):
                sys.exit()
                
            # Number of times to run code
            num_of_loops = input("Enter number of loops (1 - 5). Use 1 as default: ")
            if(num_of_loops == "q" or num_of_loops == "Q"):
                sys.exit()
            if(num_of_agents.isnumeric() & num_of_iterations.isnumeric() & num_of_wolves.isnumeric()):
                num_of_agents = int(num_of_agents)
                num_of_iterations = int(num_of_iterations)
                num_of_wolves = int(num_of_wolves)
                num_of_loops = int(num_of_loops)
                if(num_of_agents >= 0 and num_of_agents <= len(tds_y) and num_of_iterations > 0 
                   and num_of_iterations <= 200 and num_of_wolves >= 0 and num_of_wolves <= 50 and num_of_loops >= 1 and num_of_loops <= 5):
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
    #curent number of agents before loop runs
    current_num_agents = 0
    #timer list for number of agents before loop starts
    timer_num_agents = []
    timer = []

    # Lines above happen before any data is processed
    for row in dataset:
        rowlist=[]
        # Lines above happen before each row is processed
        for values in row:
            rowlist.append(values) #append each row value to a rowlist
        environment.append(rowlist) #this happens after each row is processed and the rowlist is appended to the  environment
    
    #loop through the number of loops while controlling the amount of environment eaten 
    for loop in range(num_of_loops):
        #eating variables to control control the amount of environment that is eaten
        permitted_graze_amount = 60000 
        a = 0 # Number of iterations incrementing
        grazed_land = 0 # Amount of environment grazed
        carry_on = True
        #initialise time before loop starts
        start_time = 0
        #time after loop ends
        end_time = 0

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
        # a = agent
        # print (f"Agent coordinates before moving: {a.y, a.x}")
        
        #test to see it works
        # b = wolf
        # print (f"Wolf coordinates before moving: {b.y, b.x}")
        
            
        #set size for plot
        fig = plt.figure(figsize=(7, 7))
        ax = fig.add_axes([0, 0, 1, 1])
        root = tkinter.Tk()     #builds the main tkinter window 'root'
        root.wm_title(f"Agent Based Model: Figure {loop + 1}") #add a title to the tkinter window with figure for each loop number
        
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
        
        tkinter.mainloop() #wait for user interactions
        end_time = time.time()
        
        #Statistics from the model (for agents)
        # Calculate the left most, right most, upmost, and downmost agents 
        # plot them in different colours
        # =============================================================================
        print("\n==============================================")
        print ('AGENTS STATISTICS FROM THE MODEL')
        print("===============================")
        # make the most easterly coordinate have red colour
        e = max(agents, key = lambda agent: agent.get_y())
        print(f"Agent farthest to the East is: {e}")
        plt.scatter(e.get_x(), e.get_y(), color='red')
        #plot the upmost coordinate with pink colour
        u = max(agents, key = lambda agent: agent.get_x())
        print(f"Agent farthest to the North is: {u}")
        plt.scatter(u.get_x(), u.get_y(), color='pink')
        #plot the downmost coordinate with green colour
        d = min(agents, key = lambda agent: agent.get_x())
        print(f"Agent farthest to the South is: {d}")
        plt.scatter(d.get_x(), d.get_y(), color='green')
        #plot the most west coordinate with gold colour
        w = min(agents, key = lambda agent: agent.get_x())
        print(f"Agent farthest to the West is: {w}")
        plt.scatter(w.get_x(), w.get_y(), color='gold')
            
        # Largest distance between any two agents
        if(len(agents) > 1):
            for start, agent in enumerate(agents): # Loop through each agent
                if(start == len(agents) - 1): # Check if at the last agent the come out of loop
                    break
                for index in range(start + 1, len(agents)): # Get the distance between two agents
                    max_distance.append(agent.distance_between(agents[index]))
            print(f"The maximum distance between any two agent is: {max(max_distance)}")
        
        # Get birth rate, death rate, and population growth
        birth_death_rate = (len(agents) - num_of_agents) / num_of_agents
        print(f"Agents' Population growth is: {(birth_death_rate * 100):.2f}%")
        print(f"Agents' birth rate is: {(100 * agentframework.Agent.children / num_of_agents):.2f}%")
        print(f"Agents' death rate is: {(100 * agentframework.Wolf.agents_eaten / num_of_agents):.2f}%")
        
        #Statistics from the model (wolves)
        # Calculate the left most, right most, upmost, and downmost wolves 
        # plot them in different colours
        # =============================================================================
        print ("\n")
        print ('WOLVES STATISTICS FROM THE MODEL')
        print("===============================")
        # make the most easterly coordinate have purple colour
        p = max(wolves, key = lambda wolf: wolf.get_y())
        print(f"Wolf farthest to the East is: {p}")
        plt.scatter(p.get_x(), p.get_y(), color='purple')
        #plot the upmost coordinate with maroon colour
        q = max(wolves, key = lambda wolf: wolf.get_x())
        print(f"Wolf farthest to the North is: {q}")
        plt.scatter(q.get_x(), q.get_y(), color='maroon')
        #plot the downmost coordinate with darkgreen colour
        r = min(wolves, key = lambda wolf: wolf.get_x())
        print(f"Wolf farthest to the South is: {r}")
        plt.scatter(r.get_x(), r.get_y(), color='darkgreen')
        #plot the most west coordinate with orange colour
        s = min(wolves, key = lambda wolf: wolf.get_x())
        print(f"Wolf farthest to the West is: {s}")
        plt.scatter(s.get_x(), s.get_y(), color='orange')
        
        # Largest distance between any two wolves
        if(len(wolves) > 1):
            for start, wolf in enumerate(wolves): # Loop through each wolf
                if(start == len(wolves) - 1): # Check if at the last wolf the come out of loop
                    break
                for index in range(start + 1, len(wolves)): # Get the distance between two wolves
                    wolf_max_distance.append(agent.distance_between(wolves[index]))
            print(f"The maximum distance between any two wolves is: {max(max_distance)}")
        
        #wolves do not die, therefore get birth rate and population growth
        wolves_birth_rate = (len(wolves) - num_of_wolves) / num_of_wolves
        print(f"Wolves' Population growth is: {(wolves_birth_rate * 100):.2f}%")
        print(f"Wolves' birth rate is: {(100 * agentframework.Wolf.children / num_of_wolves):.2f}%")
        
        #time taken after total loop runs
        print(f"Elapsed time for running function is: {(end_time - start_time):.2f}secs")
        timer.append(end_time - start_time)
        timer_num_agents.append(num_of_agents + current_num_agents)
        #incrememnt number of agent by 20 for each loop
        current_num_agents += 20
        #list for agents and wolves after incrementing
        agents = []
        wolves = []
        
    #Plot time
    #set size for plot
    plt.figure("Number of agents against time taken")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Number of agents")
    plt.plot(timer, timer_num_agents, color='green', linewidth=2)
