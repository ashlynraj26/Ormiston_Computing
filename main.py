from tkinter import *

root = Tk()
root.geometry('800x500')
root.title('Ormiston Computing')

#Second frame
def questionspage():
    f2=Frame()
    f2.place(x=0,y=0,width=425,height=280)
    
    b2=Button(f2,text="Login", command=namepage)
    b2.pack()

#Conditions for moving onto the questions page
#def openquestionspage():
    
    

#First frame where user enters their name
f1=Frame()
f1.place(x=0,y=0,width=425,height=280)#making the frame the same size as the root geometry

label1=Label(text="ENTER YOUR NAME")
label1.place(y=5)

usersname=Entry(f1)
usersname.place(y=30)

b1=Button(f1, text="NEXT", command=questionspage)
b1.place(y=60)







def namepage():
    f3=Frame()
    f3.place(x=0,y=0,width=425,height=280)
    e3=Entry(f3)
    e3.pack()
    b3=Button(f3,text="Back to frame 1",command=f1)
    b3.pack()



root.resizable(False,False)
root.mainloop()





#root.title('Course selection')


#ww = welcome_window(frame1)


#root.configure(bg='#f2f2f2')


