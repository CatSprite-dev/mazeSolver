from tkinter import Tk, BOTH, Canvas


from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False
        self.__root.destroy()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)



class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Line():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)



class Cell():
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.__win is None:
            return
        if self.has_left_wall:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(left_wall, "black")
        else:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(left_wall, "white")

        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(right_wall, "black")
        else:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(right_wall, "white")

        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(top_wall, "black")
        else:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(top_wall, "white")

        if self.has_bottom_wall:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(bottom_wall, "black")
        else:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        x1 = (self.__x1 + self.__x2) // 2
        y1 = (self.__y1 + self.__y2) // 2
        x2 = (to_cell.__x1 + to_cell.__x2) // 2
        y2 = (to_cell.__y1 + to_cell.__y2) // 2
        if self.__win is None:
            line = Line(Point(x1, y1), Point(x2, y2))
        else:
            line = Line(Point(x1, y1), Point(x2, y2))
            if undo == False:
                self.__win.draw_line(line, "red")
            else: 
                self.__win.draw_line(line, "gray")
        