from tkinter import *
root = Tk()
root.title("Sudoku Solver")
root.geometry("324x550")
label = Label(root, text ="Fill in the numbers and click solve").grid(row =0 ,column=1,columnspan=10)
#grid():data that is organized in a two-dimensional or three-dimensional grid-like structure, such as an image or a spreadsheet.
#columnspan:should span 10 columns in the grid. This means it will cover columns 1 to 10

errLabel=Label(root,text = "",fg="red")
errLabel.grid(row=15,column=1,columnspan=10 , pady=5)
#pady:It adds padding (empty space) on the y-axis (vertical) around the widget

solvedLabel=Label(root,text = "",fg="green")
solvedLabel.grid(row=15,column=1,columnspan=10 , pady=5)

cells ={}
def ValidateNumber(P):#intended to be used as a validation function for the Entry widgets
    out =(P.isdigit() or P=="") and len(P)<2
    return out
reg= root.register(ValidateNumber)
#This is necessary when using validation functions with Entry widgets in tkinter

def draw3x3Grid(row,column,bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry (root,width=5,bg=bgcolor , justify="center",validate="key",validatecommand=(reg,"%P"))
            #justify="center": The text inside the Entry widget is centered
            e.grid(row=row+i+1,column=column+j+1,sticky="nsew",padx=1,pady=1,ipady=5)
            #This line uses the grid geometry manager to place the Entry widget in a specific cell of the grid
            #sticky="nsew": The widget should stick to the edges of its cell in the north, south, east, and west directions.
            cells[(row+i+1,column+j+1)]=e 
def draw9x9Grid():
    color = "#D0ffff"
    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            draw3x3Grid(rowNo,colNo,color)
            if color == "#D0ffff":
                color="#ffffd0" 
            else:
                color ="#D0ffff"  
def clearValues():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell=cells[(row,col)]
            cell.delete(0,"end")
def getValues():
    board =[]
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        rows=[]
        for col in range(1,10):
            val=cells[(row,col)].get()
            if val =="":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
btn=Button(root,command=getValues,text="Solve",width=10)
btn.grid(row=20,column=1,columnspan=5,pady=20) 

btn=Button(root,command=clearValues,text="Clear",width=10)
btn.grid(row=20,column=5,columnspan=5,pady=20)   

draw9x9Grid()
root.mainloop()