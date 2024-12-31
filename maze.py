from graphics import Point, Line, Window
import time
import random
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
        self._visited = False
    
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
        else:
            self._win.draw_line(left_w, "white")
        if self._has_bottom_wall:
            self._win.draw_line(bottom_w, "green")
        else:
            self._win.draw_line(bottom_w, "white")
        if self._has_right_wall:
            self._win.draw_line(right_w, "green")
        else:
            self._win.draw_line(right_w, "white")
        if self._has_top_wall:
            self._win.draw_line(top_w, "green")
        else:
            self._win.draw_line(top_w, "white")

    def draw_move(self, to_move: 'Cell', undo = False):
        if not undo:
            line_color = "red"
        else:
            line_color = "gray"
        self_center = Point((self._x2-self._x1)/2 + self._x1,
                            (self._y2-self._y1)/2 +self._y1)
        to_move_center = Point((to_move._x2-to_move._x1)/2 + to_move._x1,
                               (to_move._y2-to_move._y1)/2 + to_move._y1)
        line = Line(self_center, to_move_center)
        self._win.draw_line(line, line_color)

class Maze():
    def __init__(self,
                x1,
                y1,
                num_rows,
                num_cols,
                cell_size_x,
                cell_size_y,
                win: Window,
                seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()


    def _create_cells(self):
        for i in range(0, self._num_cols):
            col_list = []
            for j in range(0, self._num_rows):
                top_x = self._x1 + (self._cell_size_x * i)
                top_y = self._y1 + (self._cell_size_y * j)
                top_point = Point(top_x, top_y)
                bottom_point = Point(top_x + self._cell_size_x,
                                     top_y + self._cell_size_y)
                cell = Cell(True,True,True,True,
                            top_point, bottom_point,
                            self._win)
                col_list.append(cell)
                cell.draw()
                self._animate()
            self._cells.append(col_list)

    def _animate(self):
        self._win.redraw()
        time.sleep(0.1)

    def _break_entrance_and_exit(self):
        start = self._cells[0][0]
        finish = self._cells[-1][-1]
        start._has_top_wall = False
        finish._has_bottom_wall = False
        start.draw()
        finish.draw()

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            current = self._cells[i][j]
            cells_to_visit = []
            # up
            if (j - 1) >= 0 and not self._cells[i][j - 1]._visited:
                cells_to_visit.append((i, j - 1))
            # down
            if (j + 1) < self._num_rows and not self._cells[i][j + 1]._visited:
                cells_to_visit.append((i, j + 1))
            # left
            if (i - 1) >= 0 and not self._cells[i - 1][j]._visited:
                cells_to_visit.append((i - 1, j))
            # right
            if (i + 1) < self._num_cols and not self._cells[i + 1][j]._visited:
                cells_to_visit.append((i + 1, j))
            if len(cells_to_visit) == 0:
                current.draw()
                return
            else:
                direction = cells_to_visit[
                            random.randrange(0, len(cells_to_visit))
                        ]
                k, l = direction
                next_cell = self._cells[k][l]
                if i < k: # right
                    current._has_right_wall = False
                    next_cell._has_left_wall = False
                elif i > k: # left
                    current._has_left_wall = False
                    next_cell._has_right_wall = False
                elif j < l: # down
                    current._has_bottom_wall = False
                    next_cell._has_top_wall = False
                elif j > l: #up
                    current._has_top_wall = False
                    next_cell._has_bottom_wall = False
                
                current.draw()
                next_cell.draw()
                self._break_walls_r(k, l)
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j]._visited = False
    
    def solve(self):
       return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current._visited = True
        end = self._cells[-1][-1]
        if current == end:
            return True
        directions = [
            (i-1, j, current._has_left_wall),
            (i+1, j, current._has_right_wall),
            (i, j-1, current._has_top_wall),
            (i, j+1, current._has_bottom_wall)
        ]
        for k, l, dir_wall_present in directions:
            if (self._num_cols> k and k >= 0 and 
                self._num_rows > l and l >= 0 and 
                not dir_wall_present and 
                not self._cells[k][l]._visited):
                current.draw_move(self._cells[k][l])
                solution = self._solve_r(k, l)
                if solution:
                    return True
                current.draw_move(self._cells[k][l], True)
        return False
