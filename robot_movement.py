# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:46:32 2017

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
def  doesCircleExist(commands):
    answer = []
    pos = (0,0)
    initial_pos = (0,0)
    initial_state = ((0,0),0)
    final_state = ((0,0),0)
  
    #check each individual string
    for command in commands:
        #if the command doesn't contain G, then the robot doesn't move, so it doesn't get out of any circle
        if 'G' in command:
            
            #unpack command string
            command_list = tuple(command)
            
            final_state = analyze_movement(initial_state, command_list)
            
            print(final_state)
            #if the robot returns to its initial position after following the commands, then it is constrained
            if final_state[0] == initial_pos:
                answer.append('YES')
            else:
                '''
                current_state = final_state
                for i in range(10):
                    final_state = get_new_state(initial_state, final_state)
                    if final_state[0] == initial_pos:
                        answer.append('YES')
                        break
                '''
                if get_new_state(initial_state, final_state)[0] == initial_pos:
                    answer.append('YES')
                else:
                    answer.append('NO')
        else:
            answer.append('YES')
            
    return answer
        
def decipher_command(string):
    'gets the individual command and returns how it affects movement and orientation'
    if string == 'G':
        return True, 0
    elif string == 'L':
        return False, -90
    elif string == 'R':
        return False, 90
        
def get_orientation(orientation):
    'this function constrains the orientation to only have these values: 0,90,180,270'
    if orientation == -90:
        return 270
    elif orientation == -180:
        return 180
    elif orientation == -180:
        return 180
    elif orientation == -270:
        return 90
    elif orientation == -360:
        return 0
    elif orientation == 360:
        return 0
    elif orientation == 450:
        return 90
    elif orientation == 540:
        return 180
    elif orientation == 630:
        return 270
    elif orientation == 720:
        return 0
    else:
        return orientation
        
def get_pos(pos, orientation):
    'gets the position and orientation of the robot and returns its new position'
    if orientation == 0:
        return pos[0], pos[1]+1
    elif orientation == 90:
        return pos[0]+1, pos[1] 
    elif orientation == 180:
        return pos[0], pos[1]-1
    elif orientation == 270:
        return pos[0]-1, pos[1]
        
def analyze_movement(initial_state, command_list):
    'gets the initial state of the robot and the command list, and returns its final state'
    orientation = initial_state[1]
    pos = initial_state[0]
    
    for comm in command_list:
        direction, orient = decipher_command(comm)
        orientation += orient
        orientation = get_orientation(orientation)
                
        #check first if the robot actually moves for this comm. if it moves update its position
        if direction:
            pos = get_pos(pos, orientation) 
    return pos, orientation
    
def get_new_state(initial_state, final_state):
    '''
    gets the initial and final state of the robot, after it has followed the command once,
    and returns its new state if it follows the string again.
    '''
    vertical = final_state[0][1]-initial_state[0][1]
    horizontal = final_state[0][0]-initial_state[0][0]
    difference_orient = final_state[1]-initial_state[1]
    new_axis = get_orientation(difference_orient)
    new_orient = get_orientation(new_axis + final_state[1]) 
    
    if new_axis == 0:
        return (final_state[0][0] + horizontal,final_state[0][1] + vertical), new_orient
    elif new_axis == 90:
        return (final_state[0][0] + vertical, final_state[0][1] - horizontal), new_orient
    elif new_axis == 180:
        return (final_state[0][0] - horizontal, final_state[0][1] - vertical), new_orient
    elif new_axis == 270:
        return (final_state[0][0] - vertical, final_state[0][1] + horizontal), new_orient
    else: 
        raise ValueError('invalid orientation')
        
initial_state = ((0,0), 270)
final_state = ((-3,5),180)
#print(get_new_state(initial_state, final_state))
commands = ['GRGLLLLLLGLGRRGGLGGRRRGGLGGL','GLGL','RGRG']
print(doesCircleExist(commands))