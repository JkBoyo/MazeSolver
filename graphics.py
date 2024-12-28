from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height, ):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.Canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.Canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color: str):
        line.draw(self.Canvas, fill_color)

    def close(self):
        self.running = False

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )
    