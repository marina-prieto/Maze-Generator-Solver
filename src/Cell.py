from random import choice


class Cell:
    id = tuple()
    NESO = list()
    visited, final = bool(), bool()

    def __init__(self, identifier):
        self.id = identifier
        self.final = False
        self.visited = False
        self.NESO = [False, False, False, False]

###########################---Main Methods---###########################

    def get_random_neighbour(self, rows, columns):
        while True:
            selection = choice(["N", "E", "S", "O"])
            if selection == "N":
                if self.id[0] > 0:
                    position = (self.id[0]-1, self.id[1], "N")
                    return position
            elif selection == "E":
                if self.id[1] < columns-1:
                    position = (self.id[0], self.id[1]+1, "E")
                    return position
            elif selection == "S":
                if self.id[0] < rows-1:
                    position = (self.id[0]+1, self.id[1], "S")
                    return position
            elif selection == "O":
                if self.id[1] > 0:
                    position = (self.id[0], self.id[1]-1, "O")
                    return position
