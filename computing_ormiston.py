from tkinter import *
import random

root = Tk()
root.geometry('700x400')
root.title('Ormiston Computing')


##############################  TO DO  ########################################

# change decimal placement values to whole numbers [AESTHETIC]
# cover the "start" button on questions page with the questions label [AESTHETIC]
# cover the question label with "correct" or "wrong" [AESTHETIC]
# cover wrong and correct lables so they overlap [AESTHETIC]
# write the name and user score to an external file
# CLEAR THE ENTRY WHEN "NEXT" IS CLICKED
# Error message when letters are added in entry question fields



######################################################################

score = 0
count = 0

#Lists for difficulty levels
easyq = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def scoreboard():
    f4=Frame()
    f4.place(x=0,y=0,width=700,height=400)

    #nameforscore=Label(f4, usersname.get)
    #nameforscore.place(x=20, y=10)

    start = Button(f4, text="Scoreboard")
    start.place(relx=0.45, rely=0.2)



######################################### Easy questions page:  [This should be a seperate class] ###############################################


def easyqpage():
    global nextq_easy
    f3=Frame()
    f3.place(x=0,y=0,width=700, height=400)

    #widgets
    start = Button(f3, text="Start", command=nextq_easy)
    start.place(x=60, y=100)

    solving = Entry(f3, width=7)
    solving.place(y=10)

    submit = Button(f3, text="Submit", command=lambda: submt(solving))
    submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

    ######CHANGE "TRY AGAIN" TO "NEXT QUESTION"
    nextq_easy = Button(f3, text="Next", command=nextq_easy)
    nextq_easy.place(relx=0.39, rely=0.9)
    
    

#ans1 is the solving Entry (solving =Entry(f3)) for the easy questions
def submt(ans1):
    global score, count
    if ans1.get() == str(resulteasyq()):
        correct = Label(text="Correct", fg="green", font=("Courier", 16))
        correct.place(relx=0.3, rely=0.2)
        ans1.delete(0,'end')
        score = score+1
        count = count+1
        print("your score is", score)
        
    else:
        wrong = Label(text="Wrong", fg="red", font=("Courier", 16))
        wrong.place(relx=0.3, rely=0.2)
        ans1.delete(0,'end')
        count = count+1
        
#Scoreboard is displayed after 10 questions
    if count == 11:
        scoreboard()


    else: 
        pass

    

#Displays the math question by selecting two random values from the "num" list
def nextq_easy():
    global easyqpage
    start.destroy()
    nextq_easy.easyq1update = random.choice(easyq)
    nextq_easy.easyq2update = random.choice(easyq)
    question = Label(text=f"{nextq_easy.easyq1update}+{nextq_easy.easyq2update}", font=("Courier"))
    question.place(y=5, x=15)
    


    

#This displays to the user if they got the answer right or wrong
def resulteasyq():
    nextq_easy

    return nextq_easy.easyq1update + nextq_easy.easyq2update

    

######################################### Medium questions page:  [This should be a seperate class] ###############################################


def mediumqpage():
    pass


















###################################################### Button command to difficulty selection page:######################################

def difficultypage():
    f2=Frame()
    f2.place(x=0,y=0,width=700,height=400)
    

    label2=Label(f2, text="SELECT LEVEL:", font = "Helvetica 60 bold")
    label2.place(y=50, x=100)

    
    b2=Button(f2, text="EASY", width=14, height=7, command=easyqpage, highlightbackground="yellow")
    b2.place(y=160, x=30)
    Font_Tuple2 = ("helvetica", 20, "bold")
    b2.configure(font= Font_Tuple2)

    b3=Button(f2,text="MEDIUM", width=14, height=7, command=scoreboard, highlightbackground="orange")
    b3.place(x=260, y=160)
    Font_Tuple3 = ("helvetica", 20, "bold")
    b3.configure(font= Font_Tuple3)

    b4=Button(f2,text="HARD", width=14, height=7, highlightbackground="red")
    b4.place(x=490, y=160)
    Font_Tuple4 = ("helvetica", 20, "bold")
    b4.configure(font= Font_Tuple4)


###################################################### First frame where user enters their name #########################################


f1=Frame(bg="light green")
f1.place(x=0,y=0,width=700,height=400)

label1=Label(text="ENTER YOUR NAME", font = "Helvetica 60 bold", bg="light green")
label1.place(y=70, x=50)

usersname=Entry(f1, font = "Helvetica 40 bold")
usersname.place(y=170,x=190, height=75, width=300)

b1=Button(f1, text="NEXT", width= 10, height=2 , command=difficultypage)
b1.place(y=300, x=480)
Font_Tuple1 = ("helvetica", 20, "bold")
b1.configure(font= Font_Tuple1)


root.resizable(False,False)
root.mainloop()
