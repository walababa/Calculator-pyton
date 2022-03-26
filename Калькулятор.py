#Calculator by walababa
from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#808080", foreground="#FFF")
        self.lbl.place(x=10, y=20)

        btns = [
            "C", "DEL", "X^2", "+",
            "1", "2", "3", "-",
            "4", "5", "6", "*",
            "7", "8", "9", "/",
            "(", "0", ")", "="
        ]

        x = 10
        y = 70
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#cccccc",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=50,
                                      height=50)
            x += 50
            if x > 200:
                x = 10
                y += 50

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#808080"
    root.geometry("220x330+200+200")
    root.title("Calc")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()