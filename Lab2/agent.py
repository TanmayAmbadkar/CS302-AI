from env import Environment
from priority_queue import *
import numpy as np
from time import time

class Agent:
    
    def __init__(self, env, heuristic):
        self.frontier = PriorityQueue()
        self.explored = dict()
        self.start_state = env.get_start_state()
        self.goal_state = env.get_goal_state()
        self.env = env
        self.goal_node = None
        self.heuristic = heuristic
    
    def run(self):
        init_node = Node(parent = None, state = self.start_state, pcost = 0, hcost = 0)
        self.frontier.push(init_node)
        epoch = 0
        start = time()
        while not self.frontier.is_empty():

            curr_node = self.frontier.pop()
            next_states = self.env.get_next_states(curr_node.state)

            if hash(curr_node) in self.explored:
                continue
                
            self.explored[hash(curr_node)] = curr_node

            if self.env.reached_goal(curr_node.state):
                print("Reached goal!")
                self.goal_node = curr_node
                break
            goal_state = self.env.get_goal_state()

            l = []
            for state in next_states:

                hcost = self.heuristic(state[0])
                node = Node(parent=curr_node, state=state[0], pcost=curr_node.pcost+1, hcost=hcost, action=state[1])
                self.frontier.push(node)
            epoch+=1
            if epoch%500 == 0:
                print(epoch, curr_node.cost)
        
        end = time()
        print(epoch)
        print(end - start)
    
    def print_nodes(self):
        
        node = self.goal_node
        l = []
        while node is not None:
            l.append(node)
            node = node.parent

        step = 1
        for node in l[::-1]:
            print("Step: ",step)
            print(node.action)
            #print(node)
            step+=1

        
    