# BFS AGENT

initial_state = [1,1,1,0,2,2,2]
goal_state = [2,2,2,0,1,1,1]


class node:
    
    def __init__(self, state, parent, action, path_cost):
        
        self.state = state
        self.parent = parent 
        self.action = action 
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
        
    def top(self):
        # return node with minimum cost 
        if len(self.list_nodes) == 0:
            return "NotFound"
        my_node = self.list_nodes[0]
        cost = my_node.path_cost 
        for nod in self.list_nodes:
            s,p,a,pt = nod
            if pt<cost:
                my_node = nod 
        return my_node 
    
    def is_empty(self):
        if len(self.list_nodes) == 0:
            return True 
        return False 
    
    def add(self,nod):
        self.list_nodes.append(nod)
        

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
    
def actions(current_state):
    # agent asked for all next possible states
    possible_states = []
    i = current_state.index(0)
    if i ==0:
        # first positon
        if current_state[i+1] == 2:
            # 2 0 ----
            possible_states.append(pick_R1(current_state,i))
        if current_state[i+2] == 2:
            # 2 - 0 ---
            possible_states.append(pick_R2(current_state,i))
    elif i == 1:
        if current_state[i-1] == 1:
            #0 1 -- -
            possible_states.append(pick_L1(current_state,i))
        # first positon
        if current_state[i+1] == 2:
            # 2 0 ----
            possible_states.append(pick_R1(current_state,i))
        if current_state[i+2] == 2:
            # 2 - 0 ---
            possible_states.append(pick_R2(current_state,i))
            
    elif i >= 2 and i< len(current_state)-2:
        # has both left and right full
        if current_state[i-2] == 1:
            #
            possible_states.append(pick_L2(current_state,i))
        if current_state[i-1] == 1:
            #0 1 -- -
            possible_states.append(pick_L1(current_state,i))
        # first positon
        if current_state[i+1] == 2:
            # 2 0 ----
            possible_states.append(pick_R1(current_state,i))
        if current_state[i+2] == 2:
            # 2 - 0 ---
            possible_states.append(pick_R2(current_state,i))
            
    elif i == len(current_state)-2:
        if current_state[i+1] == 2:
            #0 1 -- -
            possible_states.append(pick_R1(current_state,i))
        # first positon
        if current_state[i-1] == 1:
            # 2 0 ----
            possible_states.append(pick_L1(current_state,i))
        if current_state[i-2] == 1:
            # 2 - 0 ---
            possible_states.append(pick_L2(current_state,i))       
    elif i == len(current_state)-1:
        # last positon
        if current_state[i-1] == 1:
            # 2 0 ----
            possible_states.append(pick_L1(current_state,i))
        if current_state[i-2] == 1:
            # 2 - 0 ---
            possible_states.append(pick_L2(current_state,i))           
    
    return possible_states 


def is_goal(state,goal_state):
    for i,j in zip(state,goal_state):
        if i != j:
            return False
    return True 


Frontier = [[[1,1,1,0,2,2,2],"",0]]
Visited = []
def isVisited(state):
    if Visited == []:
        return False 
    for i,j,k in Visited:
        if i== state:
            # state is there
            return True
def agent(current_state,goal_state):
    
    if is_goal(current_state,goal_state):
        print("We reached goal")
        return
    else:
        # Exploring this so put it in visited 
        possible_actions = []
        for l,m,n in Frontier:
            possible_actions.append(l)
            
        if possible_actions == []:
            print("We couldn't reach")
            return 
        for st in possible_actions:
            if is_goal(st,goal_state):
                print("We reached goal")
                return 
        # pick one using BFS or DFS 
        possible_actions = list(sorted(possible_actions))
        for st in possible_actions:
            if isVisited(st):
                # it is visited then pass
                continue 
            else:
                # not visited  so explore it 
                # push it in visited list and explore 
                Visited.append([st,current_state,])
                
        print("Picked: ",possible_actions[-1])
        agent(possible_actions[-1],goal_state)
        
print("        ",[1,1,1,0,2,2,2])
agent([1,1,1,0,2,2,2])
        
    
