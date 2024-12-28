from graphics import Window, Line, Point
from maze import Cell

def main():
    win = Window(800,600)
    point1 = Point(75, 100)
    point2 = Point(275, 100)
    point4 = Point(275, 300)
    new_p1 = Point(475, 300)
    cell = Cell(True, True, True,True, point1, point4, win)
    
    cell2 = Cell(True, True, True,True, point2, new_p1, win)
    cell.draw()


    cell2.draw()
    cell.draw_move(cell2, undo=True)
    win.wait_for_close()

main()