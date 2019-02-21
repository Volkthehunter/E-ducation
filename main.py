#%%
from tkinter import filedialog
import tkinter as tk 
from Viewer import viewers
view_on=0
a=''
root = tk.Tk()
root.wm_title("E-ducation")
#%%
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.width = 12000
        self.height = 600
        self.pack()
        self.create_widgets()
    def browse_file(self):
        fname = filedialog.askopenfilename(filetypes = (('Word files',"*.docx"),('Ebook files',"*.epub"),("pdf files","*.pdf"),("All files","*")))
        a=fname
        self.openviewer()
        return fname
    def create_widgets(self):
        self.browse = tk.Button(master = root, text = 'Select a book', width = 60)
        self.browse['command'] = self.browse_file
        self.browse.pack(side=tk.LEFT, padx = 2, pady=0)
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.settime = tk.Entry(self,text = 'Settime hour,minute')
        self.settime.pack(side='right')
    def openviewer(self):
        #runfile 
        viewer = tk.Tk()
        viewer.wm_title('Viewer')
        viewer = viewers(master=viewer)
#%%
master = Application(master=root)
master.mainloop()