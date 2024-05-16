#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:09:53 2024

@author: yifeisu
"""

import random

class Agent:
    def __init__(self, world):
        self.world = world
        self.location = None

    def move(self):
        
        new_location = self.world.find_empty()
        if new_location:
            self.world.grid[self.location] = None  
            self.world.grid[new_location] = self  
            self.location = new_location

class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = {(x, y): None for x in range(size[0]) for y in range(size[1])}
        self.agents = [Agent(self) for _ in range(num_agents)]
        self.init_agents()

    def init_agents(self):
       
        for agent in self.agents:
            while True:
                loc = (random.randint(0, self.size[0] - 1), random.randint(0, self.size[1] - 1))
                if self.grid[loc] is None:
                    self.grid[loc] = agent
                    agent.location = loc
                    break

    def find_empty(self):
    
        empty_locations = [loc for loc, occupant in self.grid.items() if occupant is None]
        return random.choice(empty_locations) if empty_locations else None

def simulate():
  
    size = (10, 10) 
    num_agents = 20 
    num_iterations = 10  

    world = World(size, num_agents)

    for _ in range(num_iterations):
        for agent in world.agents:
            agent.move()

if __name__ == "__main__":
    simulate()


#repo:https://github.com/yifeis0810/Week-9-lab