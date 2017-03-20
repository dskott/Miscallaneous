# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:41:38 2017

@author: Demetris
"""
'''
This submodule contains functions that find out whether a circle of any finite radius exists,
in which a robot can move by following an infinite loop of a set of commands.
i.e.  the movements of the robot should constrain it in a circle.

The commands are given by an array called 'commands', in which can be contained
more than one strings of commands. Each string consists of one or more of these 3 letters:
-'G' (means go forward 1 unit)
-'R' (means turn right)
-'L' (means turn left)

So for example if the string is 'GLLR', then the robot goes forward, turns left,
turns left, turns right.


'''

import numpy as np

def doesCricleExist(commands):
    d = np.array([0,1])
    p = np.array([0,0])
    result = []
    
    #unpack commands array
    for command in commands:
        position, direction = analyze_movement(p,d, command)
        #the robot's movement is bounded only if it returns to its initial position after completing the string
        #or if it lands to any other position and is direction is not (0,1)
        if np.array_equal(position,[0,0]) or not (np.array_equal(direction,[0,1])):
            result.append(('yes',position,direction))
        else:
            result.append(('no',position,direction))
    
        
    return result
        
def analyze_movement(p,d, command):
    'gets a string, the initial position and direction of the robot and returns its final position and direction'
    for c in command:
        if c == 'G':
            p = p+d
        elif c == 'L':
            d = np.array([-d[1], d[0]])
        elif c== 'R':
            d = np.array([d[1], -d[0]])
        else:
            raise ValueError('wrong character')
            
    return p,d

#print(get_direction((0,-1),'L'))  
a = ['GGRRGLLGL', 'GLLRGRGRGL','GG','GGLLLL'] 
print(doesCricleExist(a))