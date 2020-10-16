"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavón
    -   Josue Carlos Zenteno Yave
"""
from random import randint
from src.Cell import Cell
from PIL import Image, ImageDraw
import json


class Maze:
    ############################---Attributes---###########################
    rows, columns = int(), int()
    body, frontier, directions, pointer = list(), list(), list(), list()

    ###########################---Constructor---###########################
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.build_body(rows, columns)

    ###########################---Main Methods---##########################
    def generate_wilson(self):

        first_part_done, second_part_done, everything_visited = False, False, False

        self.get_initial_random_cells()

        while not first_part_done:
            first_part_done = self.find_path("Main_path")

        self.free_resources()

        #while not second_part_done or not everything_visited:
        self.get_random_cell()
        while not everything_visited:
            if self.find_path("Path"):
                if not self.look_for_visited():
                    self.get_random_cell()
            everything_visited = self.look_for_visited()

    def generate_image(self):
        # Creating a picture of size <xy>, which depends on the size of a cell (20x20 px) and the number of rows and columns
        maze_pic = Image.new(mode="1", size=((self.columns * 20) + 10, (self.rows * 20) + 10), color=1)
        maze_pic_draw = ImageDraw.Draw(maze_pic)

        # Initialize a pointer in (5,5) (x,y)
        pointer = [5, 5]
        for i in range(self.rows):
            #We don't want to move the pointer if we are in the first row neither in the first column
            if i != 0:
                pointer[0] = 5
                pointer[1] += 20
            for j in range(self.columns):
                if j != 0:
                    pointer[0] += 20
                if not self.body[i][j].NESO[0]:
                    maze_pic_draw.line((pointer[0], pointer[1], pointer[0] + 20, pointer[1]), width=3, fill=0)
                if not self.body[i][j].NESO[1]:
                    maze_pic_draw.line((pointer[0] + 20, pointer[1], pointer[0] + 20, pointer[1] + 20), width=3, fill=0)
                if not self.body[i][j].NESO[2]:
                    maze_pic_draw.line((pointer[0], pointer[1] + 20, pointer[0] + 20, pointer[1] + 20), width=3, fill=0)
                if not self.body[i][j].NESO[3]:
                    maze_pic_draw.line((pointer[0], pointer[1], pointer[0], pointer[1] + 20), width=3, fill=0)

        maze_pic.save(str(self.rows) + "x" + str(self.columns) + ".jpg")

    def generate_json(self):
        #Creating a Dictionary for the Maze class
        maze_dict = {"rows": self.rows, "cols": self.columns, "max_n": 4, "mov": [[-1, 0], [0, 1], [1, 0], [0, -1]],
                     "id_mov": ["N", "E", "S", "O"], "cells": {}}

        #Filling the Cells key for the Maze dictionary with auxiliary dictionaries (one per cell per row)
        for i in range(self.rows):
            for j in range(self.columns):
                cell_dict_aux = {"(" + str(i) + "," + str(j) + ")": {"value": 0, "neighbours": [self.body[i][j].NESO[0],
                                                                                                self.body[i][j].NESO[1],
                                                                                                self.body[i][j].NESO[2],
                                                                                                self.body[i][j].NESO[3]]}}
                maze_dict["cells"].update(cell_dict_aux)

        #Saving the JSON file
        with open(str(self.rows) + "x" + str(self.columns) + ".json", "w") as outfile:
            json.dump(maze_dict, outfile, indent=4)

    #################---Wilson's Auxiliary Methods---######################
    def get_initial_random_cells(self):
        rnd_final, rnd_beginning = tuple(), tuple()
        different = False
        #Selecting random Cells
        while not different:
            rnd_final, rnd_beginning = (randint(0, self.rows-1), randint(0, self.columns-1)), (randint(0, self.rows-1), randint(0, self.columns-1))
            if rnd_final != rnd_beginning:
                different = True
        #Setting the corresponding values in order to initiate the algorithm
        self.body[rnd_final[0]][rnd_final[1]].final = True
        self.body[rnd_beginning[0]][rnd_beginning[1]].visited = True
        #Introducing the first element to the frontier (which is the beginning cell)
        self.frontier.append(self.body[rnd_beginning[0]][rnd_beginning[1]])

    def find_path(self, kind):
        #Saving the last element of the Frontier (the last cell reached)
        selector = self.frontier[-1]
        #Getting the tuple of (row, column, selected direction) of the cell that we are trying to reach
        next_cell_rcd = selector.get_random_neighbour(self.rows, self.columns)
        #Checking if the cell that we want to access was already visited
        if self.body[next_cell_rcd[0]][next_cell_rcd[1]] in self.frontier:
            if len(self.frontier) > 1:
                found = False
                # Looking for the repeated value pop-ing all the elements in the Frontier until finding the repeated cell in order to avoid loops
                while not found:
                    #Ask if the element that we are looking for is the same as the next element in the frontier
                    if self.frontier[-1] == self.body[next_cell_rcd[0]][next_cell_rcd[1]]:
                        found = True
                    else:
                        #Unvisiting the cell
                        self.body[self.frontier[-1].id[0]][self.frontier[-1].id[1]].visited = False
                        #Unbreaking the wall that the cell broke after
                        self.body[self.frontier[-2].id[0]][self.frontier[-2].id[1]].NESO[self.neso_converter_go(self.directions[-1])] = False
                        #removing both the cell and the direction chosen to reach that cell
                        self.frontier.pop(-1)
                        self.directions.pop(-1)
        else:
            # Adding the last direction chosen to the directions list
            self.directions.append(next_cell_rcd[2])
            # Marking the cell as Visited
            self.body[next_cell_rcd[0]][next_cell_rcd[1]].visited = True
            # Adding the last cell chosen to the Frontier list
            self.frontier.append(self.body[next_cell_rcd[0]][next_cell_rcd[1]])
            # Erasing the wall, updating the values of the NESO List of the cell
            self.body[self.frontier[-2].id[0]][self.frontier[-2].id[1]].NESO[self.neso_converter_go(next_cell_rcd[2])] = True

            #Check if the cell that we added is the final cell (or a visited one if we are completing the maze)
            if kind == "Main_path":
                if self.body[next_cell_rcd[0]][next_cell_rcd[1]].final:
                    self.dig()
                    return True
            elif kind == "Path":
                if self.body[next_cell_rcd[0]][next_cell_rcd[1]].visited and self.body[next_cell_rcd[0]][next_cell_rcd[1]].final:
                    self.dig()
                    return True
        return False

    def get_random_cell(self):
        rnd_beginning = tuple()
        valid = False
        #Selecting random Cells
        while not valid:
            rnd_beginning = (randint(0, self.rows-1), randint(0, self.columns-1))
            if not self.body[rnd_beginning[0]][rnd_beginning[1]].final:
                valid = True
        #Setting the corresponding values in order to initiate the algorithm
        self.body[rnd_beginning[0]][rnd_beginning[1]].visited = True
        #Introducing the first element to the frontier (which is the beginning cell)
        self.frontier.append(self.body[rnd_beginning[0]][rnd_beginning[1]])

    def dig(self):
        length = len(self.frontier)
        for i in range(length):
            self.body[self.frontier[-1].id[0]][self.frontier[-1].id[1]].final = True
            if len(self.directions) != 0:
                self.body[self.frontier[-1].id[0]][self.frontier[-1].id[1]].NESO[self.neso_converter_back(self.directions[-1])] = True
            self.frontier.pop(-1)
            if len(self.directions) != 0:
                self.directions.pop(-1)

    def look_for_visited(self):
        for i in range(self.rows):
            for j in range(len(self.body[0])):
                if not self.body[i][j].final:
                    return False
        return True

    def free_resources(self):
        self.frontier.clear()
        self.directions.clear()

    def build_body(self, rows, columns):
        for i in range(rows):
            self.body.append(list())
            for j in range(columns):
                self.body[i].append(Cell((i, j)))

    @staticmethod
    def neso_converter_go(selection):
        if selection == "N":
            return 0
        elif selection == "E":
            return 1
        elif selection == "S":
            return 2
        elif selection == "O":
            return 3

    @staticmethod
    def neso_converter_back(selection):
        if selection == "N":
            return 2
        elif selection == "E":
            return 3
        elif selection == "S":
            return 0
        elif selection == "O":
            return 1
