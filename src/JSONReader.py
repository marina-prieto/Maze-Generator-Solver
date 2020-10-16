"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavón
    -   Josue Carlos Zenteno Yave
"""
import json
from src.Maze import Maze
from src.Cell import Cell
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


class JSONReader:
    ###########################---Attributes---############################
    file_path = str()
    input_file = str()
    input_json = json

    ###########################---Constructor---###########################
    def __init__(self):
        pass

    ###########################---Main Methods---##########################
    def read_json(self):
        #Checking if the input file is correct or not
        if not self.is_valid_json():
            self.notify_error("File_Type")
        else:
            self.input_file = open(self.file_path)
            self.input_json = json.load(self.input_file)

    def generate_image(self):
        #Generating a temporal maze which will store the information about the maze read in the json file
        temp_maze = self.generate_temp_maze()
        #Using the corresponding method
        temp_maze.generate_image()

    def generate_temp_maze(self):
        maze = Maze(self.input_json["rows"], self.input_json["cols"])
        #Assigning the NESO values to the corresponding cells of the maze
        for i in range(self.input_json["rows"]):
            for j in range(self.input_json["cols"]):
                maze.body[i][j].NESO = self.input_json["cells"]["(" + str(i) + ", " + str(j) + ")"]["neighbors"]
        return maze

    def is_valid_json(self):
        #Checking if the file is a JSON file
        if self.file_path[-4:] == "json":
            return True
        return False

    def ask_for_file(self):
        # Hiding the tk GUI
        Tk().withdraw()
        # show an "Open" dialog box and return the path to the selected file
        filename = askopenfilename()
        self.file_path = filename

    @staticmethod
    def notify_error(kind):
        #List of errors that we will notify
        if kind == "File_Type":
            print("Wrong file type, please select a json file")
        #TODO
