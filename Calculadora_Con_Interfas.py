import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.resultado_var = tk.StringVar()
        self.resultado_var.set("")

        self.entry = tk.Entry(master, textvariable=self.resultado_var, justify="right", font=("Arial Black", 18))
        self.entry.grid(row=0, column=0, columnspan=4, sticky="ew")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(master, text=text, font=("Arial", 18), command=lambda t=text: self.pulsar(t))
            button.grid(row=row, column=col, sticky="nsew")

        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
        for j in range(4):
            master.grid_columnconfigure(j, weight=1)

    def pulsar(self, tecla):
        if tecla == "=":
            try:
                resultado = str(eval(self.resultado_var.get()))
                self.resultado_var.set(resultado)
            except Exception as e:
                self.resultado_var.set("Error")
        else:
            self.resultado_var.set(self.resultado_var.get() + tecla)

root = tk.Tk()
app = Calculadora(root)
root.geometry("400x500")
root.mainloop()