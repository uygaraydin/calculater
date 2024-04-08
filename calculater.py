from tkinter import*

window=Tk()
window.title("Calculater")
window.geometry("300x240+300+300")
window.resizable(FALSE,FALSE)

store=""

def calculate(node):
    global store
    if node in "0123456789":
        data_entry.insert(END,node)
        store=store+node

    if node in"+-/*":
        data_entry.insert(END,node)
        store=store+node

    if node=="=":
        data_entry.delete(0,END)
        result=eval(store,{"__builtins__":None},{})
        store=str(result)
        data_entry.insert(END,store)


    if node=="C":
        window.delete(0,"END")
        store=""

data_entry=Entry(width=32, justify=RIGHT)
data_entry.grid(row=0,column=0,columnspan=20,ipady=8)

list=["1","2","3","4","5","6","7","8","9","0","+","-","/","*","=","C"]

row=1
column=0
for i in list:
    command=lambda x=i:calculate(x)
    Button(text=i,font="verdana 8 bold", width=10,height=2,relief=GROOVE,command=command).grid(row=row,column=column)
    column+=1
    if column>2:
        column=0
        row+=1




window.mainloop()

