from cell import Cell
from objects import Point
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
            ):
        
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._create_cells()
    
    def _create_cells(self):
        self._cells = [[] for _ in range(self.num_cols)]
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                x1 = self.x1 + col * self.cell_size_x
                y1 = self.y1 + row * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y

                point_1 = Point(x1, y1)
                point_2 = Point(x2, y2)

                self._cells[col].append(Cell(self.win, point_1, point_2))

        for col in self._cells:
            for cell in col:
                self._draw_cell(cell)

    def _draw_cell(self,cell):
        if self.win is None or cell is None:
            return
        cell.draw()
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)