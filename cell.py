from objects import Point, Line

class Cell:
    def __init__(self,top_left,bottom_right,win,has_left_wall=True,has_right_wall=True,has_bottom_wall=True,has_top_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = top_left.x
        self._x2 = bottom_right.x
        self._y1 = top_left.y
        self._y2 = bottom_right.y
        self._win = win

    def draw(self):
        bottom_left = Point(self._x1,self._y2)
        bottom_right = Point(self._x2,self._y2)
        top_left = Point(self._x1,self._y1)
        top_right = Point(self._x2,self._y1)

        if self.has_bottom_wall:
            self.bottom_wall = Line(bottom_left,bottom_right)
            self._win.draw_line(self.bottom_wall)
        if self.has_left_wall:
            self.left_wall = Line(bottom_left,top_left)
            self._win.draw_line(self.left_wall)
        if self.has_right_wall:
            self.right_wall = Line(bottom_right,top_right)
            self._win.draw_line(self.right_wall)
        if self.has_top_wall:
            self.top_wall = Line(top_left,top_right)
            self._win.draw_line(self.top_wall)