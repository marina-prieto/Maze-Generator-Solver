"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavon
    -   Josue Carlos Zenteno Yave
"""
from src.Maze import Maze
from src.JSONManager import JSONManager
from src.ImageManager import ImageManager

from src.Node import Node
from src.Frontier import Frontier
from random import randint

import sys

json_manager = JSONManager()


###########################---Main methods---##############################
def main():
    print_header()
    while True:
        print_menu()


def generate_maze():
    rows, columns = get_rows_columns()
    maze = Maze(int(rows), int(columns))
    maze.generate_wilson()

    JSONManager.generate_maze_json(maze, maze.rows, maze.columns)
    ImageManager.generate_image(maze, maze.rows, maze.columns)

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


def load_problem():
    try:
        json_manager.read_problem_json()
    except KeyError:
        print("The selected JSON file does not follow the correct format, one error was found: ", sys.exc_info())


def test_frontier():
    n = list()
    f = Frontier()
    for x in range(9):
        node = Node(0, 0, (randint(0, 9), randint(0, 9)), (0, 0), "hola", 0, 0, randint(0, 9))
        n.append(node)

    f.create_priority_queue(n)
    listo = f.obtain_all_nodes_ordered()
    for x in listo:
        print("Value:" + str(x.value) + " Row:" + str(x.id_state[0]) + " Column:" + str(x.id_state[1]))


##########################---Auxiliary methods---##########################
def print_header():
    print("Hi! Thanks for using our A-Maze-ing Generator.")


def print_menu():
    option = input("\nFeel free to choose an option:"
                   "\n\t[1] Generate a Maze"
                   "\n\t[2] Load a Maze"
                   "\n\t[3] Generate a Problem"
                   "\n\t[4] Load a Problem"
                   "\n\t[5] Frontier TEST"
                   "\n\t[6] Exit\n")
    if option == "1":
        generate_maze()
    elif option == "2":
        load_maze()
    elif option == "3":
        generate_problem()
    elif option == "4":
        load_problem()
    elif option == "5":
        test_frontier()
    elif option == "6":
        sys.exit()
    else:
        print("Please, choose a valid option")


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
