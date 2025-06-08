from graphics import Window, Cell
import time as tm
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        if seed is not None:
            random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
    
    def __create_cells(self):
        for i in range(self.__num_cols):
            cells_col = []
            for j in range(self.__num_rows):
                cells_col.append(Cell(self.__win))
            self.__cells.append(cells_col)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)
        

    def __draw_cell(self, i, j): 
        if self.__win is None:
            return
        x1 = self.__x1 + (self.__cell_size_x * i)
        x2 = x2 = x1 + self.__cell_size_x     
        y1 = self.__y1 + (self.__cell_size_y * j)
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()      

    def __animate(self):
        if self.__win is None:
            return
        tm.sleep(0.025)
        self.__win.redraw()

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols-1][self.__num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1 , self.__num_rows-1)
        self.__break_walls_r(0, 0)
        
        
    def __break_walls_r(self, i, j):
        current = self.__cells[i][j]
        current.visited = True

        while True:
            possible_dir = []
            if i != self.__num_cols - 1 and self.__cells[i+1][j].visited == False:
                possible_dir.append((i+1, j))
            if j != self.__num_rows - 1 and self.__cells[i][j+1].visited == False:
                possible_dir.append((i, j+1))
            if i != 0 and self.__cells[i-1][j].visited == False:
                possible_dir.append((i-1, j))
            if j != 0 and self.__cells[i][j-1].visited == False:
                possible_dir.append((i, j-1))

            if len(possible_dir) == 0:
                self.__draw_cell(i, j)
                return
            
            new_current = random.choice(possible_dir)
            new_i = new_current[0]
            new_j = new_current[1]

            if new_i == i + 1 and new_j == j:
                current.has_right_wall = False
            if new_i == i and new_j == j + 1:
                current.has_bottom_wall = False
            if new_i == i - 1 and new_j == j:
                current.has_left_wall = False
            if new_i == i and new_j == j - 1:
                current.has_top_wall = False
            
            self.__break_walls_r(new_i, new_j)

                

        






