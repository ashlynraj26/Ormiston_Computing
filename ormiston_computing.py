from tkinter import *


root = Tk()
root.geometry('800x500')
root.title('Ormiston Computing')

###################### BUTTON COMANDS #######################

#Easy questions page:
def easyqpage():
    f3=Frame()
    f3.place(x=0,y=0,width=425,height=280)

    


#Button commnd to difficulty selection page:
def difficultypage():
    f2=Frame()
    f2.place(x=0,y=0,width=425,height=280)

    label2=Label(f2, text="SELECT DIFFICULTY LEVEL:")
    label2.place(y=5)
    
    b2=Button(f2,text="EASY",command=easyqpage)
    b2.pack()

    b3=Button(f2,text="MEDIUM",command=mediumqpage)
    b3.pack()

    b4=Button(f2,text="HARD",command=hardqpage)
    b4.pack()




#First frame where user enters their name
f1=Frame()
f1.place(x=0,y=0,width=425,height=280)#making the frame the same size as the root geometry

label1=Label(text="ENTER YOUR NAME")
label1.place(y=5)

usersname=Entry(f1)
usersname.place(y=30)

b1=Button(f1, text="NEXT", command=difficultypage)
b1.place(y=60)




















root.resizable(False,False)
root.mainloop()
#ww = welcome_window(frame1)


#root.configure(bg='#f2f2f2')
