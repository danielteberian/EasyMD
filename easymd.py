from tkinter import *
from tkinter import font , filedialog
from markdown2 import Markdown
from tkhtmlview import HTMLLabel

class Window(Frame):
   def __init__(self, master=None):
      Frame.__init__(self, master)
      self.master = master
      self.myfont = font.Font(family="Helvetica", size=14)
      self.init_window()

   def init_window(self):
      self.master.title("EasyMD")
      self.pack(fill=BOTH, expand=1)



root = Tk()
root.geometry("700x600")
app = Window(root)
app.mainloop()
