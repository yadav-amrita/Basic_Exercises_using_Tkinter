from tkinter import *
root = Tk()

def getvals():
    print("Value Submitter!")
    
Label(root,text="USERNAME").grid()
Label(root,text="PASSWORD").grid(row=1)

uservalue = StringVar()
passvalue = StringVar()

Entry(root,textvariable=uservalue).grid(row=0,column=1)
Entry(root,textvariable=passvalue).grid(row=1,column=1)

Button(text="Submit",command=getvals).grid(row=3,column=0)
root.mainloop()