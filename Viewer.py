# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:38:00 2019

@author: Pongpanot
"""
import tkinter as tk 

class viewers(tk.Frame):
    def __init__(self,master = None):
        from main import a
        document = Document(a)
        super().__init__(master)
        self.master = master
        self.pack()
        T = Text(root,state='normal',height=15,width=60)
        T.pack()
        T.insert(END,open(a).read())
    def create_widgets(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="top")
    def answerquestion(self):
        Quiz =Quizbox()
        '''
class Quizbox(tk.Frame):
    def __init__(self, master=master):
        pass
'''