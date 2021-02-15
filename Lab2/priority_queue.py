import numpy as np

class Node:
    def __init__(self, parent, state, pcost, hcost, action=None):
        
        self.parent = parent
        self.state = state
        self.action = action
        self.pcost = pcost
        self.hcost = hcost
        self.cost = pcost + hcost
    
    def __hash__(self):
        
        return hash(str(self.state.flatten()))
    
    def __str__(self):
        return str(self.state)
    
    def __eq__(self, other):
        
        return hash(''.join(self.state.flatten())) == hash(''.join(other.state.flatten())) 
    
    def __ne__(self, other):
        return hash(''.join(self.state.flatten())) != hash(''.join(other.state.flatten()))


class PriorityQueue():
    
    def __init__(self):
        self.queue = []
        self.hashes = {}
        
    def push(self, node):
        if hash(node) not in self.hashes:
            self.hashes[hash(node)] = 1
            self.queue.append(node)
    
    def pop(self):
        
        next_state = None
        state_cost = 10**18
        index = -1
        
        for i in range(len(self.queue)):
            
            if self.queue[i].cost<state_cost:
                state_cost = self.queue[i].cost
                index = i
        
        return self.queue.pop(index)
    
    def is_empty(self):
        
        return len(self.queue)==0
    
    def __str__(self):
        l = []
        for i in self.queue:
            l.append(i.state)
        
        return str(l)
    
    def __len__(self):
        return len(self.queue)
            