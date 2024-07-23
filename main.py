import tkinter

#window
window = tkinter.Tk()
window.title("Python tkinter")
window.minsize(width=450, height=300)

def clickbutton():
    userinput= myentry.get()
    print(userinput)

#label
mylabel= tkinter.Label(text="this is a label", font=("Arial",30,"italic"))
#mylabel.config(bg="black", fg="white")
#mylabel.pack(side="left")
#mylabel.place(x=0,y=0)
mylabel.grid(row=0, column=0)


#button
mybutton=tkinter.Button(text="this is a button",command=clickbutton)
#mybutton.pack(side="left")
#mybutton.place(x=225-63,y=150-14)
#mybutton.update()
#print(mybutton.winfo_height())
#print(mybutton.winfo_width())
mybutton.grid(row=1, column=1)

#entry
myentry=tkinter.Entry(width=20)
#myentry.pack(side="left")
myentry.grid(row=0, column=2)














window.mainloop()