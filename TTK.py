import customtkinter
from tkinter import ttk


def monstrar_Command():
    print((entry.get()))

janela = customtkinter.CTk()
janela.title("1,2,3")
janela.geometry("400x300")

label = ttk.Label(janela,text="Caveirinha games",font=("Couvier",16))
label.pack(pady=10)

entry = ttk.Entry(janela,font=("Couvier",16))
entry.pack(pady=10)

button = ttk.Button(janela,text="Mostrar Comando", command=monstrar_Command)

janela.mainloop()

