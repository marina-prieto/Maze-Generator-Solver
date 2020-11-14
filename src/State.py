"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavon
    -   Josue Carlos Zenteno Yave
"""

from Cell import Cell


class State:
    ###########################---Attributes---############################
    id_state = tuple()
    value = tuple()
    neighbors = list()
    cell = None
    
    ###########################---Constructor---###########################
    def init(self, id_state, value, neighbors, cell):
        self.id_state = id_state
        self.value = value
        self.neighbors = neighbors
        self.cell = cell
