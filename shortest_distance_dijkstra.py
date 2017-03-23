# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 00:10:24 2017

@author: Demetris
"""
nodes = {}
nodes['town0'] = [('town2',3),('town3',8)]
nodes['town2'] = [('town0',3),('town3',4),('town1',2)]
nodes['town3'] = [('town0',8),('town2',4),('town4',3)]
nodes['town4'] = [('town1',14),('town3',3)]
nodes['town1'] = [('town5',14),('town4',14),('town2',2)]
nodes['town5'] = [('town1',14)]

def dijkstra(nodes, current_node, target, unvisited = [], distances = {}, first_time = True):
    
    #initialize unvisited list and distances dictionary. 
    #for the distances dictionary, all the stations have initial distance infinity except for the initial node
    if first_time:
        big_number = 2e10
        initial_node = current_node
        
        for key in nodes:
            unvisited.append(key)
            distances[key] = big_number
        distances[initial_node] = 0
                    
    if target in unvisited:
        #check all the neighbours of the current node and update the shortest distance to each node found so far
        for town, distance in nodes[current_node]:
            tentative_distance = distance + distances[current_node]
            if tentative_distance < distances[town]:
                distances[town]=tentative_distance
        
        unvisited.remove(current_node)
        
        #this stage finds the next node to be visited. It has to be the unvisited node with the smallest distance so far
        check = distances.copy()
        for i in range(len(distances)):
            
            #the next 3 lines simply get the node with the smallest distance in the check dictionary
            min_value = min(check.values())
            result = [key for key, value in distances.items() if value == min_value]
            result = result[0]
        
            if result in unvisited:
                current_node = result
                break
            else:
                check.pop(result)
        
        #here the algorithm has finished one cycle, and it uses recursion to repeat the process
        return dijkstra(nodes, current_node, target, unvisited, distances, False)
    else:
        #if the target node has been visited, the algorithm is finished
        return distances[target] #break out of recursion loop
    
print(dijkstra(nodes,'town0', 'town5'))