"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavon
    -   Josue Carlos Zenteno Yave
"""
from src.Maze import Maze
from src.JSONReader import JSONReader
import sys


###########################---Main methods---##############################
def main():
    print_header()
    while True:
        print_menu()


def generate_maze():

    rows, columns = get_rows_columns()
    maze = Maze(int(rows), int(columns))

    maze.generate_wilson()
    maze.generate_json()
    maze.generate_image()
    maze.body.clear()


def read_json():
    json_reader = JSONReader()
    json_reader.ask_for_file()
    json_reader.read_json()
    json_reader.generate_image()


##########################---Auxiliary methods---##########################
def print_header():
    print("Hi! Thanks for using our A-Maze-ing Generator.")


def print_menu():
    option = input("\nFeel free to choose an option:"
                   "\n\t[1] Generate a Maze"
                   "\n\t[2] Load a Maze"
                   "\n\t[3] Exit\n")
    if option == "1":
        generate_maze()
    elif option == "2":
        read_json()
    elif option == "3":
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
