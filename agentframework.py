# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:37:44 2022

@author: IYANULOLUWA
"""

import random

#create class Agent
class Agent:
    # Class variables
    Agent_id = 0 # Sheep id
    gender = ["m", "f"]
    breed_distance = 2
    
    # Function definitions    
    def __init__ (self, environment, agents, sheep_pace, gender, colour, child=False):  
        """
        This initialises variables x and y
        Parameters
        ----------
        x : Agent 
            This is one of the agents
        y : Agent
            This is one of the agents.

        Returns
        -------
        Number
            Agents coordinates.

        """
        self._x = random.randint(0,len(environment))
        self._y = random.randint(0,len(environment[0]))
        self.environment= environment
        self.store= 0
        self.agents= agents
        self.sheep_pace = sheep_pace # Default pace of sheep
        self.gender = gender # gender of the sheep
        self.colour = colour # colour of sheep
        self.id = self.create_new_sheep()
        self.child = child
        
    # Creates new sheep
    def create_new_sheep(self):
        """
        This creates new sheep after breeding among parent sheep
        Parameters
        -------
        

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        Agent.Agent_id += 1
        return Agent.Agent_id
        
    #this function gets the attribute value of x        
    def get_x(self):
        return self._x
    
    #this function sets the attribute value of x     
    def set_x(self, value):
        self._x = value
    
    x= property(get_x,set_x, "I am the 'x' property")
    
    #this function gets the attribute value of y    
    def get_y(self):
        return self._y
    
    #this function sets the attribute value of y    
    def set_y(self, value):
        self._y = value
    
    y= property(get_y,set_y, "I am the 'y' property")
    
    def move(self): #this method moves the agents between random positions
        """
        

        Returns
        -------
        None.

        """
        
        
        if (self.store < 50):
            #set the movement to be faster if they have more resources
            d = self.sheep_pace - 3 #distance of movement for less than 50
        else:
            d = self.sheep_pace #distance of movement for greater than 50
        nrows = len(self.environment)
        ncols = len(self.environment[0])
        if random.random() < 0.5:
            self._x = (self._x + d) % ncols
        else:
            self._x = (self._x - d) % ncols

        if random.random() < 0.5:
            self._y = (self._y + d) % nrows
        else:
            self._y = (self._y- d) % nrows
            
    def eat(self): # can you make it eat what is left?
        """
        

        Returns
        -------
        None.

        """
        
        eat_space = 10 # Amount of unit space to eat
        if self.store >= 100: # If the agent has eaten at least 100 units
                self.environment[self._y][self._x] += self.store # Vomit all the units eaten on a particular location
                self.store = 0 # Empty the agents bowel
        else: # If the agent has eaten less than 100 units
            if self.environment[self._y][self._x] > 0:
                if self.environment[self._y][self._x] >= eat_space:
                    self.environment[self._y][self._x] -= eat_space
                    self.store += 10
                else:
                    self.environment[self._y][self._x] = 0   
                    self.store += self.environment[self._y][self._x]
    
    # Breeding among sheep
    def breed(self):
        """
        This method is for breeding among sheep

        Returns
        -------
        None.

        """
        for index, agent in enumerate(self.agents):
            # Cannot mate with itself or with a sheep of the same gender
            # Must be close enought (within a proximity of 2 units)
            if(not(self.child) and not(self.gender == agent.gender) and (self.distance_between(agent) <= Agent.breed_distance)):
                i = random.randint(-1, 1)
                # self.agents.append(Agent(self.environment, self.agents, self.sheep_pace, Agent.gender[i % 2], "white"))
                new_child = Agent(self.environment, self.agents, self.sheep_pace, Agent.gender[i], "white", child=True)
                self.agents.append(new_child)
                print(f"An agent child is created - Location: {self.x}, {self.y}")
            # if(distance <= 5):
            #     print(f"This agent is dead: {agent}")
            #     self.agents.pop(index)
            #     break;
    
    def share_with_neighbours(self, neighbourhood):
        """
        

        Parameters
        ----------
        neighbourhood : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        #go through the agents list and find others within the neighbourhood distance
        # Loop through the agents in self.agents 
        for agent in self.agents:
        # Calculate the distance between self and the current other agent:   
            distance= self.distance_between(agent)
            if (distance <= neighbourhood):
                # share
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #check it works
                # print ("sharing:" + " " + str(distance) + " " + str(ave))
    
    #function to calculate the distance between agents (adapted from former function in Model.py)
    def distance_between(self, agent):
        """
        
        This calculates the distance between agents and self, and returns the result.

        Parameters
        ----------
        a : Agent
            This is one of the agents.
        b : Agent
            This is one of the agents.
        
        Returns
        -------
        Number
            Distance between a and b.


        """
        return (((agent._x - self._x)**2) + ((agent._y - self._y)**2))**0.5   
    
    #Can you override __str__(self) in the agents, as mentioned in the lecture on classes, 
#so that they display this information information about their location and stores when printed?            
 
    def __str__(self): 
        """
        

        Returns
        -------
        str
            DESCRIPTION.

        """
        return f"Location: ({self.x}, {self.y})\tStore: {self.store}"
    
    def __repr__(self):
        """
        

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.__str__()