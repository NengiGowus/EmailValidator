import tkinter
from tkinter import *
root = tkinter.Tk()
root.title("Email Validator")
def checkemail(email):
                                checka = '@'
                                checkb = '.'
                                checkc = 'com'
                                checkd = 'gmail'
                                checke= 'outlook'
                                checkf= 'yahoo'
                                if checka in email:
                                                if checkb in email:
                                                                if checkc in email:
                                                                                if checkd in email:
                                                                                                eil = "Your gmail is verified"
                                                                                                labelE.config(text=eil)
                                                                
                                                                                elif checke in email:
                                                                                                
                                                                                                labelE.config(text="Your outlook email is verified")
                                                                                elif checkf in email:
                                                                                                
                                                                                                labelE.config(text="Your yahoo email is verified")
                                                                                else:
                                                                                
                                                                                                labelE.config(text="Your email could not be verified as gmail, outlook or yahoo, please try again")

                                                                else:
                                                                                labelE.config(text="Your email does not contain the word 'com'")
                                                else:
                                                                labelE.config(text="Your email does not contain '.'")
                                else:
                                                labelE.config(text="Your email does not contain the '@' symbol")
def click(bleh):
                email = enter.get()
                checkemail(email)
def clear():
                enter.delete(0,END)
                labelE.config(text="")

canvasE = Canvas(width=400,height=100,relief='raised')
canvasE.pack()
lab = Label(root,text="Enter your email:",font=('times',16))
canvasE.create_window(100,30,window=lab)
enter = Entry(root)
bleh = ""
enter.bind('<Return>',click)
canvasE.create_window(90,60,window=enter)
validateButton = Button(root,text='Validate',command=click,width=8,height=1)
canvasE.create_window(40,90,window=validateButton)
labelE = Label(root,text="",font=('times',9))
canvasE.create_window(250,60,window=labelE)
clrButton = Button(root,text="Clear",command=clear)
canvasE.create_window(100,90,window=clrButton)
#print("Enter your email")
#email = input("Here: ")
#checkemail(email)

root.mainloop()
                                                                                
                       
