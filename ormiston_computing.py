from tkinter import *
import random

root = Tk()
root.geometry('700x400')
root.title('Ormiston Computing')      




score = 0
count = 0


class interface:
###################################################### First frame where user enters their name #########################################    


    def __init__(self):
        self.f1=Frame(bg="#7CFC00")
        self.f1.place(x=0,y=0,width=700,height=400)

        self.label1=Label(self.f1, text="ENTER YOUR NAME", font = "Helvetica 60 bold", bg="#7CFC00")
        self.label1.place(y=70, x=50)

        self.usersname=Entry(self.f1, font = "Helvetica 40 bold")
        self.usersname.place(y=170,x=190, height=75, width=300)

        self.b1=Button(self.f1, text="NEXT", width= 10, height=2, command=self.checkentry) 
        self.b1.place(y=300, x=480)
        self.Font_Tuple1 = ("helvetica", 20, "bold")
        self.b1.configure(font= self.Font_Tuple1)

   #validates and checks for user input     
    def checkentry(self):

        self.usersname_text = self.usersname.get()
        if self.usersname_text =="":
            
            self.errormsg=Label(self.f1, text="Name required", font = "Helvetica 15 bold", fg="red", bg="#7CFC00")
            self.errormsg.place(y=260, x=280)

        else:

            self.difficultypage()     
        
###################################################### Button command to difficulty selection page:######################################

   

    def difficultypage(self):
        
        self.f2=Frame(bg="#8A2BE2")
        self.f2.place(x=0,y=0,width=700,height=400)
    
    #widgets
        self.label2=Label(self.f2, text="SELECT LEVEL:", font = "Helvetica 60 bold", bg="#8A2BE2")
        self.label2.place(y=50, x=100)

    
        self.b2=Button(self.f2, text="EASY", width=14, height=7, highlightbackground="yellow", command=self.easyqpage)
        self.b2.place(y=160, x=30)
        self.Font_Tuple2 = ("helvetica", 20, "bold")
        self.b2.configure(font= self.Font_Tuple2)

        self.b3=Button(self.f2,text="MEDIUM", width=14, height=7, highlightbackground="orange", command=self.mediumqpage)
        self.b3.place(x=260, y=160)
        self.Font_Tuple3 = ("helvetica", 20, "bold")
        self.b3.configure(font= self.Font_Tuple3)

        self.b4=Button(self.f2,text="HARD", width=14, height=7, highlightbackground="red", command=self.hardqpage)
        self.b4.place(x=490, y=160)
        self.Font_Tuple4 = ("helvetica", 20, "bold")
        self.b4.configure(font= self.Font_Tuple4)


        #Lists for difficulty levels
        self.easyq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.medq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.hardq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        

################################################################# Easy questions page: ##########################################################################
    def easyqpage(self):
         
         self.f3=Frame(bg="#E0FFFF")
         self.f3.place(x=0,y=0,width=700, height=400)

    #widgets
         self.start = Button(self.f3, text="Start", width=16, height=4, command=self.nextq_easy)
         self.start.place(x=200, y=95)
         self.Font_Tuple6 = ("helvetica", 14, "bold")
         self.start.configure(font= self.Font_Tuple6)

         self.solving = Entry(self.f3, width=7, font = "Helvetica 40 bold")
         self.solving.place(y=90,x=370, height=75, width=100)

         self.submit = Button(self.f3, text="Submit Answer", width=16, height=4, command=lambda: self.submt(self.solving))
         self.submit.place(x=280, y=220)
         self.Font_Tuple5 = ("helvetica", 14, "bold")
         self.submit.configure(font= self.Font_Tuple5)

    
         self.nextq_easy = Button(self.f3, text="Next", width=12, height=3, command=self.nextq_easy)
         self.nextq_easy.place(x=290, y=300)
         self.Font_Tuple5 = ("helvetica", 16, "bold")
         self.nextq_easy.configure(font= self.Font_Tuple5)
    
    

#solving Entry (solving =Entry(f3)) for the easy questions

    def submt(self, solving): 
        global score, count
        if self.solving.get() == str(self.resulteasyq()):
            self.correct = Label(text="CORRECT", fg="green", font=("helvetica", 38), bg="#E0FFFF")
            self.correct.place(x=470, y=120)
            self.submit.config(state=DISABLED)
            self.solving.config(state=DISABLED)
            self.nextq_easy.config(state=NORMAL)
            score = score+1
            count = count+1
           
        
        else:
           self.wrong = Label(text="WRONG", fg="red", font=("helvetica", 38), bg="#E0FFFF")
           self.wrong.place(x=470, y=120)
           self.submit.config(state=DISABLED)
           self.solving.config(state=DISABLED)
           self.nextq_easy.config(state=NORMAL)
           count = count+1


        
        
#Scoreboard is displayed after 10 questions
        if count == 11:
           self.scoreboard()

        else:
           pass

    

#Displays the math question by selecting two random values from the "num" list      CLASS

    def nextq_easy(self):
         self.start.destroy()
         
         self.nextq_easy.config(state=DISABLED)
         self.submit.config(state=NORMAL)
         self.solving.config(state=NORMAL)
         self.solving.delete(0,'end')
         self.cover = Label(text="                   ", fg="green", font=("helvetica", 40), bg="#E0FFFF")
         self.cover.place(x=470, y=120)

         #DEFINE THIS W A NEW FUCNTION THEN ADD THIS TO CLASS AS ENCAPSULATION
         self.nextq_easy.easyq1update = random.choice(self.easyq)
         self.nextq_easy.easyq2update = random.choice(self.easyq)
         self.question = Label(text=f"{self.nextq_easy.easyq1update}+{self.nextq_easy.easyq2update}=", font = "Helvetica 70 bold",bg="#E0FFFF")
         self.question.place(y=80, x=160)
    

#This displays to the user if they got the answer right or wrong   ADD THIS TO A CLASS W A DEF FUNC FOR MED AND HARD
    def resulteasyq(self):
         self.question.destroy()
         self.nextq_easy
         
         return self.nextq_easy.easyq1update + self.nextq_easy.easyq2update






############################################################################## SCOREBOARD ###################################################################################

    def scoreboard(self):
         self.f4=Frame(bg="#FFFF00")
         self.f4.place(x=0,y=0,width=700,height=400)
         
         #Player name displayed on scoreboard
         self.playername=Label(self.f4, text=f"{score}/10", font="Helvetica 100 bold", bg="#FFFF00")
         self.playername.place(x=240, y=140)

         self.newp = Button(self.f4, text="New Player", width=16, height=3, command=interface)
         self.newp.place(y=300, x=500)
         self.Font_Tuple7 = ("helvetica", 16, "bold")
         self.newp.configure(font= self.Font_Tuple7)

         self.home = Button(self.f4, text="HOME", width=16, height=3, command=self.difficultypage)
         self.home.place(y=300, x=50)
         self.Font_Tuple8 = ("helvetica", 16, "bold")
         self.home.configure(font= self.Font_Tuple8)

    

########################################################################## Medium questions page ##########################################################################

    def mediumqpage(self):
         
         self.f3=Frame(bg="#E0FFFF")
         self.f3.place(x=0,y=0,width=700, height=400)

    #widgets
         self.start = Button(self.f3, text="Start", width=16, height=4, command=self.nextq_med)
         self.start.place(x=200, y=95)
         self.Font_Tuple6 = ("helvetica", 14, "bold")
         self.start.configure(font= self.Font_Tuple6)

         self.solving = Entry(self.f3, width=7, font = "Helvetica 40 bold")
         self.solving.place(y=90,x=370, height=75, width=100)

         self.submit = Button(self.f3, text="Submit Answer", width=16, height=4, command=lambda: self.submt(self.solving))
         self.submit.place(x=280, y=220)
         self.Font_Tuple5 = ("helvetica", 14, "bold")
         self.submit.configure(font= self.Font_Tuple5)

    
         self.nextq_med = Button(self.f3, text="Next", width=12, height=3, command=self.nextq_med)
         self.nextq_med.place(x=290, y=300)
         self.Font_Tuple5 = ("helvetica", 16, "bold")
         self.nextq_med.configure(font= self.Font_Tuple5)
    
    

#solving Entry (solving =Entry(f3)) for the easy questions

    def submt(self, solving): 
        global score, count
        if self.solving.get() == str(self.resultmedq()):
            self.correct = Label(text="CORRECT", fg="green", font=("helvetica", 38), bg="#E0FFFF")
            self.correct.place(x=470, y=120)
            self.submit.config(state=DISABLED)
            self.solving.config(state=DISABLED)
            self.nextq_med.config(state=NORMAL)
            score = score+1
            count = count+1
           
        
        else:
           self.wrong = Label(text="WRONG", fg="red", font=("helvetica", 38), bg="#E0FFFF")
           self.wrong.place(x=470, y=120)
           self.submit.config(state=DISABLED)
           self.solving.config(state=DISABLED)
           self.nextq_med.config(state=NORMAL)
           count = count+1


        
        
#Scoreboard is displayed after 10 questions
        if count == 11:
           self.scoreboard()

        else:
           pass

    

#Displays the math question by selecting two random values from the "num" list      CLASS

    def nextq_med(self):
         self.start.destroy()
         
         self.nextq_med.config(state=DISABLED)
         self.submit.config(state=NORMAL)
         self.solving.config(state=NORMAL)
         self.solving.delete(0,'end')
         self.cover = Label(text="                   ", fg="green", font=("helvetica", 40), bg="#E0FFFF")
         self.cover.place(x=470, y=120)

         #DEFINE THIS W A NEW FUCNTION THEN ADD THIS TO CLASS AS ENCAPSULATION
         self.nextq_med.medq1update = random.choice(self.medq)
         self.nextq_med.medq2update = random.choice(self.medq)
         self.question = Label(text=f"{self.nextq_med.medq1update}-{self.nextq_med.medq2update}=", font = "Helvetica 70 bold",bg="#E0FFFF")
         self.question.place(y=80, x=160)
    

#This displays to the user if they got the answer right or wrong   ADD THIS TO A CLASS W A DEF FUNC FOR MED AND HARD
    def resultmedq(self):
         self.question.destroy()
         self.nextq_med
         
         return self.nextq_med.medq1update - self.nextq_med.medq2update



########################################################################## Hard questions page ##########################################################################

    def hardqpage(self):
         
         self.f3=Frame(bg="#E0FFFF")
         self.f3.place(x=0,y=0,width=700, height=400)

    #widgets
         self.start = Button(self.f3, text="Start", width=16, height=4, command=self.nextq_hard)
         self.start.place(x=200, y=95)
         self.Font_Tuple6 = ("helvetica", 14, "bold")
         self.start.configure(font= self.Font_Tuple6)

         self.solving = Entry(self.f3, width=7, font = "Helvetica 40 bold")
         self.solving.place(y=90,x=370, height=75, width=100)

         self.submit = Button(self.f3, text="Submit Answer", width=16, height=4, command=lambda: self.submt(self.solving))
         self.submit.place(x=280, y=220)
         self.Font_Tuple5 = ("helvetica", 14, "bold")
         self.submit.configure(font= self.Font_Tuple5)

    
         self.nextq_hard = Button(self.f3, text="Next", width=12, height=3, command=self.nextq_hard)
         self.nextq_hard.place(x=290, y=300)
         self.Font_Tuple5 = ("helvetica", 16, "bold")
         self.nextq_hard.configure(font= self.Font_Tuple5)
    
    

#solving Entry (solving =Entry(f3)) for the easy questions

    def submt(self, solving): 
        global score, count
        if self.solving.get() == str(self.resulthardq()):
            self.correct = Label(text="CORRECT", fg="green", font=("helvetica", 38), bg="#E0FFFF")
            self.correct.place(x=470, y=120)
            self.submit.config(state=DISABLED)
            self.solving.config(state=DISABLED)
            self.nextq_hard.config(state=NORMAL)
            score = score+1
            count = count+1
           
        
        else:
           self.wrong = Label(text="WRONG", fg="red", font=("helvetica", 38), bg="#E0FFFF")
           self.wrong.place(x=470, y=120)
           self.submit.config(state=DISABLED)
           self.solving.config(state=DISABLED)
           self.nextq_hard.config(state=NORMAL)
           count = count+1


        
        
#Scoreboard is displayed after 10 questions
        if count == 11:
           self.scoreboard()

        else:
           pass

    

#Displays the math question by selecting two random values from the "num" list      CLASS

    def nextq_hard(self):
         self.start.destroy()
         
         self.nextq_hard.config(state=DISABLED)
         self.submit.config(state=NORMAL)
         self.solving.config(state=NORMAL)
         self.solving.delete(0,'end')
         self.cover = Label(text="                   ", fg="green", font=("helvetica", 40), bg="#E0FFFF")
         self.cover.place(x=470, y=120)

         #DEFINE THIS W A NEW FUCNTION THEN ADD THIS TO CLASS AS ENCAPSULATION
         self.nextq_hard.hardq1update = random.choice(self.hardq)
         self.nextq_hard.hardq2update = random.choice(self.hardq)
         self.question = Label(text=f"{self.nextq_hard.hardq1update}×{self.nextq_hard.hardq2update}=", font = "Helvetica 70 bold",bg="#E0FFFF")
         self.question.place(y=80, x=160)
    

#This displays to the user if they got the answer right or wrong   ADD THIS TO A CLASS W A DEF FUNC FOR MED AND HARD
    def resulthardq(self):
         self.question.destroy()
         self.nextq_hard
         
         return self.nextq_hard.hardq1update * self.nextq_hard.hardq2update


    





interface()




root.resizable(False,False)
root.mainloop()
