"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavon
    -   Josue Carlos Zenteno Yave
"""
from Maze import Maze
from JSONManager import JSONManager
from ImageManager import ImageManager

from Node import Node
from Frontier import Frontier
from random import randint
from ProblemExitMaze import ProblemExitMaze

import sys

json_manager = JSONManager()
image_manager = ImageManager()
problem_solver = ProblemExitMaze()

###########################---Main methods---##############################
def main():
    print_header()
    while True:
        print_menu()


def generate_maze():
    rows, columns = get_rows_columns()
    maze = Maze(int(rows), int(columns))
    maze.generate_wilson()

    json_manager.generate_maze_json(maze, maze.rows, maze.columns)
    image_manager.generate_image(maze, maze.rows, maze.columns)

    maze.body.clear()


def load_maze():
    json_manager.ask_for_file()
    try:
        json_manager.read_json()
        json_manager.generate_image()
    except KeyError:
        print("The selected JSON file does not follow the correct format, one error was found: ", sys.exc_info())


def generate_problem():
    rows, columns = get_rows_columns()
    maze = Maze(int(rows), int(columns))
    maze.generate_wilson()

    json_manager.generate_maze_json(maze, maze.rows, maze.columns)
    json_manager.generate_problem_json(maze.rows, maze.columns)

    maze.body.clear()


def solve_problem():
    try:
        problem = json_manager.read_problem_json()
        strategy = ask_for_strategy()
        problem_solver.solve_problem(problem, strategy)

    except KeyError:
        print("The selected JSON file does not follow the correct format, one error was found: ", sys.exc_info())


##########################---Auxiliary methods---##########################
def print_header():
    print("Hi! Thanks for using our A-Maze-ing Generator.")


def print_menu():
    option = input("\nFeel free to choose an option:"
                   "\n\t[1] Generate a Maze"
                   "\n\t[2] Load a Maze"
                   "\n\t[3] Generate a Problem"
                   "\n\t[4] Solve Problem"
                   "\n\t[5] Exit\n")
    if option == "1":
        generate_maze()
    elif option == "2":
        load_maze()
    elif option == "3":
        generate_problem()
    elif option == "4":
        solve_problem()
    elif option == "5":
        sys.exit()
    else:
        print("Please, choose a valid option")

def ask_for_strategy():
    strategy = input("\nFeel free to choose an option:"
                    "\n\t[1] BREADTH"
                    "\n\t[2] DEPTH"
                    "\n\t[3] UNIFORM"
                    "\n\t[4] GREDDY"
                    "\n\t[5] A\n")

    if strategy == "1":
        return "BREADTH"
    if strategy == "2":
        return "DEPTH"
    if strategy == "3":
        return "UNIFORM"
    if strategy == "4":
        return "GREEDY"
    if strategy == "5":
        return "A"

def get_rows_columns():
    rows = input("Introduce the number of Rows: ")
    columns = input("Introduce the number of Columns: ")
    return rows, columns


################################--- Main---################################
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
