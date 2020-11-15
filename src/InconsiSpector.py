"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavón
    -   Josue Carlos Zenteno Yave
"""

class InconsiSpector:
    ###########################---Constructor---###########################
    def __init__(self):
        pass

    ###########################---Main Methods---##########################
    def find_inconsistencies(self, suspicious_maze):
        # Checking inconsistencies, one by one, ordered by speed of execution. If we find one then it's not necessary to find more
        if self.border_inconsistency(suspicious_maze):
            return True, "There are blank spaces in the border"
        if self.isolated_cell(suspicious_maze):
            return True, "There are isolated cells"
        if self.bad_neighbors(suspicious_maze):
            return True, "There are wall inconsistencies"
        return False, "No error found"

    #########################---Auxiliary Methods---#######################
    @staticmethod
    def border_inconsistency(suspicious_maze):
        # Looking for True in the N and S components for both top and bottom rows of the maze
        for i in range(suspicious_maze.columns):
            if suspicious_maze.body[0][i].NESO[0] or suspicious_maze.body[suspicious_maze.rows-1][i].NESO[2]:
                return True
        # Looking for True in the E and O components for both left-most and right-most columns of the maze
        for i in range(suspicious_maze.rows):
            if suspicious_maze.body[i][0].NESO[3] or suspicious_maze.body[i][suspicious_maze.columns-1].NESO[1]:
                return True

    @staticmethod
    def isolated_cell(suspicious_maze):
        #Comparing every NESO list with a bad example of it
        bad_NESO = [False, False, False, False]
        for i in range(suspicious_maze.rows):
            for j in range(suspicious_maze.columns):
                if suspicious_maze.body[i][j].NESO == bad_NESO:
                    return True

    @staticmethod
    def bad_neighbors(suspicious_maze):
        # Checking only right and bottom neighbours of every cell and avoiding to check non-existing cells (left-most column and bottom row of the maze)
        for i in range(suspicious_maze.rows):
            for j in range(suspicious_maze.columns):
                if not suspicious_maze.body[i][j].id[1] == suspicious_maze.columns-1:
                    if suspicious_maze.body[i][j].NESO[1] != suspicious_maze.body[i][j+1].NESO[3]:
                        return True
                if not suspicious_maze.body[i][j].id[0] == suspicious_maze.rows-1:
                    if suspicious_maze.body[i][j].NESO[2] != suspicious_maze.body[i+1][j].NESO[0]:
                        return True
        return False
