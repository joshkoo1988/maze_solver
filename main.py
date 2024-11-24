from objects import Window
from maze import Maze



def main():

    num_rows = 12
    num_col = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_col
    cell_size_y = (screen_y - 2 * margin) / num_col

    win = Window(screen_x,screen_y)
    
    maze = Maze(margin,margin,num_rows,num_col,cell_size_x,cell_size_y,win)


    win.wait_for_close()


main()