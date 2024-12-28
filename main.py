from graphics import Window, Line, Point
from maze import Cell

def main():
    win = Window(800,600)
    point1 = Point(75, 100)
    point2 = Point(275, 100)
    point3 = Point(75, 300)
    point4 = Point(275, 300)
    new_p1 = Point(475, 300)
    line1 = Line(point1, point2)
    line2 = Line(point2, point3)
    line3 = Line(point3, point4)
    line4 = Line(point4, point1)
    cell = Cell(True, True, True,True, point1, point4, win)
    
    cell.draw()

    cell.draw(point2, new_p1)

    win.wait_for_close()

main()