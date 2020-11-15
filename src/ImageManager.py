"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavón
    -   Josue Carlos Zenteno Yave
"""
from PIL import Image, ImageDraw

class ImageManager:
    ###########################---Constructor---###########################
    def __init__(self):
        pass

    ###########################---Main Methods---##########################
    def generate_image(self, maze, rows, columns):
        # Creating a picture of size <xy>, which depends on the size of a cell (20x20 px) and the number of rows and columns
        maze_pic = Image.new(mode="RGB", size=((columns * 20) + 10, (rows * 20) + 10), color = (255,255,255))
        maze_pic_draw = ImageDraw.Draw(maze_pic)

        # Initialize a pointer in (5,5) (x,y)
        pointer = [5, 5]
        for i in range(rows):
            # We don't want to move the pointer if we are in the first row neither in the first column
            if i != 0:
                pointer[0] = 5
                pointer[1] += 20
            for j in range(columns):
                if j != 0:
                    pointer[0] += 20
                self.draw_floor(maze, maze_pic_draw, pointer, i, j)
                self.draw_wall(maze, maze_pic_draw, pointer, i, j)

        maze_pic.save("puzzle_"+str(rows) + "x" + str(columns) + ".png")

    def draw_solution(self, solution, final_fringe, final_closed, maze, strategy):
        # Creating a picture of size <xy>, which depends on the size of a cell (20x20 px) and the number of rows and columns
        maze_pic = Image.new(mode="RGB", size=((maze.columns * 20) + 10, (maze.rows * 20) + 10), color = (255,255,255))
        maze_pic_draw = ImageDraw.Draw(maze_pic)

        # Initialize a pointer in (5,5) (x,y)
        pointer = [5, 5]
        for i in range(maze.rows):
            # We don't want to move the pointer if we are in the first row neither in the first column
            if i != 0:
                pointer[0] = 5
                pointer[1] += 20
            for j in range(maze.columns):
                if j != 0:
                    pointer[0] += 20
                # We keep an specific order to draw the elements of the picture as we want to highlight the solution path and the walls
                self.draw_floor(maze, maze_pic_draw, pointer, i, j)
                self.draw_frontier(final_fringe, maze,maze_pic_draw,pointer,i,j)
                self.draw_closed(final_closed, maze,maze_pic_draw,pointer,i,j)
                self.draw_solution_path(solution, maze, maze_pic_draw,pointer,i,j)
                self.draw_wall(maze, maze_pic_draw, pointer, i, j)

        maze_pic.save("solution_"+str(maze.rows) + "x" + str(maze.columns) +"_"+strategy+".png")


    #########################---Auxiliary Methods---#######################
    def draw_floor(self, maze, maze_pic_draw, pointer, i, j):
        color = self.get_floor_color(maze.body[i][j].value)
        # We draw a rectangle of the corresponding color
        maze_pic_draw.rectangle((pointer[0], pointer[1], pointer[0] + 20, pointer[1]+20), fill = color)
    
    @staticmethod
    def draw_wall(maze, maze_pic_draw, pointer, i, j):
        #We draw a line per wall
        if not maze.body[i][j].NESO[0]:
            maze_pic_draw.line((pointer[0], pointer[1], pointer[0] + 20, pointer[1]), width=3, fill=(0,0,0))
        if not maze.body[i][j].NESO[1]:
            maze_pic_draw.line((pointer[0] + 20, pointer[1], pointer[0] + 20, pointer[1] + 20), width=3, fill=(0,0,0))
        if not maze.body[i][j].NESO[2]:
            maze_pic_draw.line((pointer[0], pointer[1] + 20, pointer[0] + 20, pointer[1] + 20), width=3, fill=(0,0,0))
        if not maze.body[i][j].NESO[3]:
            maze_pic_draw.line((pointer[0], pointer[1], pointer[0], pointer[1] + 20), width=3, fill=(0,0,0))
    
    @staticmethod
    def draw_solution_path(solution, maze, maze_pic_draw,pointer,i,j):
        # We go through the solution nodes and draw a rectangle of the corresponding color
        for x in solution:
            if x.state.id_state == (i,j):
                maze_pic_draw.rectangle((pointer[0], pointer[1], pointer[0] + 20, pointer[1]+20), fill = (255,0,0))
    
    @staticmethod
    def draw_frontier(final_fringe, maze, maze_pic_draw,pointer,i,j):
        # We go through the fringe nodes and draw a rectangle of the corresponding color
        for x in final_fringe.pop_all():
            if x.state.id_state == (i,j):
                maze_pic_draw.rectangle((pointer[0], pointer[1], pointer[0] + 20, pointer[1]+20), fill = (0,0,255))
    
    @staticmethod
    def draw_closed(final_closed, maze, maze_pic_draw,pointer,i,j):
        # We go through the visited nodes and draw a rectangle of the corresponding color
        for x in final_closed:
            if x == (i,j):
                maze_pic_draw.rectangle((pointer[0], pointer[1], pointer[0] + 20, pointer[1]+20), fill = (0,255,0))

    @staticmethod
    def get_floor_color(value):
        #Depending on the kind of floor we return its RGB color
        if value == 0:
            return (255,255,255)
        elif value == 1:
            return (223,180,123)
        elif value == 2: 
            return (129,231,105)
        elif value == 3:
            return (18,167,213)