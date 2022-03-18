# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 12:59:31 2022

@author: aman raj
"""

#----------------M C side
initial_state = [3,3,0]
goal_state =    [0,0,1]

def pick_R1(current_state,i):
    temp = current_state.copy()
    temp[i+1] = 0
    temp[i] = 2 
    return temp

def pick_R2(current_state,i):
    temp = current_state.copy()
    temp[i+2] = 0
    temp[i] = 2 
    return temp

def pick_L1(current_state,i):
    temp = current_state.copy()
    temp[i-1] = 0
    temp[i] = 1 
    return temp

def pick_L2(current_state,i):
    temp = current_state.copy()
    temp[i-2] = 0
    temp[i] = 1 
    return temp
 
import numpy as np
   
def actions(current_state):
    a = current_state[0]
    b = current_state[1]
    int_states = []
    in_arr = np.array([[a,b] for i in range(5)]).reshape(5,2)
    move = np.array([[-1,0],[0,-1],[-2,0],[0,-2],[-1,-1]])
    bb = in_arr + move
    cc = np.sum(bb>= 0, axis=1) == 2
    for row in bb[cc]:
        int_states.append(row)
    clean_states = []
    for ro in int_states:
        if list(ro) ==  [0,0]:
            # reached 
            print('current_state              ',(ro[0],ro[1],1))
            return "Found"
        for r in [[3,0],[3,1],[3,2],[3,3],[2,2],[1,1],[0,3],[0,2],[0,1]]:
            if r[0] == ro[0] and r[1] == ro[1]:
                clean_states.append(ro)
    if clean_states == []:
        # not possible to reach 
        return  []
    #---------------------------------------
    final_states = []
    for st in clean_states:
        a = st[0]
        b = st[1]
        in_arr = np.array([[a,b] for i in range(5)]).reshape(5,2)
        move = np.array([[+1,0],[0,+1],[+2,0],[0,+2],[+1,+1]])
        bb = in_arr + move
        cc = np.sum(bb<= 3, axis=1) == 2
        for row in bb[cc]:
            final_states.append(row)
    clean_final_states = []
    for ro in final_states:
        if list(ro) == [0,0]:
            # reached 
            print('reached')
            return []
        for r in [[3,0],[3,1],[3,2],[3,3],[2,2],[1,1],[0,3],[0,2],[0,1]]:
            if r[0] == ro[0] and r[1] == ro[1]:
                clean_final_states.append(tuple(ro))
    #print("clean",clean_final_states)
    if clean_final_states == []:
        # not possible to reach 
        return  []

    return list(set(clean_final_states))


class node:
    
    def __init__(self, state, parent,  path_cost):
        
        self.state = state
        self.parent = parent 
        self.path_cost = path_cost 
        
class Frontier:
    # priority que 
    def __init__(self, root_node):
        self.list_nodes = [root_node]
        
    def pop(self):
        # remove first element 
        if len(self.list_nodes) == 0:
            return "NotFound"
        first = self.list_nodes[0]
        self.list_nodes = self.list_nodes[1:].copy()
        return first 
    def remove(self, nod):
        if nod not in self.list_nodes:
            return "NotFound"
        
        del self.list_nodes[self.list_nodes.index(nod)]
     
    def isbetter(self, nod):
        list_same_state =[]
        for no in self.list_nodes:
            if nod.state == no.state:
                list_same_state.append(no)
        for no in list_same_state:
            if no.path_cost <= nod.path_cost:
                return False 
        return True
        
    def top(self):
        # return node with minimum cost 
        if len(self.list_nodes) == 0:
            return "NotFound"
        my_node = self.list_nodes[0]
        cost = my_node.path_cost 
        for nod in self.list_nodes:
            s = nod.state 
            p = nod.parent
            pt = nod.path_cost
            if pt<cost:
                my_node = nod 
        return my_node 
    
    def is_empty(self):
        if len(self.list_nodes) == 0:
            return True 
        return False 
    
    def add(self,nod):
        self.list_nodes.append(nod)
        
class Visited():
    
    def __init__(self):
        self.visited_list = []
        
    def add(self,nod):
        self.visited_list.append(nod)
        
    def isin(self,st):
        for no in self.visited_list:
            if list(st) == list(no.state) :
                return True 
        return False

def backtrack(my_frontier, my_visited, top_node,home_state):
    # top node is where we reached 
    current_node = top_node
    print(current_node.state)
    while current_node.state != home_state:
        # find next node
        p = current_node.parent
        for no in my_visited.visited_list:
            # got node 
            if no.state == p:
                current_node = no 
        print(current_node.state)
    print("="*40)
        
    

# BestFirstsearch Agent 
def BestFirstSearch_Agent(initial_state, goal_state):
    ## 
    home_state = initial_state.copy()
    #(initial state, None,0)
    parent_node = node(initial_state, None, 0)
    my_frontier = Frontier(parent_node)
    my_visited = Visited()
    
    if initial_state == goal_state:
        # we got 
        return initial_state 
    
    while my_frontier.is_empty() != True:
        # while my frontier is not empty 
        # Best First search 
        top_node = my_frontier.top()
        my_frontier.remove(top_node)
        if top_node.state == goal_state:
            backtrack(my_frontier,my_visited, top_node,home_state)
            return top_node.state 
        # not goal so move it to Visited state and expand it 
        # check whether it is in visited or not 
        if my_visited.isin(top_node.state):
            # so we already visited it 
            continue 
        

        my_visited.add(top_node) # expanded 
        
        print("current_state              ",top_node.state)
        all_possible_actions = actions(top_node.state)
        #print("these are all valid actions",all_possible_actions) 
        if all_possible_actions ==[]:
            print("Not possible")
            return 
        if all_possible_actions == "Found":
            print()
            print("BackTracking: ")
            print((0, 0, 1))
            backtrack(my_frontier,my_visited, top_node,home_state)
            return 
        
        all_possible_actions = [(a,b,0) for a,b in all_possible_actions]
        c = top_node.path_cost
        all_possible_nodes = [node( st,top_node.state , c+1) for st in all_possible_actions]

        clean_nodes =[]
        for no in all_possible_nodes:
            if my_frontier.isbetter(no) and not my_visited.isin(no.state):
                clean_nodes.append(no)
            if my_frontier.isbetter(no):
                # it is better so replace 
                my_frontier.remove(no)
        for no in clean_nodes:
            my_frontier.add(no)
        initial_state = top_node.state
        
    print("Not found")

if __name__ == "__main__": 
    """
    We have considered state as :
        (no of Missionaries on left, no of Cannibal on left , side of boat )
    where side of boat is 0 if it is in left and 1 if it is in right.
    initial state:- (3, 3, 0)
    goal state:-    (0, 0, 1)
    """
    #----------------M C side
    initial_state = [3,3,0]
    goal_state =    [0,0,1]
        
    print(BestFirstSearch_Agent(initial_state, goal_state))