"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavon
    -   Josue Carlos Zenteno Yave
"""

from State import State
from JSONManager import JSONManager
from ImageManager import ImageManager
from Maze import Maze
from Frontier import Frontier
from Node import Node
from TextManager import TextManager

class ProblemExitMaze:
    ###########################---Constructor---###########################
    def __init__(self):
        pass

    ###########################---Main Methods---##########################
    def solve_problem(self, problem, strategy):
        goal_node, final_fringe, final_closed = self.search_algorithm(problem, strategy)
        self.build_solution(goal_node, final_fringe, final_closed, problem[2])
    
    def search_algorithm(self, problem, strategy):
        fringe = Frontier()
        closed = list()
        initial_node = Node(0,0,self.get_initial_state(problem),None,None,0,None,None)
        initial_node.heuristic = self.get_heuristic(initial_node, problem)
        initial_node.value = self.calc_value_strategy(initial_node, strategy)

        fringe.push(initial_node)

        while True:
            if fringe.pqueue.empty():
                print("There is no solution")
                break
            
            node = fringe.pop()
            if self.goal_test(problem, node.state):
                return node, fringe, closed

            if not (node.state in closed):
                closed.append(node.state)
                fringe.push_all(self.expand(node, problem, strategy))
    
    def build_solution(self, goal_node, final_fringe, final_closed, maze):
        image_manager = ImageManager()
        text_manager = TextManager()

        solution = self.get_parents(goal_node)
        image_manager.draw_solution(solution, final_fringe, final_closed, maze)
        text_manager.generate_txt_solution(solution, maze.rows, maze.columns)

    @staticmethod
    def get_parents(goal_node):
        solution = list()
        temp_node = goal_node
        while temp_node.parent != None:
            solution.append(temp_node)
            temp_node = temp_node.parent
        return solution

    @staticmethod
    def get_initial_state(problem):
        return State(problem[0],problem[0],None,problem[2].body[problem[0][0]][problem[0][1]])

    @staticmethod
    def successor_function(node, problem):
        successors_list = list()
        identifier = node.state.id_state

        if problem[2].body[identifier[0]][identifier[1]].NESO[0]:
            new_cell = (identifier[0] - 1, identifier[1])
            position = ("N", new_cell, 1)
            successors_list.append(position)

        if problem[2].body[identifier[0]][identifier[1]].NESO[1]:
            new_cell = (identifier[0], identifier[1] + 1)
            position = ("E", new_cell, 1)
            successors_list.append(position)

        if problem[2].body[identifier[0]][identifier[1]].NESO[2]:
            new_cell = (identifier[0] + 1, identifier[1])
            position = ("S", new_cell, 1)
            successors_list.append(position)

        if problem[2].body[identifier[0]][identifier[1]].NESO[3]:
            new_cell = (identifier[0], identifier[1] - 1)
            position = ("O", new_cell, 1)
            successors_list.append(position)

        node.state.neighbors = successors_list
        
        return successors_list

    def expand(self,node, problem, strategy):
        expanded_nodes = list()
        for succesors in self.successor_function(node,problem):
            temp_node = Node(
                node.id_node +1,
                node.cost + succesors[2] + problem[2].body[succesors[1][0]][succesors[1][1]],
                State((succesors[1][0], succesors[1][1]), (succesors[1][0], succesors[1][1]), None, problem[2].body[succesors[1][0]][succesors[1][1]]),
                node,
                succesors[0],
                node.depth + 1,
                self.get_heuristic(node, problem),
                self.calc_value_strategy(node, strategy)
                )
            expanded_nodes.append(temp_node)
        return expanded_nodes

    @staticmethod
    def calc_value_strategy(node, strategy):
        if strategy == "BREADTH":
            return node.depth
        if strategy == "DEPTH":
            return 1/(node.depth+1)
        if strategy == "UNIFORM":
            return node.cost
        if strategy == "GREEDY":
            return node.heuristic
        if strategy == "A":
            return node.cost + node.heuristic

    @staticmethod
    def get_heuristic(node, problem):
        return (abs(node.state.id_state[0]-problem[1][0]) + abs(node.state.id_state[1]-problem[1][1]))

    @staticmethod
    def goal_test(problem, state):
        if state.id_state == problem[1]:
            return True
        else:
            return False
