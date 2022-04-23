# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:37:44 2022

This file contains all codes about the agents and agents predator (Wolves).
Here, behaviours such as how they move, share with their neighbours, eat, and breed to populate themselves are
included. Properties of each agent is also included in the file.


Version: 1.0.1

@author: 201576424
"""

#import module to be used
import random

#create class Agent
class Agent:
    
    # Class attributes
    Agent_id = 0 # Sheep id
    gender = ["m", "f"] #Sheep gender for breeding
    breed_distance = 1 #Required distance for breeding to take place
    
    # Function definitions 
    def __init__ (self, environment, agents, sheep_pace, gender, colour, x = None, y = None, child=False):  
        """
            Creates an Agent within an environment, with pace, gender, colour, and children
            
            Parameters
            ----------
            environment :  str
                The environment where the agents behave
            agents : str
                List of the agents.
            sheep_pace :  int
                Pace given to the agents before eaten by wolves (default is 5)
            gender : str
                Agents gender (default is 'm' and 'f')
            colour : str
                Various colour given to the agents and their children
            x : int, optional
                x coordinates from webscrapped data
            y : int, optional
                y coordinates from webscrapped data
            child : 
                new agent child created

        """
        if(x == None or y == None):
            self._x = random.randint(0,len(environment))
            self._y = random.randint(0,len(environment[0]))
        else:
            self._x = x
            self._y = y
        self.environment= environment
        self.store= 0
        self.agents= agents
        self.sheep_pace = sheep_pace # Default pace of sheep
        self.gender = gender # gender of the sheep
        self.colour = colour # colour of sheep
        self.id = self.create_new_sheep() #breeding sheep
        self.child = child #new sheep child created
        
    # Creates new sheep (breeding)
    def create_new_sheep(self):
        """
            This creates new agents.
            
            Returns
            -------
            int
                Total number of agents.

        """
        Agent.Agent_id += 1
        return Agent.Agent_id
        
    #this function gets the attribute value of x        
    def get_x(self):
        '''
        Gets the attribute value of x

        Returns
        -------
        str
            x attribute

        '''
        return self._x
    
    #this function sets the attribute value of x     
    def set_x(self, value):
        '''
        Sets the attribute value of x

        Parameters
        ----------
        value : str
            x attribute

        Returns
        -------
        None.

        '''
        self._x = value
    
    x= property(get_x,set_x, "I am the 'x' property")
    
    #this function gets the attribute value of y    
    def get_y(self):
        '''
        Gets attribute value of y

        Returns
        -------
        str
            y attribute

        '''
        return self._y
    
    #this function sets the attribute value of y    
    def set_y(self, value):
        '''
        Sets y attribute

        Parameters
        ----------
        value : str
            y attribute

        Returns
        -------
        None.

        '''
        self._y = value
    
    y= property(get_y,set_y, "I am the 'y' property")
    
    def move(self): 
        """
        This method moves the agents between random positions
        Movement is faster if agents have more resources to share.

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
            
    def eat(self): 
        """
        This makes the agents eat the environment and their eating is controlled.
        If an agent eats at least 100 units, it vomits and empties its bowel (Store) and stops eating.
        
        Returns
        -------
        None.

        """
        
        eat_space = 10 # Amount of unit space to eat
        if self.store >= 100: # If the agent has eaten at least 100 units
                self.environment[self._y][self._x] += self.store # Vomit all units eaten on a particular location
                self.store = 0 # Empty the agents bowel
                return 0
        if self.environment[self._y][self._x] > 0:
            if self.environment[self._y][self._x] >= eat_space:
                self.environment[self._y][self._x] -= eat_space
                self.store += eat_space
                return eat_space
            else:
                self.environment[self._y][self._x] = 0   
                self.store += self.environment[self._y][self._x]
                return self.environment[self._y][self._x]
    
    # Breeding among sheep
    def breed(self):
        """
        This method is for breeding among agents
        Agents must be close enough (2 units proximity) to breed 
        Children cannot breed.

        Returns
        -------
        None.

        """
        for index, agent in enumerate(self.agents):
            # Cannot mate with itself or with a sheep of the same gender
            # Must be close enough (within a proximity of 2 units)
            if(not(self.child) and not(self.gender == agent.gender) and (self.distance_between(agent) <= Agent.breed_distance)):
                i = random.randint(-1, 1)
                # self.agents.append(Agent(self.environment, self.agents, self.sheep_pace, Agent.gender[i % 2], "white"))
                new_child = Agent(self.environment, self.agents, self.sheep_pace, Agent.gender[i], colour="white", child=True)
                self.agents.append(new_child)
                print(f"An agent child is created - {self}")
            # if(distance <= 5):
            #     print(f"This agent is dead: {agent}")
            #     self.agents.pop(index)
            #     break
    
    def share_with_neighbours(self, neighbourhood):
        """
        Neighbourhood distance for sharing among the agents

        Parameters
        ----------
        neighbourhood : int
            Sharing distance among agents

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
        
            This calculates the distance between agents and returns the result.
    
            Parameters
            ----------
            agent: int
            
            Returns
            -------
            int
                Distance between agents.

        """
        return (((agent._x - self._x)**2) + ((agent._y - self._y)**2))**0.5   
    
    #Can you override __str__(self) in the agents, as mentioned in the lecture on classes, 
#so that they display this information information about their location and stores when printed?            
 
    def __str__(self): 
        """
        Shows the location and store for the agents as string

        Returns
        -------
        str
           Agents' location and store
        """
        return f"Location: ({self.x}, {self.y})\tStore: {self.store}"
    
    def __repr__(self):
        """
        Calls the __str__ function by displaying the agents location and store

        Returns
        -------
        str
            agents location and store

        """
        return self.__str__()


#create class Wolf
class Wolf:
    
    # Class variables
    Wolf_id = 0 # Wolf id
    attack_distance = 2
    gender = ["m", "f"]
    child_colour = 'red'
    breed_distance = 1
    
    def __init__ (self, environment, agents, wolves, wolf_pace, gender, colour):  
        """
            Creates wolves within an environment, wolf pace, gender, and colour
            
            Parameters
            ----------
            environment :  str
                The environment where the wolves behave
            agents : str
                List of the agents.
            wolf_pace :  int
                Pace given to the wolves before they eat the agents 
            gender : str
                WOlves gender (default is 'm' and 'f')
            colour : str
                Various colour given to the agents and their children
            
        """
        self._x = random.randint(0,len(environment))
        self._y = random.randint(0,len(environment[0]))
        self.environment= environment
        self.store= 0
        self.agents= agents
        self.wolves= wolves
        self.wolf_pace = wolf_pace
        self.gender = gender # gender of the wolf
        self.colour = colour # colour of wolf
        self.id = self.create_new_wolf()
        
    # Creates new Wolf
    def create_new_wolf(self):
        '''
        Creates a wolf, increases when each new wolf is created.

        Returns
        -------
        int
            Total number of wolves, adult child.

        '''
        Wolf.Wolf_id += 1
        return Wolf.Wolf_id
        
    #this function gets the attribute value of x        
    def get_x(self):
        '''
            Gets the wolves attributes
    
            Returns
            -------
            str
                Wolves attributes.

        '''
        return self._x
    
    #this function sets the attribute value of x     
    def set_x(self, value):
        '''
            Sets the wolves attributes (location and store)
    
            Parameters
            ----------
            value : str
                wolves x attributes.
    
            Returns
            -------
            None.

        '''
        self._x = value
    
    x= property(get_x,set_x, "I am the 'x' property")
    
    #this function gets the attribute value of y    
    def get_y(self):
        '''
            Gets the wolves y attributes
    
            Returns
            -------
            str
                wolves attributes.

        '''
        return self._y
    
    #this function sets the attribute value of y    
    def set_y(self, value):
        '''
            Sets wolves y attribute value
    
            Parameters
            ----------
            value : str
                Wolves attribute value.
    
            Returns
            -------
            None.

        '''
        self._y = value
    
    y= property(get_y,set_y, "I am the 'y' property")
    
    def move(self):#The wolf moves twice as fast as the sheep
        '''
            Determines the Wolves movement, which is faster than the agents so
            they can catch them fast and kill to eat
    
            Returns
            -------
            None.

        '''
        # if (self.store < 50):
        #     #set the movement to be faster if they have more resources
        #     d = 1 #distance of movement for less than 50
        # else:
        #     d = wolf_pace #distance of movement for greater than 50
        
        nrows = len(self.environment)
        ncols = len(self.environment[0])
        d = self.wolf_pace
        if random.random() < 0.5:
            self._x = (self._x + d) % ncols
        else:
            self._x = (self._x - d) % ncols

        if random.random() < 0.5:
            self._y = (self._y + d) % nrows
        else:
            self._y = (self._y- d) % nrows

# can you make it eat what is left?            
    def eat(self): 
        '''
            Wolves eating the agents based on attack distance
    
            Returns
            -------
            None.

        '''
        for index, agent in enumerate(self.agents):
            distance = self.distance_between(agent)
            if(distance <= Wolf.attack_distance):
                print(f"This agent is dead: {agent}")
                self.agents.pop(index)
                Wolf.Wolf_id -= 1
                break;
                
    # Breeding among wolves
    def breed(self):
        '''
            Breeding among wolves, breeding distance of 1 is given to ensure close proximity.
            Cannot mate with itself or with an agent of same gender.
    
            Returns
            -------
            None.

        '''
        for index, wolve in enumerate(self.wolves):
            # Cannot mate with itself or with a sheep of the same gender
            # Must be close enough (within a proximity of 1 unit)
            if(not(self.gender == wolve.gender) and (self.distance_between(wolve) <= Wolf.breed_distance)):
                i = random.randint(-1, 1)
                new_child = Wolf(self.environment, self.agents, self.wolves, self.wolf_pace, Wolf.gender[i % 2], Wolf.child_colour)
                self.wolves.append(new_child)
                print(f"A wolf child is created - {self}")
               
    #function to calculate the distance between wolves 
    def distance_between(self, agent):
        """
        
            This calculates the distance between wolves and returns the result.
    
            Parameters
            ----------
            agent: int
            
            Returns
            -------
            int
                Distance between wolves.


        """
        return (((agent._x - self._x)**2) + ((agent._y - self._y)**2))**0.5   
    
#display this information information about wolves location and stores when printed?            
    def __str__(self): 
        '''
            Displays information about wolves location and store when a wolf child is created
    
            Returns
            -------
            str
                Location for Wolves.

        '''
        return f"Location: ({self.x}, {self.y})\tStore: {self.store}"
    
    def __repr__(self):
        '''
        Calls the __str__ function by displaying the wolves location and store

        Returns
        -------
        str
            wolves location and store

        '''
        return self.__str__()
    
    