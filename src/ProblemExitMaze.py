"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavon
    -   Josue Carlos Zenteno Yave
"""

from State import State
from JSONManager import JSONManager
from Maze import Maze


class ProblemExitMaze:
    ###########################---Constructor---###########################
    def init(self):
        pass

    ###########################---Main Methods---##########################
    @staticmethod
    def problem_exit_maze():
        pass

    def get_initial_state(self):
        states = self.get_info()
        return states[0]

    @staticmethod
    def successor_function(maze, state):
        successors_list = list()
        identifier = state.id

        if maze.body[identifier[0]][identifier[1]].NESO[0]:
            new_cell = (identifier[0] - 1, identifier[1])
            position = ("N", new_cell, 1)
            successors_list.append(position)
        if maze.body[identifier[0]][identifier[1]].NESO[1]:
            new_cell = (identifier[0], identifier[1] + 1)
            position = ("E", new_cell, 1)
            successors_list.append(position)
        if maze.body[identifier[0]][identifier[1]].NESO[2]:
            new_cell = (identifier[0] + 1, identifier[1])
            position = ("S", new_cell, 1)
            successors_list.append(position)
        if maze.body[identifier[0]][identifier[1]].NESO[3]:
            new_cell = (identifier[0], identifier[1] - 1)
            position = ("O", new_cell, 1)
            successors_list.append(position)

        return successors_list

    def goal_test(self, state):
        goal_completed = False
        states = self.get_info
        goal = states[1]

        if state.id == goal:
            goal_completed = True

        return goal_completed

    @staticmethod
    def get_info():
        json_manager = JSONManager
        states = json_manager.read_problem_json()
        return states
