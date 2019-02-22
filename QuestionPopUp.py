from tkinter import *
from tkinter import messagebox
import CheckAnswerFunction as caf
import KeyAndQuestion as kaq
import MakeName as mn

def makeform(root, question):
    row = Frame(root)
    lab = Label(row, width=len(question), text=question, anchor='w')
    ent = Entry(row)
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    lab.pack(side=LEFT)
    ent.pack(side=RIGHT, expand=YES, fill=X)
    entries = (question, ent)
    return entries
    
def check(index, entry, key):
    text = entry[1].get()
    re = caf.checkAns(index, text)
    if(re == True):
        messagebox.showinfo("Congratulation", "Great Job!")
    else:
        messagebox.showinfo("Uh Oh!", "Sorry, you're wrong.")

def makeWindow(index, limit):
    root = mn.makeName('root', index)
    root = Tk()
    question = kaq.findQuestion(index)[1]
    ents = makeform(root, question)
    if(index < limit):
        b1 = Button(
                root,
                text='Check',
                command= (lambda: (check(index, ents, key), root.destroy(), makeWindow(index+1, limit)))
                )
        b1.pack(side = BOTTOM , padx=5, pady=5)
    else:
        b2 = Button(
                root,
                text='Check',
                command= (lambda: (check(index, ents, key), root.destroy()))
                )
        b2.pack(side = BOTTOM , padx=5, pady=5)
    root.mainloop()

#makeWindow(1, kaq.countQuestion())
