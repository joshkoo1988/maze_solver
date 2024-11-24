from cell import Cell
from objects import Point
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
            ):
        
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self.reset_visited()
    
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

                self._cells[col].append(Cell(point_1, point_2,win=self.win))

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

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(self._cells[0][0])
        
        last_col_index = len(self._cells) - 1
        last_row_index = len(self._cells[last_col_index]) - 1
        self._cells[last_col_index][last_row_index].has_bottom_wall = False
        self._draw_cell(self._cells[last_col_index][last_row_index])


    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True

        while True:
            possible_directions  = []
            #right
            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                possible_directions.append((i+1,j))
            #left
            if i > 0 and not self._cells[i-1][j].visited:
                possible_directions.append((i-1,j))
            #down
            if j < self.num_rows - 1 and not self._cells[i][j+1].visited:
                possible_directions.append((i,j+1))
            #up
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append((i,j-1))


            if len(possible_directions) == 0:
                self._draw_cell(self._cells[i][j])
                return


            direction_index = random.randrange(len(possible_directions))
            next_index = possible_directions[direction_index]

            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                #print(f"i:{i} j:{j} direction: up")

            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                #print(f"i:{i} j:{j} direction: down")

            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                #print(f"i:{i} j:{j} direction: left")

            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                #print(f"i:{i} j:{j} direction: right")
                
            self._break_walls_r(next_index[0],next_index[1])
            
    def reset_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False
                #print(f"cell i{i}j{j} reset to {self._cells[i][j].visited}")
