"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavon
    -   Josue Carlos Zenteno Yave
"""

from queue import PriorityQueue


class Frontier:
    ###########################---Attributes---############################
    q = PriorityQueue()
    list_nodes = list()

    ###########################---Constructor---###########################
    def __init__(self):
        pass

    ###########################---Methods---###############################
    def create_priority_queue(self, nodes):
        for i in range(len(nodes)):
            self.q.put(((nodes[i].value, nodes[i].id_state[0], nodes[i].id_state[1]), nodes[i]))

    def push(self, node):
        self.q.put(((node.value, node.id_state[0], node.id_state[1]), node))

    def pop(self):
        item = self.q.get()
        return item

    def obtain_all_nodes_ordered(self):
        while not self.q.empty():
            item = self.q.get()
            self.list_nodes.append(item[1])
        return self.list_nodes
