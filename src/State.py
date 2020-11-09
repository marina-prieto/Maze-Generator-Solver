"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavon
    -   Josue Carlos Zenteno Yave
"""

from src.Cell import Cell


class State:
    ###########################---Attributes---############################
    c = Cell
    neighbours = list()
    value = int
    id = tuple()

    ###########################---Constructor---###########################
    def init(self, cell, neighbours, value, id):
        self.c = cell
        self.neighbours = neighbours
        self.value = value
        self.id = id
