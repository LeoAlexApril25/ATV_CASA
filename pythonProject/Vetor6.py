import customtkinter
def soma():
   var_nome=Nome.get()
   var_tipo=Tipo_Morango.get()
   Label_A.configure(text=f'O nome de do Produtor que vai receber o pagamento é: {var_nome}')
   Label_Y.configure(text=f'O tipo do morango é: {var_tipo}')
   Nome.delete(0,'end')
   Tipo_Morango.delete(0,'end')

   if var_tipo == 'Sujo':
      var_peso=float(Peso_Morango.get())*3.50
      Label_Z.configure(text=f'A quantidade em dinheiro que o Agricultor vai receber no morango sujo  é de: R$ {var_peso:.2f}')
      Peso_Morango.delete(0, 'end')
   elif var_tipo == 'Limpo':
       var_peso=float(Peso_Morango.get())*5.00
       Label_Z.configure(text=f'A quantidade em dinheiro que Agricultor vai receber no morango limpo é de: R${var_peso:.2f}')
       Peso_Morango.delete(0, 'end')


def resultado1():
    Frame02.pack_propagate(False)
    Frame03.grid_forget()
    Frame02.grid(row=0, column=1)

def resultado2():
    Frame03.pack_propagate(False)
    Frame02.grid_forget()
    Frame03.grid(row=0, column=1)


janela = customtkinter.CTk()
janela.title("Home")
janela.geometry("1920x1080")

Frame01 = customtkinter.CTkFrame(janela, fg_color="red", width=1080, height=720, corner_radius=0)
Frame01.pack_propagate(False)
Frame01.grid(row=0, column=0)

Frame02 = customtkinter.CTkFrame(janela, fg_color="blue", width= 1080, height= 720, corner_radius=0)
Frame02.pack_propagate(False)
Frame02.grid(row=0, column=1)

Frame03 = customtkinter.CTkFrame(janela, fg_color="dark red", width=1080, height=720, corner_radius=0)
Frame03.pack_propagate(False)
Frame03.grid(row=0, column=1)

Label_X=customtkinter.CTkLabel(Frame02,text='Calcular morango',font=('Arial',20),text_color='red',height=636)
Label_X.grid(padx=20,pady=0,row = 0, column=0, columnspan=1)

Nome=customtkinter.CTkEntry(Frame02,placeholder_text='Nome do produtor:', width=350)
Nome.grid(padx=5,pady=0,row = 1, column=1,stick="w")

Tipo_Morango=customtkinter.CTkEntry(Frame02,placeholder_text='Tipo do morango:',width=350)
Tipo_Morango.grid(padx=5,pady=0,row = 2, column=1,stick="w")

Peso_Morango=customtkinter.CTkEntry(Frame02,placeholder_text='Kilos do morango(Kg)',width=350)
Peso_Morango.grid(padx=5,pady=0,row =3 , column=1,stick="w")

Botao01 = customtkinter.CTkButton(Frame01, text="Inserir dados", command = resultado1,font=('Arial',15),text_color='green')
Botao01.grid(padx=5,pady=0,row = 2, column=1)

botao02=  customtkinter.CTkButton(Frame01,text='Clique aqui',command=soma,font=('Arial',15),text_color='green')
botao02.grid(padx=5,pady=0,row = 2, column=1)

Botao03 = customtkinter.CTkButton(Frame01, text="Resultado do pagamento", command= resultado2,font=('Arial',18),text_color='green')
Botao03.grid(padx=5,pady=0,row = 2, column=1)

Label_A=customtkinter.CTkLabel(Frame01,text='O nome do Produtor que vai receber o pagamento é:',font=('Arial',18),text_color='white')
Label_A.grid(padx=5,pady=0,row = 2, column=1)

Label_Y=customtkinter.CTkLabel(Frame01,text='Resultado do peso é :',font=('Arial',15),text_color='white')
Label_Y.grid(padx=5,pady=0,row = 2, column=1)

Label_Z=customtkinter.CTkLabel(Frame01,text='O valor do morango doce é:',font=('Arial',15),text_color='white')
Label_Z.grid(padx=5,pady=0,row = 2, column=1)



janela.mainloop()

