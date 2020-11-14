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
                self.draw_floors(maze, maze_pic_draw, pointer, i, j)
                self.draw_walls(maze, maze_pic_draw, pointer, i, j)


        maze_pic.save("Lab_"+str(rows) + "_" + str(columns) + ".jpg")

    @staticmethod
    def draw_walls(maze, maze_pic_draw, pointer, i, j):
        if not maze.body[i][j].NESO[0]:
            maze_pic_draw.line((pointer[0], pointer[1], pointer[0] + 20, pointer[1]), width=3, fill=(0,0,0))
        if not maze.body[i][j].NESO[1]:
            maze_pic_draw.line((pointer[0] + 20, pointer[1], pointer[0] + 20, pointer[1] + 20), width=3, fill=(0,0,0))
        if not maze.body[i][j].NESO[2]:
            maze_pic_draw.line((pointer[0], pointer[1] + 20, pointer[0] + 20, pointer[1] + 20), width=3, fill=(0,0,0))
        if not maze.body[i][j].NESO[3]:
            maze_pic_draw.line((pointer[0], pointer[1], pointer[0], pointer[1] + 20), width=3, fill=(0,0,0))
    
    def draw_floors(self, maze, maze_pic_draw, pointer, i, j):
        color = self.get_floor_type(maze.body[i][j].value)
        maze_pic_draw.rectangle((pointer[0], pointer[1], pointer[0] + 20, pointer[1]+20), fill = color)
    
    @staticmethod
    def get_floor_type(value):
        color = tuple()
        if value == 0:
            color = (255,255,255)
            return color
        elif value == 1:
            color = (223,180,123)
            return color
        elif value == 2:
            color = (129,231,105) 
            return color
        elif value == 3:
            color = (18,167,213) 
            return color
    
    def draw_solution(self, solution, final_fringe, final_closed, maze):
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
                self.draw_floors(maze, maze_pic_draw, pointer, i, j)
                self.draw_solution_path(solution, maze, maze_pic_draw,pointer,i,j)
                self.draw_frontier(final_fringe, maze,maze_pic_draw,pointer,i,j)
                self.draw_closed(final_closed, maze,maze_pic_draw,pointer,i,j)
                self.draw_walls(maze, maze_pic_draw, pointer, i, j)

        maze_pic.save("Solution_"+str(maze.rows) + "_" + str(maze.columns) +".jpg")

    @staticmethod
    def draw_solution_path(solution, maze, maze_pic_draw,pointer,i,j):
        for x in solution:
            if x.state.id_state == (i,j):
                maze_pic_draw.rectangle((pointer[0], pointer[1], pointer[0] + 20, pointer[1]+20), fill = (255,0,0))
    
    @staticmethod
    def draw_frontier(final_fringe, maze, maze_pic_draw,pointer,i,j):
        for x in final_fringe:
            if x.state.id_state == (i,j):
                maze_pic_draw.rectangle((pointer[0], pointer[1], pointer[0] + 20, pointer[1]+20), fill = (0,0,255))
    
    @staticmethod
    def draw_closed(final_closed, maze, maze_pic_draw,pointer,i,j):
        for x in final_closed:
            if x.id_state == (i,j):
                maze_pic_draw.rectangle((pointer[0], pointer[1], pointer[0] + 20, pointer[1]+20), fill = (0,255,0))