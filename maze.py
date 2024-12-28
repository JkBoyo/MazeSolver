from graphics import Point, Line, Window
class Cell():
    def __init__(self, left_w, right_w, top_w, bottom_w, point_1, point_2, win):
        self._has_left_wall = left_w
        self._has_right_wall = right_w
        self._has_top_wall = top_w
        self._has_bottom_wall = bottom_w
        self._x1 = point_1.x
        self._y1 = point_1.y
        self._x2 = point_2.x
        self._y2 = point_2.y
        self._win = win
    
    def draw(self, point1=None, point2=None):
        if point1:
            self._x1 = point1.x
            self._y1 = point1.y
        if point2:
            self._x2 = point2.x
            self._y2 = point2.y
            
        top_left = Point(self._x1, self._y1)
        bottom_left = Point(self._x1, self._y2)
        top_right = Point(self._x2, self._y1)
        bottom_right = Point(self._x2, self._y2)

        left_w = Line(top_left, bottom_left)
        bottom_w = Line(bottom_left, bottom_right)
        right_w = Line(bottom_right, top_right)
        top_w = Line(top_left, top_right)

        if self._has_left_wall:
            left_w.draw(self._win.Canvas,"green")
        if self._has_bottom_wall:
            bottom_w.draw(self._win.Canvas, "green")
        if self._has_right_wall:
            right_w.draw(self._win.Canvas, "green")
        if self._has_top_wall:
            top_w.draw(self._win.Canvas, "green")