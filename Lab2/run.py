import numpy as np
from agent import Agent
from env import Environment

def heuristic1(curr_state):
    cost = 0
    for i in range(7):
        for j in range(7):
            if curr_state[i][j]==1:
                cost += abs(i-3)+abs(j-3)
    
    return cost
   
def heuristic2(curr_state):
    cost = 0
    for i in range(7):
        for j in range(7):
            if curr_state[i][j]==1:
                cost += 2**(max(abs(i-3),abs(j-3)))
    
    return cost

agent = Agent(Environment(), heuristic2)

agent.run()
agent.print_nodes()