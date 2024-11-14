from tkinter import *
window = Tk()
frame = Frame(window,bg = "grey",borderwidth = 6, relief = SUNKEN)
frame.pack(side=LEFT,anchor="nw",fill=X)
def Press1():
    print("Before Launch")
def Press2():
    print("Checking all the sensors,and keeping default value to be zero for all sensors and altitude zero with reference to launch pad")
def Press3():
    print("Getting ready for Launch")
def Press4():
    print("Covering more than 100 meter in 3 seconds")
def Press5():
    print("Deploying DC Motor")
def Press6():
    print("Covering less than 3 meters in 3 seconds")
def Press7():
    print("Before Landing")
def Press8():
    print("Reset all the parameters after launch")
B1 = Button(frame,text="BOOT",bg="black",fg="white",command=Press1)
B1.pack(side=LEFT,padx=10)
B2 = Button(frame,text="TEST_MODE",bg="black",fg="white",command=Press2)
B2.pack(side=LEFT,padx=10)
B3 = Button(frame,text="Pre Launch",bg="black",fg="white",command=Press3)
B3.pack(side=LEFT,padx=10)
B4 = Button(frame,text="ASCENT",bg="black",fg="white",command=Press4)
B4.pack(side=LEFT,padx=10)
B5 = Button(frame,text="ROCKET_DEPLOY",bg="black",fg="white",command=Press5)
B5.pack(side=LEFT,padx=10)
B6 = Button(frame,text="DESCENT",bg="black",fg="white",command=Press6)
B6.pack(side=LEFT,padx=10)
B7 = Button(frame,text="AEROBRAKE_RELEASE",bg="black",fg="white",command=Press7)
B7.pack(side=LEFT,padx=10)
B8 = Button(frame,text="IMPACT",bg="black",fg="white",command=Press8)
B8.pack(side=LEFT,padx=10)
window.mainloop()