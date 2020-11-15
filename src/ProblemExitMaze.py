"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavon
    -   Josue Carlos Zenteno Yave
"""
from Node import Node
from Maze import Maze
from State import State
from Frontier import Frontier
from TextManager import TextManager
from JSONManager import JSONManager
from ImageManager import ImageManager

class ProblemExitMaze:
    ###########################---Attributes---############################
    id_counter = 1
    ###########################---Constructor---###########################
    def __init__(self):
        pass

    ###########################---Main Methods---##########################
    def solve_problem(self, problem, strategy):
        self.id_counter = 1
        goal_node, final_fringe, final_closed = self.search_algorithm(problem, strategy)
        self.build_solution(goal_node, final_fringe, final_closed, problem[2], strategy)
    
    def search_algorithm(self, problem, strategy):
        # We use the Graph Search Pseudocode
        fringe = Frontier()
        closed = list()
        initial_node = self.generate_initial_node(problem, strategy)

        fringe.push(initial_node)

        while True:
            if fringe.pqueue.empty():
                print("There is no solution")
                break
            
            node = fringe.pop()
            if self.goal_test(problem, node.state):
                return node, fringe, closed

            if not (node.state.id_state in closed):
                closed.append(node.state.id_state)
                fringe.push_all(self.expand(node, problem, strategy))

    def expand(self,node, problem, strategy):
        # We use the Expand Pseudocode
        expanded_nodes = list()
        for succesors in self.successor_function(node,problem):
            temp_node = Node(
                self.id_counter,
                node.cost + succesors[2] + problem[2].body[succesors[1][0]][succesors[1][1]].value,
                State((succesors[1][0], succesors[1][1]), (succesors[1][0], succesors[1][1]), None, problem[2].body[succesors[1][0]][succesors[1][1]]),
                node,
                succesors[0],
                node.depth + 1,
                None,
                None
                )
            temp_node.heuristic = self.calc_heuristic(temp_node, problem)
            temp_node.value = self.calc_value_strategy(temp_node, strategy)
            expanded_nodes.append(temp_node)
            self.id_counter += 1
        if temp_node.depth > 1000000:
            self.depth_limit_reached()
        else:
            return expanded_nodes
    
    def build_solution(self, goal_node, final_fringe, final_closed, maze, strategy):
        # We go backwards from the goal state to the beginning state
        solution = self.get_parents(goal_node)
        
        # We create an ImageManager to draw the solution
        image_manager = ImageManager()
        image_manager.draw_solution(solution, final_fringe, final_closed, maze, strategy)
        
        # We create a TextManager to generate the corresponding txt file
        text_manager = TextManager()
        text_manager.generate_txt_solution(solution, maze.rows, maze.columns, strategy)

    #########################---Auxiliary Methods---#######################
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

    def generate_initial_node(self, problem, strategy):
        # We create the initial node 
        initial_node = Node(0,0,self.get_initial_state(problem),None,None,0,None,None)
        initial_node.heuristic = self.calc_heuristic(initial_node, problem)
        initial_node.value = self.calc_value_strategy(initial_node, strategy)
        return initial_node

    @staticmethod
    def get_initial_state(problem):
        return State(problem[0],problem[0],None,problem[2].body[problem[0][0]][problem[0][1]])

    @staticmethod
    def goal_test(problem, state):
        if state.id_state == problem[1]:
            return True
        else:
            return False

    @staticmethod
    def get_parents(goal_node):
        solution = list()
        temp_node = goal_node
        while temp_node.parent != None:
            solution.append(temp_node)
            temp_node = temp_node.parent
        solution.append(temp_node)
        return solution

    @staticmethod
    def calc_heuristic(node, problem):
        return (abs(node.state.id_state[0]-problem[1][0]) + abs(node.state.id_state[1]-problem[1][1]))

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
    def depth_limit_reached():
        print("Depth limit bound reached. Depth greater than 1.000.000")
