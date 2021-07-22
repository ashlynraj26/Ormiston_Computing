from tkinter import *
#t=Tk()
#t.geometry("425x280")

root.geometry('425x280')


def login():
    f2=Frame()
    f2.place(x=0,y=0,width=425,height=280)
    e1=Entry(f2)
    e1.pack()
    e2=Entry(f2)
    e2.pack()
    b2=Button(f2,text="Login", command=namepage)
    b2.pack()
#making the frame the same size as the root geometry
def frameone():
    f1=Frame()
    f1.place(x=0,y=0,width=425,height=280)

    b1=Button(f1, text="Click!", command=login)
    b1.pack()

def namepage():
    f3=Frame()
    f3.place(x=0,y=0,width=425,height=280)
    e3=Entry(f3)
    e3.pack()
    b3=Button(f3,text="Back to frame 1", command=frameone)
    b3.pack()


root = Tk(f1)
#t.mainloop()
root.mainloop()





#root.title('Course selection')


#ww = welcome_window(frame1)


#root.configure(bg='#f2f2f2')
#root.resizable(False,False)

