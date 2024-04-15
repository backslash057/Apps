import tkinter as tk
import customtkinter as ctk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

class Panel(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.padx, self.pady = 40, 20
        self.inputs = []
        self.outputs = []

        self.title = tk.Label(self, text="New Diagram", bg=self.cget("bg"), font=("Calibri", 18, "bold"), fg="#FFFFFF")
        self.title.pack(anchor="nw", padx=self.padx)

        self.canvas = tk.Canvas(self, bg=self.cget("bg"), highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", self.update)
        
        self.display()

    def display(self):
        w, h = int(self.cget("width")), int(self.cget("height"))
        self.bg = self.canvas.create_rectangle(self.padx, 0, w-self.padx, h-self.pady, width=4, outline="#6C6C6E")
        

    def update(self, event):
        self.canvas.coords(self.bg, self.padx, 0, event.width-self.padx, event.height-self.pady)



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btns = ["AND", "NOT", "OR", "NOR", "NAND", "XOR", "ALU"]

        self.geometry("900x900")
        self.config(bg="#1D1D20")

        self.title("Binary magic")

        self.addWidgets()
        

    def addWidgets(self):
        panel = Panel(self, bg="#363538", highlightthickness=0)
        panel.pack(fill="both", expand=True)

        bar = tk.Frame(self, pady=5)
        bar.config(bg=bar.master.cget("bg"))
        bar.pack(fill="x")

        font = ("Consolas", 12)
        menuBtn = tk.Label(bar, text="Menu", bg="#466896", fg="#E3FDFF", font=("Consolas", 15, "bold"))
        menuBtn.config(padx=5, cursor="hand2")
        menuBtn.pack(side="left", padx=(10, 0))

        for btnName in self.btns:
            btn = tk.Label(bar, text=btnName, bg="#303030", fg="#FFFFFF", padx=5, pady=5, font=font)
            btn.config(cursor="hand2")
            btn.pack(side="left", padx=(10, 0))


app = App()
app.mainloop()