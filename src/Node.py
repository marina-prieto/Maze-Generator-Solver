"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavon
    -   Josue Carlos Zenteno Yave
"""
from State import State


class Node:
    ###########################---Attributes---############################
    id_node = int()
    cost = float()
    state = None
    parent = None
    action = str()
    depth = int()
    heuristic = int()
    value = float()

    ###########################---Constructor---###########################
    def __init__(self, id_node, cost, state, parent, action, depth, heuristic, value):
        self.id_node = id_node
        self.cost = cost
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.heuristic = heuristic
        self.value = value

    def toString(self):
        return "["+str(self.id_node)+"],["+str(self.cost)+",("+str(self.state.id_state[0])+","+str(self.state.id_state[1])+"),"+str(self.parent.id_node)+","+self.action+","+str(self.depth)+","+str(self.heuristic)+","+str(self.value)+"]"