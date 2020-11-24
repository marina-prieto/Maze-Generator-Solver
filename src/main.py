"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavon
    -   Josue Carlos Zenteno Yave
"""
import sys
from Node import Node
from Maze import Maze
from art import tprint
from random import randint
from Frontier import Frontier
from JSONManager import JSONManager
from ImageManager import ImageManager
from ProblemExitMaze import ProblemExitMaze

##############################---Global---#################################
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
    except Exception:
        print("Error at loading (We expected a valid JSON file)")


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
        problem[2].body.clear()
    except Exception:
        print("Error at loading (We expected a valid JSON file)")


##########################---Auxiliary methods---##########################
def print_header():
    print("\n\n")
    tprint("A-Maze-Ing",font = "larry3d")


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
    while True: 
        rows = input("Introduce the number of Rows: ")
        columns = input("Introduce the number of Columns: ")
        if rows.isdigit() and columns.isdigit():
            if int(rows) > 1  and int(columns) > 1:
                break
            else:
                print("\nInvalid size, the minimum size for a maze is <rows> = 2 and <columns> = 2\n")
        else:
            print("\nPlease introduce a valid size (<number>, <number>) \n")
    return rows, columns


################################--- Main---################################
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
