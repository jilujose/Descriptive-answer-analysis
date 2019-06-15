from Tkinter import *
import sys
import Tkinter as tk
import new
sys.path.append("main.py")


class App(Frame):
    def run_script(self):
        sys.stdout = self
        try:
            del(sys.modules["Descriptive Answer Analysis"])
        except:
            pass
            import main
            
    def build_widgets(self):
        self.text1 = Text(self)
        self.text1.pack(side=TOP)
        self.button = Button(self)
        self.button["text"] = "Run"
        self.button["command"] = self.run_script
        self.button.pack(side=TOP)

    def write(self, txt):
        self.text1.insert(INSERT, txt)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.build_widgets()

    def on_button(self):
        print(self.entry.get())
    
#new part

    def show_entry_fields():
        print("Enter student filename: %s" % (new.img.get()))
        new.img = new.img.get()
    master = tk.Tk()
    tk.Label(master, 
         text="Enter student filename").grid(row=0)
    new.img = tk.Entry(master)
    new.img.grid(row=0, column=1)
    tk.Button(master, 
          text='Enter', command=show_entry_fields).grid(row=3, 
                                                       column=0, 
                                                       sticky=tk.W, 
                                                       pady=4)
    tk.Button(master, 
          text='Next', 
          command=master.quit).grid(row=3, 
                                    column=1, 
                                    sticky=tk.W, 
                                    pady=4)

    tk.mainloop()

    def show_entry_fields():
        print("Enter Answerkey name: %s" % (new.tea.get()))
        new.tea = new.tea.get()
    master = tk.Tk()
    tk.Label(master, 
         text="Enter Answerkey name").grid(row=0)
    new.tea = tk.Entry(master)
    new.tea.grid(row=0, column=1)
    tk.Button(master, 
          text='Enter', command=show_entry_fields).grid(row=3, 
                                                       column=0, 
                                                       sticky=tk.W, 
                                                       pady=4)
    tk.Button(master, 
          text='Next', 
          command=master.quit).grid(row=3, 
                                    column=1, 
                                    sticky=tk.W, 
                                    pady=4)

    tk.mainloop()

root = Tk()
app = App(master = root)
app.mainloop()
