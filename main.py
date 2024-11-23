from objects import Window, Point, Line
from cell import Cell


def main():

    win = Window(800,600)
    
    point1 = Point(100,100)
    point2 = Point(200,200)
    line1 = Line(point1,point2)

    c = Cell(point1,point2,win,has_bottom_wall=False,has_left_wall=False)
    c.draw()
    win.draw_line(line1)


    win.wait_for_close()


main()