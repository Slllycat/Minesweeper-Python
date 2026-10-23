#minesweper
import tkinter as tk
import random

#settings
size0=20        #the size of your minesweeper
biggnes=40      #the visuel size on your screen
fullness=15      #the amount of mines in %  (10-20 optimal)

#variable :O
death=0
mx=0
my=0
size = size0+2
size2 = size**2
flags=0
near = []
flag = []



#window setup
window = tk.Tk()
window.title("BLEH")
window.geometry(str(size * biggnes) + "x" + str(size * biggnes))
canvas = tk.Canvas(window, width=(size * biggnes), height=(size * biggnes), bg="white")
canvas.pack()



#resets
def reset():
    global size,size2,blocks,near
    blocks = []
    near = []
    for i in range(size):
        blocks.append(1)
    for i in range(size-2):
        blocks.append(1)
        for i in range(size-2):
            blocks.append(0)
        blocks.append(1)
    for i in range(size):
        blocks.append(1)
    for i in range(size2):
        near.append("x")



def mines():
    global size,size2,mines,fullness,flag,flags
    mines = []
    for i in range(size):
        mines.append(0)
        flag.append(0)
    for i in range(size-2):
        mines.append(0)
        flag.append(0)
        for i in range(size-2):
            if random.randint(0,100) <= fullness:
                mines.append(1)
                flag.append(1)
            else:
                mines.append(0)
                flag.append(0)
        mines.append(0)
        flag.append(0)
    for i in range(size):
        mines.append(0)
        flag.append(0)
    mines[int(size/2)+int(size/2)*size]=0
    flag[int(size/2)+int(size/2)*size]=0
    flags=mines.count(1)
    print(flags)



reset()
mines()
def die():
    global death
    death=1
    render()
    exit("YOU LOST")



def tick(weg):
    global mines,near,size,size2
    if mines[weg]==1:
        die()
        return False
    if weg+1+size<=size2-1 and weg-1-size>=0:
        near[weg]=mines[weg+1]+mines[weg-1]+mines[weg+size]+mines[weg-size]+mines[weg+1+size]+mines[weg-1+size]+mines[weg-1-size]+mines[weg+1-size]
        if near[weg] ==0:
            if weg+1<=size2 and near[weg+1]=="x":
                tick(weg+1)
            if weg-1>=0 and near[weg-1]=="x":
                tick(weg-1)
            if (weg+size)<=size2 and near[weg+size]=="x":
                tick(weg+size)
            if (weg-size)>=0 and near[weg-size]=="x":
                tick(weg-size)
            if (weg+1+size)<=size2 and near[weg+1+size]=="x":
                tick(weg+1+size)
            if (weg+1-size)>=0 and near[weg+1-size]=="x":
                tick(weg+1-size)
            if (weg-1+size)<=size2 and near[weg-1+size]=="x":
                tick(weg-1+size)
            if (weg-1-size)>=0 and near[weg-1-size]=="x":
                tick(weg-1-size)
    render()




def render():
    global cube,blocks,near,mines,death,flag,flags
    x = 0
    y = biggnes*size
    weg = 0
    canvas.delete("all")
    # RENDER BLOCKS
    for i in range(size):
        for i in range(size):
            if blocks[weg] == 1:
                cube = canvas.create_rectangle(x, y, x + biggnes, y - biggnes, fill="black")
            else:
                if death==0:
                    if near[weg]!="x":
                        cube = canvas.create_rectangle(x, y, x + biggnes, y - biggnes, fill="white")
                        if near[weg]==0:
                            color="black"
                        elif near[weg]<=2:
                            color="darkgreen"
                        elif near[weg]<=4:
                            color="blue"
                        elif near[weg]<=6:
                            color="blue"
                        elif near[weg]<=8:
                            color="blue"
                        else:
                            color="violet"
                        canvas.create_text(x+biggnes/2, y-biggnes/2, text=(near[weg]), fill=color, font=("Arial", biggnes))
                        if flag[weg]=="f":
                            flag[weg]==mines[weg]
                            flags=flags+1
                    else:
                        cube = canvas.create_rectangle(x, y, x + biggnes, y - biggnes, fill="grey")
                        if flag[weg]=="f":
                            oval = canvas.create_oval(x+2, y-2, x+biggnes-2, y-biggnes+2, fill="black", outline="black", width=2)
                elif death==1:
                    if mines[weg]==0:
                        cube = canvas.create_rectangle(x, y, x + biggnes, y - biggnes, fill="white")
                    else:
                        cube = canvas.create_rectangle(x, y, x + biggnes, y - biggnes, fill="red")
                        oval = canvas.create_oval(x+2, y-2, x+biggnes-2, y-biggnes+2, fill="black", outline="black", width=2)
                else:
                    if mines[weg]==0:
                        cube = canvas.create_rectangle(x, y, x + biggnes, y - biggnes, fill="white")
                    else:
                        cube = canvas.create_rectangle(x, y, x + biggnes, y - biggnes, fill="blue")
                        oval = canvas.create_oval(x+3, y-3, x+biggnes-3, y-biggnes+3, fill="darkgreen", outline="black", width=2)
            weg = weg + 1
            x = x + biggnes
        x = 0
        y = y - biggnes
    if death!=2:
        win()


#mouse pos
def mouse_pos(event):
    global mx, my
    mx, my = event.x, event.y
canvas.bind("<Motion>", mouse_pos)




#click detect
def mouse_click(event):
    global mx, my,size,biggnes,flag,death
    if death==0:
        if flag[int(mx/biggnes)+int(size-my/biggnes)*size]!="f":
            tick(int(mx/biggnes)+int(size-my/biggnes)*size)

canvas.bind("<Button-1>", mouse_click)


#TASTEN
def move(event):
    global mines,mx, my,size,biggnes,flag,flags,death
    if death==0:
        if event.keysym == "space":
            if flag[int(mx/biggnes)+int(size-my/biggnes)*size]!="f":
                if flags>0 and near[int(mx/biggnes)+int(size-my/biggnes)*size]=="x":
                    flag[int(mx/biggnes)+int(size-my/biggnes)*size]="f"
                    flags=flags-1
            else:
                flag[int(mx/biggnes)+int(size-my/biggnes)*size]=mines[int(mx/biggnes)+int(size-my/biggnes)*size]
                flags=flags+1
        render()

window.bind("<Key>", move)


def win():
    global death
    if not(1 in flag):
        death=2
        render()
        canvas.create_text(int(size*biggnes/2), int(size*biggnes/2), text=("YOU WON"), fill="darkgreen", font=("Arial", int(size*biggnes/8)))
        exit()

tick(int(size/2)+int(size/2)*size)
window.mainloop()
