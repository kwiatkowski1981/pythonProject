import tkinter as tk
from tkinter import messagebox


def send_name():
    if first_name.get() == 'kuba':
        messagebox.showinfo(title='ok!', message='Witam Pana!')
    else:
        messagebox.showerror(title='hoojofo', message='who the fuck are u?')


window = tk.Tk()
window.title('PyStart')
window.geometry('600x400')

label = tk.Label(window, text="Jak masz na imię?")
label.pack()

first_name = tk.Entry()
first_name.pack()

button = tk.Button(text="ok", command=send_name)
button.pack()
window.mainloop()
