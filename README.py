import tkinter as tk

class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Python Calculator")
        self.equation = tk.StringVar()
        self.create_ui()

    def create_ui(self):
        entry = tk.Entry(self, textvariable=self.equation, width=36, borderwidth=5)
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'C', '0', '=', '/'
        ]

        row, col = 1, 0
        for button in buttons:
            tk.Button(self, text=button, width=9, command=lambda b=button: self.click_button(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click_button(self, value):
        if value == '=':
            try:
                result = str(eval(self.equation.get()))
                self.equation.set(result)
            except:
                self.equation.set("Error")
        elif value == 'C':
            self.equation.set('')
        else:
            current_equation = self.equation.get()
            current_equation += value
            self.equation.set(current_equation)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
