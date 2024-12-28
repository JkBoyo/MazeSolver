from graphics import Point, Line, Window
class Cell():
    def __init__(self, left_w, right_w, top_w, bottom_w, point_1, point_2, win: Window):
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
            self._win.draw_line(left_w, "green")
        if self._has_bottom_wall:
            self._win.draw_line(bottom_w, "green")
        if self._has_right_wall:
            self._win.draw_line(right_w, "green")
        if self._has_top_wall:
            self._win.draw_line(top_w, "green")

    def draw_move(self, to_move: 'Cell', undo = False):
        if not undo:
            line_color = "red"
        else:
            line_color = "gray"
        self_center = Point((self._x2-self._x1)/2 + self._x1, (self._y2-self._y1)/2 +self._y1)
        to_move_center = Point((to_move._x2-to_move._x1)/2 +to_move._x1, (to_move._y2-to_move._y1)/2 + to_move._y1)
        line = Line(self_center, to_move_center)
        self._win.draw_line(line, line_color)