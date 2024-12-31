import unittest
from maze import Maze
from graphics import Window
class Tests(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self._win = Window(600,600)
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(25, 25, num_rows, num_cols, 10, 10, self._win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        num_cols2 = 5
        num_rows2 = 20
        m2 = Maze(25,150, num_rows2, num_cols2, 10, 10, self._win)
        self.assertEqual(
            len(m2._cells),
            num_cols2
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows2,
        )

    def test_maze_break_ent_and_exit(self):
        num_cols = 5
        num_rows = 3
        m2 = Maze(160, 25, num_rows, num_cols, 20, 20, self._win)
        m2._break_entrance_and_exit()
    
    def test_reset_cells_visited(self):
        num_cols = 5
        num_rows = 3
        m2 = Maze(160, 25, num_rows, num_cols, 20, 20, self._win)
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertFalse(m2._cells[i][j]._visited)
if __name__ == "__main__":
    unittest.main()
