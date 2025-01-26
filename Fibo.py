#fibonacci tree
from graphics import *
import random

# Declare constants and global variables
win = GraphWin("Fibo", 700, 700)
sbranch_x = [350]
sbranch_y = [600]
LEN_x = 50
LEN_y = 40
ebranch_x = [350]
ebranch_y = [550]

# Functions
def FiboTree():
    a = 0
    b = 1
    prev = 1.0
    rnd = 0.0
    width = 12

# Draw first tree trunk
    pt1 = Point(sbranch_x[0], sbranch_y[0])
    pt2 = Point(ebranch_x[0], ebranch_y[0])
    trunk = Line(pt1, pt2)
    trunk.setWidth(width)
    trunk.draw(win)
    
# loop on generations
    for i in range(12):
        width = width-1
        print(width)
        time.sleep(0.1)
        nbranch = len(ebranch_x)
        nbranch_next = len(ebranch_x)
        
        # loop on branches of generation i
        for j in range(nbranch):           
            rnd = random.random()

            if (rnd < 0.618):
                # generate new branch and let go with angle
                nbranch_next += 1
                lbranch_x = int((random.random()-0.5)*LEN_x)
                lbranch_y = int((random.random()-0.1)*LEN_y)

                pt1 = Point(ebranch_x[j], ebranch_y[j])
                pt2 = Point(ebranch_x[j]+lbranch_x, ebranch_y[j]-lbranch_y)
                trunk = Line(pt1, pt2)
                trunk.setWidth(width)   
                trunk.draw(win)
    
                list.append(ebranch_x, ebranch_x[j]+lbranch_x)
                list.append(ebranch_y, ebranch_y[j]-lbranch_y)
                
                # let original branch grow at same angle as before
                lbranch_x = int((random.random()-0.5)*LEN_x)
                lbranch_y = int((random.random()-0.1)*LEN_y)
                pt1 = Point(ebranch_x[j], ebranch_y[j])
                pt2 = Point(ebranch_x[j]+lbranch_x, ebranch_y[j]-lbranch_y)
                trunk = Line(pt1, pt2)
                trunk.setWidth(width)
                trunk.draw(win)                
                ebranch_x[j] = ebranch_x[j]+lbranch_x
                ebranch_y[j] = ebranch_y[j]-lbranch_y
            else:
                # let original branch grow
                lbranch_x = int((random.random()-0.5)*LEN_x)
                lbranch_y = int((random.random()-0.1)*LEN_y)
                pt1 = Point(ebranch_x[j], ebranch_y[j])
                pt2 = Point(ebranch_x[j]+lbranch_x, ebranch_y[j]-lbranch_y)
                trunk = Line(pt1, pt2)
                trunk.setWidth(width)
                trunk.draw(win)                
                ebranch_x[j] = ebranch_x[j]+lbranch_x
                ebranch_y[j] = ebranch_y[j]-lbranch_y
                
        print(i, nbranch_next, nbranch_next/nbranch)
        
#        a, b = b, a+b
#        prev = float(b)

# Function main    
def main():
#    for i in range(6):
    FiboTree()
    time.sleep(1)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done


# Launch execution of function main from command shell
if __name__ == "__main__":
    main()
