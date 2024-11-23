from objects import Window, Point, Line
from cell import Cell


def main():

    win = Window(800,600)
    
    point1 = Point(50,50)
    point2 = Point(100,100)
    point3 = Point(100,50)
    point4 = Point(150,100)
    point5 = Point(150,150)
   


    c = Cell(win,point1,point2,has_right_wall=False)
    c2 = Cell(win,point3,point4,has_left_wall=False,has_bottom_wall=False)
    c3 = Cell(win,point2,point5,has_top_wall=False)


    c.draw()
    c2.draw()
    c3.draw()
    
    c.draw_move(c2)
    c2.draw_move(c3)

    


    win.wait_for_close()


main()