import tkinter as tk
from tkinter import messagebox
import webbrowser
from tkinter import BOTTOM



class hesapmakinesi:

    def __init__(self, master):
        self.master = master
        master.title("Hesap Makinesi")

        # Ekran
        self.screen = tk.Entry(master, width=25, font=('Arial', 16))
        self.screenf = tk.Label(root, text="InnovateTech | CodeHunter00", fg="#6E7371", cursor="hand2",font="Verdana 7 bold")
        self.screenf.bind("<Button-1>", lambda e: callback(webbrowser.open_new("https://www.instagram.com/kod.arsivim/")))
        self.screen.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
        self.screenf.grid(row=6, column=0, columnspan=4, padx=20, pady=20)

        # Düğmeler
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)

        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)

        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)

        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('C', 4, 2)
        self.create_button('+', 4, 3)

        self.create_button('=', 5, 0, columnspan=4)

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, width=5, height=2,
                           font=('Arial', 14), command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=2, pady=1)

    def button_click(self, text):
        if text == 'C':
            self.screen.delete(0, tk.END)
        elif text == '=':
            self.calculate()
        else:
            self.screen.insert(tk.END, text)

    def calculate(self, error_message="Böyle bir işlem mümkün değil!"):
        try:
            result = eval(self.screen.get())
            self.screen.delete(0, tk.END)
            self.screen.insert(0, result)
        except:
            self.screen.delete(0, tk.END)
            self.screen.insert(0, "")

            def show_error():
                error_message = "Böyle bir işlem mümkün değil!"
                messagebox.showerror("Hata", error_message)
            root = tk.Tk()
            root.title("Hata Penceresi")
            #error_message = "Böyle bir işlem mümkün değil!"
            messagebox.showerror("Hata", error_message)
            root.after(10, root.destroy())









def callback(url):
    webbrowser.open_new(url)



root = tk.Tk()
root.resizable(width=False, height=False)
calc = hesapmakinesi(root)
root.mainloop()
