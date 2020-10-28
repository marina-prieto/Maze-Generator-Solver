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
    @staticmethod
    def generate_image(maze, rows, columns):
        # Creating a picture of size <xy>, which depends on the size of a cell (20x20 px) and the number of rows and columns
        maze_pic = Image.new(mode="1", size=((columns * 20) + 10, (rows * 20) + 10), color=1)
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
                if not maze.body[i][j].NESO[0]:
                    maze_pic_draw.line((pointer[0], pointer[1], pointer[0] + 20, pointer[1]), width=3, fill=0)
                if not maze.body[i][j].NESO[1]:
                    maze_pic_draw.line((pointer[0] + 20, pointer[1], pointer[0] + 20, pointer[1] + 20), width=3, fill=0)
                if not maze.body[i][j].NESO[2]:
                    maze_pic_draw.line((pointer[0], pointer[1] + 20, pointer[0] + 20, pointer[1] + 20), width=3, fill=0)
                if not maze.body[i][j].NESO[3]:
                    maze_pic_draw.line((pointer[0], pointer[1], pointer[0], pointer[1] + 20), width=3, fill=0)

        maze_pic.save("Lab_"+str(rows) + "_" + str(columns) + ".jpg")
