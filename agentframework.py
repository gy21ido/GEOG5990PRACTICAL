# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:37:44 2022

@author: IYANULOLUWA
"""

import random

#create class Agent
class Agent:
    def __init__ (self):  
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
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
        # self.environment= environment
        
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
        # nrows = len(self.environment)
        # ncols = len(self.environment[0])
        if random.random() < 0.5:
            self.x = self.x + 1 #% ncols
        else:
            self.x = self.x - 1 #% ncols

        if random.random() < 0.5:
            self.y = self.y + 1 #% nrows
        else:
            self.y = self.y- 1 #% nrows
    
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
        return (((agent.x - self.x)**2) + ((agent.y - self.y)**2))**0.5   