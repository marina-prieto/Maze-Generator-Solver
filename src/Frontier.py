"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavon
    -   Josue Carlos Zenteno Yave
"""

from queue import PriorityQueue


class Frontier:
    ###########################---Attributes---############################
    pqueue = PriorityQueue()
    list_nodes = list()

    ###########################---Constructor---###########################
    def __init__(self):
        pass

    ###########################---Methods---###############################
    def push(self, node):
        self.pqueue.put(((node.value, node.state.id_state[0], node.state.id_state[1]), node))

    def pop(self):
        item = self.pqueue.get()
        return item[1]

    def push_all(self, nodes):
        for i in range(len(nodes)):
            self.pqueue.put(((nodes[i].value, nodes[i].state.id_state[0], nodes[i].state.id_state[1]), nodes[i]))
    
    def pop_all(self):
        while not self.pqueue.empty():
            item = self.pqueue.get()
            self.list_nodes.append(item[1])
        return self.list_nodes
