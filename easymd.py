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

      self.inputeditor = Text(self, background="black", foreground="white", width="1" , font=self.myfont)
      self.inputeditor.pack(fill=BOTH, expand=1, side=LEFT)

      self.outputbox = HTMLLabel(self, width="1", background="black", foreground="white",  html="<h1>EasyMD</h1>")
      self.outputbox.pack(fill=BOTH, expand=1, side=RIGHT)
      self.outputbox.fit_height()



root = Tk()
root.geometry("700x600")
app = Window(root)
app.mainloop()

