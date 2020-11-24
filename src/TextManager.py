"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavon
    -   Josue Carlos Zenteno Yave
"""
import os

class TextManager:

    ###########################---Constructor---###########################
    def __init__(self):
        pass
    ###########################---Main Methods---##########################
    @staticmethod
    def generate_txt_solution(solution, rows, columns, strategy):
        # Creating the file
        output_txt = open("solution_"+str(rows)+"x"+str(columns)+"_"+strategy+".txt", "w")
        # Changing the order of the solution list as it is required that the output is printed
        # in an specific order.
        solution.reverse()
        #Writting the very first line (legend)
        output_txt.write("[id][cost,state,father_id,action,depth,h,value]" + os.linesep)
        # Writting the solution list in the txt
        for x in solution:
            output_txt.write(x.toString() + os.linesep)
        
        output_txt.close()