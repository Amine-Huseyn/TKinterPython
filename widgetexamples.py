from tkinter import *

window = Tk()
window.title("Tkinter Python")
window.minsize(width=600, height=600)
window.config(padx=20,pady=20)



mylabel= Label(text="my label")
mylabel.config(bg="black")
mylabel.config(fg="white")
mylabel.config(padx=10, pady=10)
mylabel.pack()



def buttonclicked():
    print("button clicked")
    print(mytext.get("1.0", END))


mybutton=Button(text="button", command=buttonclicked)
mybutton.config(padx=10, pady=10)
mybutton.pack()

myentry= Entry(width=20)
myentry.pack()

#multiline
mytext= Text(width=30, height=5)
mytext.pack()

#scale
def scaleselected(value):
    print(value)
myscale=Scale(from_=0,to=50,command=scaleselected)
myscale.pack()

#spinbox
def spinboxselected():
    print(myspinbox.get())
myspinbox= Spinbox(from_=0,to=50, command=spinboxselected)
myspinbox.pack()

#checkbutton
def checkbuttonselected():
    print(checkstate.get())


checkstate=IntVar()
mycheckb=Checkbutton(text="check", variable=checkstate, command=checkbuttonselected)
mycheckb.pack()

#radio button

def radioselected():
    print(radiochecked.get())

radiochecked=IntVar()
myradio = Radiobutton(text="1.option",value=10,variable=radiochecked,command=radioselected)
myradio2=Radiobutton(text="2.option",value=20,variable=radiochecked,command=radioselected)
myradio.pack()
myradio2.pack()

#listbox

def listboxselected(event):
    print(mylistbox.get(mylistbox.curselection()))


mylistbox=Listbox()
mylist=["Amine","Atil","ABC"]
for i in range(len(mylist)):
    mylistbox.insert(i,mylist[i])
mylistbox.bind('<<ListboxSelect>>', listboxselected)
mylistbox.pack()


window.mainloop()