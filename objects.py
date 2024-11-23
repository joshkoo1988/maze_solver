from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root,bg="white",width=width,height=height)
        self.canvas.pack(fill=BOTH,expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed ...")

    def close(self):
        self.running = False

    def draw_line(self,line,fill_color="Black"):
        line.draw(self.canvas,fill_color)


class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,point_a,point_b):
        self.a = point_a
        self.b = point_b
        
    def draw(self,canvas,fill_color="Black"):
        canvas.create_line(self.a.x,self.a.y,self.b.x,self.b.y,fill=fill_color,width=2)

