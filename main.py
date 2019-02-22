#%%
from tkinter import filedialog
import tkinter as tk 
view_on=0
expired = 0
a=''
root = tk.Tk()
root.wm_title("E-ducation")
#%%
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.width =100
    def browse_file(self):
        fname = filedialog.askopenfilename(filetypes = (('Word files',"*.docx"),('Text files',"*.txt"),('Ebook files',"*.epub"),("pdf files","*.pdf"),("All files","*")))
        self.openviewer()
        self.filelocation=fname
        viewer = ebookviewers(master=master)
        return fname
    def create_widgets(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side=tk.RIGHT,padx=0,pady=0  )
        self.browse = tk.Button(master = root, text = 'Select a book', width = 20,height=40)
        self.browse['command'] = self.browse_file
        self.browse.pack(side=tk.LEFT, padx = 0, pady=0)
        
        self.settime = tk.Entry(self)
        self.settime.pack(side=tk.RIGHT,padx=200,pady=0)
    def openviewer(self):
        #runfile 
        viewer = ebookviewers(master=master)
        viewer.mainloop()
class ebookviewers(tk.Frame):
    def __init__(self,master = None):
        
        super().__init__(master)
        self.width = 100
        self.master = master
        self.pack()
        
    def create_widgets(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="top")
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side = 'Right',fill='y')
        self.mylist = tk.Listbox(self, yscrollcommand = tk.scrollbar.set ) 
        self.scrollbar.config( command = tk.mylist.yview )
        self.text = 'This is our Message'
        self.messageVar = tk.Message(self, text = self.text) 
        self.messageVar.config(bg='lightgreen') 
        self.messageVar.pack() 


master = Application(master=root)
master.mainloop()