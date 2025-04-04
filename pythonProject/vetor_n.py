import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

janela =  customtkinter.CTk()
janela.title("Estoque")
janela.geometry("800x400")

Frame1= customtkinter.CTkFrame(janela,fg_color="Red",width=190, height=380)
Frame1.grid_propagate(False)
Frame1.grid(padx=10,pady=10,row=0,column=0)

Frame2= customtkinter.CTkFrame(janela, fg_color="Yellow", width=590, height=380)
Frame2.grid_propagate(False)
Frame2.grid(padx=10,pady=10,row=0, column=1)

Label_Titulo1= customtkinter.CTkLabel(Frame1, width=190, text="Estoque", text_color="Black", font=("Couvier",18))
Label_Titulo1.grid(padx=10,pady=20,row=0, column=0)

B_Cadastrar= customtkinter.CTkButton(Frame1,text="Cadastrar", font=("Couvier",16), corner_radius=0)
B_Cadastrar.grid(pady=5, row=1, column=0)

B_editar= customtkinter.CTkButton(Frame1, text="editar", font=("Couvier",16), corner_radius=0)
B_editar.grid(pady=5,row=2,column=0)

B_saida= customtkinter.CTkButton(Frame1, text="Saída", font=("Couvier",16), corner_radius=0)
B_saida.grid(pady=5,row=3,column=0)

B_Entrada= customtkinter.CTkButton(Frame1, text="Entrada", font=("Couvier",16), corner_radius=0)
B_Entrada.grid(pady=5,row=4,column=0)

B_Relatorio= customtkinter.CTkButton(Frame1, text="Relátorio", font=("Couvier",16), corner_radius=0)
B_Relatorio.grid(pady=5,row=5,column=0)

Titulo_cadastro= customtkinter.CTkLabel(Frame2, text="Cadastrar", text_color="Purple", font=("Couvier",18), corner_radius=0)
Titulo_cadastro.grid(padx=70,pady=20,row=0,column=0)

Titulo_nome= customtkinter.CTkLabel(Frame2, text="Nome do produto:", text_color="Purple", font=("Couvier",18))
Titulo_nome.grid(padx=5,pady=5,row=1,column=0)

nome_produto= customtkinter.CTkEntry(Frame2, placeholder_text="Nome cadastrado do produto:", font=("Couvier",18),corner_radius=0,width=300)
nome_produto.grid(padx=5,pady=5,row=1,column=1)

Titulo_Preco= customtkinter.CTkLabel(Frame2, text="Nome do produto:", text_color="Purple", font=("Couvier",18))
Titulo_Preco.grid(padx=5,pady=5,row=2,column=0)

Preco= customtkinter.CTkEntry(Frame2, placeholder_text="Preço R$:", font=("Couvier",18))
Preco.grid(padx=5,pady=5,row=2,column=1, sticky="w")

Titulo_descricao= customtkinter.CTkLabel(Frame2, text="Descrição:", text_color="Purple", font=("Couvier",18))
Titulo_descricao.grid(padx=5,pady=5,row=3,column=0)

descricao= customtkinter.CTkTextbox(Frame2)
descricao.grid( pady=5,row=3,column=1)

janela.mainloop()