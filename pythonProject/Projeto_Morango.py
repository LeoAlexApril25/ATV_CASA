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

customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('blue')

janela = customtkinter.CTk()
janela.title('Projeto Morango')
janela.geometry('1200x720')

Label_X=customtkinter.CTkLabel(janela,text='Calcular morango',font=('Arial',20),text_color='red',)
Label_X.pack(pady=20)

Nome=customtkinter.CTkEntry(janela,placeholder_text='Nome do produtor:')
Nome.pack(pady=20)

Tipo_Morango=customtkinter.CTkEntry(janela,placeholder_text='Tipo do morango:')
Tipo_Morango.pack(pady=20)

Peso_Morango=customtkinter.CTkEntry(janela,placeholder_text='Kilos do morango(Kg)')
Peso_Morango.pack(pady=20)

botao=customtkinter.CTkButton(janela,text='Clique aqui',command=soma,font=('Arial',15),text_color='green')
botao.pack(pady=20)

Label_A=customtkinter.CTkLabel(janela,text='O nome do Produtor que vai receber o pagamento é:',font=('Arial',15),text_color='red')
Label_A.pack(pady=20
             )
Label_Y=customtkinter.CTkLabel(janela,text='Resultado do peso é :',font=('Arial',15),text_color='red')
Label_Y.pack(pady=20)

Label_Z=customtkinter.CTkLabel(janela,text='O valor do morango doce é:',font=('Arial',15),text_color='red')
Label_Z.pack(pady=20)

janela.mainloop()
