

import customtkinter
from  tkinter import ttk

coluna_x=["Moragueiro","data","tipo","Peso","Pagamento"]

def registrar():
    FrameX3.grid_forget()
    Framex4.grid_forget()
    Frame2.grid_propagate(False)
    Frame2.grid(pady=0, padx=0, row=1, column=1)

def relatorio():
    Framex4.grid_forget()
    Frame2.grid_forget()
    FrameX3.grid_propagate(False)
    FrameX3.grid(pady=0, padx=0, row=1, column=1)

def saida():
    Frame2.grid_forget()
    FrameX3.grid_forget()
    Framex4.grid_propagate(False)
    Framex4.grid(pady=0, padx=0, row=1, column=1)

customtkinter.set_appearance_mode("Black")
customtkinter.set_default_color_theme("blue")

janela  =  customtkinter.CTk()
janela.title('Pagamento Morango')
janela.geometry("800x400")

Frame1 = customtkinter.CTkFrame(janela,fg_color="Blue",width=210,height=300, corner_radius=0)
Frame1.grid_propagate(False)
Frame1.grid(pady=0,padx=0,row=1,column=0)


Titulo1 = customtkinter.CTkLabel(Frame1, text="Calcular Morango", text_color="Black", font=("Couvier",18))
Titulo1.grid(pady=5,padx=10,row=1,column=0,stick="w")

Registrar = customtkinter.CTkButton(Frame1, text="Registrar", fg_color="Green", font=("Couvier",18), width=100,command=registrar)
Registrar.grid(pady=5,padx=10,row=2,column=0)

Relatorio = customtkinter.CTkButton(Frame1, text="Relatorio", fg_color="Green", font=("Couvier",18), width=100,command=relatorio)
Relatorio.grid(pady=5,padx=10,row=3,column=0)


Sair = customtkinter.CTkButton(Frame1, text=" Saindo ", fg_color="Green", font=("Couvier",18), width=100, command= saida)
Sair.grid(pady=5,padx=10,row=4,column=0)


Frame2 = customtkinter.CTkFrame(janela,fg_color="Gray",width=490,height=300,  corner_radius=0)
Frame2.grid_propagate(False)
Frame2.grid(pady=0,padx=0,row=1,column=1)

Titulo2 = customtkinter.CTkLabel(Frame2, text="Calcular Morango", text_color="Black", font=("Couvier",18))
Titulo2.grid(pady=5,padx=10,row=0, column=1,columnspan=3)

Produtor = customtkinter.CTkEntry(Frame2, placeholder_text="Nome do produtor",width=230)
Produtor.grid(pady=5,padx=0,row=1,column=1, stick='w')

Quantidade_m= customtkinter.CTkEntry(Frame2,placeholder_text="Quantidade de Morango",width=230)
Quantidade_m.grid(pady=5,padx=0,row=2,column=1, stick='w')

Data = customtkinter.CTkEntry(Frame2,placeholder_text="Insira a Data", width=80)
Data.grid(pady=5,padx=10, row=1,column=3, sticky="e")

descricao = customtkinter.CTkTextbox(Frame2,width=170,height=80)
descricao.grid(pady=10,padx=0,row=3,column=1,columnspan=3,sticky="we" )

Salvar = customtkinter.CTkButton(Frame2, text=" Salvar ", fg_color="Green", font=("Couvier",18), width=80, command= saida)
Salvar.grid(pady=5,padx=5,row=4,column=2, stick="w")

Sair2 = customtkinter.CTkButton(Frame2, text=" Sair ", fg_color="Green", font=("Couvier",18), width=80, command= saida)
Sair2.grid(pady=5,padx=5,row=4,column=3, stick="e")

FrameX3 = customtkinter.CTkFrame(janela,fg_color="Red", width=490,height=300, corner_radius=0)
FrameX3.grid_propagate(False)
FrameX3.grid(pady=0,padx=0,row=1,column=1)

Framex4 = customtkinter.CTkFrame(janela,fg_color="White", width=490,height=300, corner_radius=0)
Framex4.grid_propagate(False)
Framex4.grid(pady=0,padx=0,row=1,column=1)

Titulo3 = customtkinter.CTkLabel(FrameX3, text="Relatorio", text_color="Black", font=("Couvier",18))
Titulo3.grid(pady=5,padx=10,row=0,column=0)

Buscar_r= customtkinter.CTkEntry(FrameX3, placeholder_text="Buscar",text_color='Black',font=('Couvier',18),width=250,height=10)
Buscar_r.grid(pady=5,padx=0,row=1,column=0,stick="w")

tabela_M=ttk.Treeview(FrameX3, columns=coluna_x,show='headings', height=5)
tabela_M.heading('Moragueiro',text='Moragueiro')
tabela_M.column('Moragueiro',width=100)


janela.mainloop()