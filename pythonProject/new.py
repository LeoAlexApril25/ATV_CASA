import customtkinter
item_vet = 0
customtkinter.set_appearance_mode("Dark")

janela = customtkinter.CTk()
janela.geometry("800x400")
janela.title("gerenciamento de maquinas agriculas")


items2 = ["ola,mundo" , "mundo" ,"oi,mundo","bao,mundo" ,"opa,mundo", "ola"]





def abrir_frame2():
    # fechar frames
    frame4.grid_forget()
    frame5.grid_forget()
    frame6.grid_forget()
    frame7.grid_forget()
    frame8.grid_forget()
    frame9.grid_forget()

    #abrir frame
    frame2.grid_propagate(False)
    frame2.grid(row=0, column=1, padx=5, pady=5)


def abrir_frame4():
    frame2.grid_forget()
    frame5.grid_forget()
    frame6.grid_forget()
    frame7.grid_forget()
    frame8.grid_forget()
    frame9.grid_forget()
    frame4.grid_propagate(False)
    frame4.grid(row=0, column= 1,padx=5,pady=10)


def abrir_frame5():
    frame2.grid_forget()
    frame4.grid_forget()
    frame6.grid_forget()
    frame7.grid_forget()
    frame8.grid_forget()
    frame9.grid_forget()
    frame5.grid_propagate(False)
    frame5.grid(row=0, column=1, padx=5, pady=10)


def abrir_frame6():
    frame2.grid_forget()
    frame4.grid_forget()
    frame5.grid_forget()
    frame7.grid_forget()
    frame8.grid_forget()
    frame9.grid_forget()
    frame6.grid_propagate(False)
    frame6.grid(row=0, column=1, padx=5, pady=10)


def abrir_frame7():
    frame2.grid_forget()
    frame4.grid_forget()
    frame5.grid_forget()
    frame6.grid_forget()
    frame8.grid_forget()
    frame9.grid_forget()
    frame7.grid_propagate(False)
    frame7.grid(row=0, column=1, padx=5, pady=10)

def abrir_frame8():
    frame7.grid_forget()
    frame9.grid_forget()
    frame8.grid_propagate(False)
    frame8.grid(row=0, column=1, padx=5, pady=10)

def abrir_frame9():
    frame7.grid_forget()
    frame8.grid_forget()
    frame9.grid_propagate(False)
    frame9.grid(row=0, column=1, padx=5, pady=10)

popup = None

def abrir_poppup():
    global popup
    if popup is None or not popup.winfo_exists():
        popup = customtkinter.CTkToplevel()
        popup.geometry("590x380")
        popup.title("popup")


        label_relatorio = customtkinter.CTkLabel(popup,text="Escolher relatório(s):",text_color="#A8B30F")
        label_relatorio.grid(row=1,column=0,pady=20,padx=20,sticky="w")

        exportar_estoque = customtkinter.CTkCheckBox(popup, text="Exportar Estoque")
        exportar_estoque.grid(row=2, column=0,pady=20, padx=20, sticky="w")

        exportar_saida = customtkinter.CTkCheckBox(popup, text="Exportar Saída")
        exportar_saida.grid(row=3, column=0,pady=20, padx=20, sticky="w")

        exportar_entrada = customtkinter.CTkCheckBox(popup, text="Exportar Entrada")
        exportar_entrada.grid(row=4, column=0,pady=20, padx=20, sticky="w")

        #titulo escolher extenção

        label_extencao = customtkinter.CTkLabel(popup,text="Escolher extensão:",text_color="#A8B30F")
        label_extencao.grid(row=1,column=2,pady=20,padx=100,sticky="w")

        # Caixas para formatos de arquivo
        formato_word = customtkinter.CTkCheckBox(popup, text="Word")
        formato_word.grid(row=2, column=2,pady=20, padx=100, sticky="w")

        formato_pdf = customtkinter.CTkCheckBox(popup, text="PDF")
        formato_pdf.grid(row=3, column=2,pady=20, padx=100, sticky="w")

        formato_excel = customtkinter.CTkCheckBox(popup, text="Excel")
        formato_excel.grid(row=4, column=2,pady=20, padx=100, sticky="w")

        # botoes

        salvar_popup = customtkinter.CTkButton(popup,text="salvar",width=100)
        salvar_popup.grid(row=5,column=2,pady=5,padx=0,sticky="w")

        cancelar_popup = customtkinter.CTkButton(popup,text="cancelar",width=100)
        cancelar_popup.grid(row=5,column=1,pady=5,padx=20,sticky="w")

        popup.protocol("WM_DELETE_WINDOW", fechar_popup)
        popup.attributes("-topmost", 1) # garante que propup fica na frente
    else:
        popup.lift()

def fechar_popup():
    global popup
    if popup is not None:
        popup.destroy()
        popup = None



frame1 = customtkinter.CTkFrame(janela,width=190,height=380,corner_radius=0,fg_color="Gray")
frame1.grid_propagate(False)
frame1.grid(row=0, column= 0,padx=5,pady=10)


frame2 = customtkinter.CTkFrame(janela,width=590,height=380,corner_radius=0,fg_color="Gray")
frame2.grid_propagate(False)
frame2.grid(row= 0,column=1,padx=5,pady=5)

frame4 = customtkinter.CTkFrame(janela,width=590,height=380,corner_radius=0,fg_color="Gray")
frame4.grid_propagate(False)

mensagem_frame4 = customtkinter.CTkLabel(frame4, text="Tela de Edição de Produto", font=("Couvier", 18, "bold"), text_color="#A8B30F")
mensagem_frame4.grid(pady=20, padx=0, row=0, column=0,columnspan=4)

#rowspan, columnspan e sticky


frame5 = customtkinter.CTkFrame(janela,width=590,height=380,corner_radius=0,fg_color="Gray")
frame5.grid_propagate(False)

mensagem_frame5 = customtkinter.CTkLabel(frame5, text="Tela de Saída", font=("Couvier", 18, "bold"), text_color="#A8B30F")
mensagem_frame5.grid(pady=0,padx=0, row=0, column=1)

frame6 = customtkinter.CTkFrame(janela,width=590,height=380,corner_radius=0,fg_color="Gray")
frame6.grid_propagate(False)

mensagem_frame6 = customtkinter.CTkLabel(frame6, text="Tela de Entrada", font=("Couvier", 18, "bold"), text_color="#A8B30F")
mensagem_frame6.grid(pady=0,padx=0, row=0, column=1)

frame7 = customtkinter.CTkFrame(janela,width=590,height=380,corner_radius=0,fg_color="Gray")
frame7.grid_propagate(False)

mensagem_frame7 = customtkinter.CTkLabel(frame7, text="Tela de Relatório",font=("Couvier", 18, "bold"), text_color="#A8B30F")
mensagem_frame7.grid(pady=30,padx=30, row=0, column=0,columnspan=4)

mensagem = customtkinter.CTkLabel(frame2,text="Cadastro do Produto",font=("Couvier", 18, "bold"),text_color="#A8B30F")
mensagem.grid(pady=30,padx=40,row=0,column=1)

mensagem2 = customtkinter.CTkLabel(frame2,text="Nome do produto:",text_color="#A8B30F",font=("Couvier", 15, "bold"))
mensagem2.grid(padx=40,row=1,column=0)

mensagem3 = customtkinter.CTkLabel(frame2,text="Preço (R$):",text_color="#A8B30F",font=("Couvier", 15, "bold"))
mensagem3.grid(padx=40,row=2,column=0,sticky="ne")

mensagem4 = customtkinter.CTkLabel(frame2,text="Descrição:",text_color="#A8B30F",font=("Couvier", 15, "bold"))
mensagem4.grid(padx=40,row=3,column=0,sticky="ne")


produto = customtkinter.CTkEntry(frame2,placeholder_text="Digite o nome do produto:",width=300,text_color="#A8B30F")
produto.grid(row=1,column=1,padx=5,pady=5)

preco = customtkinter.CTkEntry(frame2,placeholder_text="00.0",width=80,text_color="#A8B30F")
preco.grid(row=2,column=1,padx=5,pady=5,sticky="w")

descricao = customtkinter.CTkTextbox(frame2,width=300,height=80,text_color="#A8B30F")
descricao.grid(row=3,column=1,sticky="")

salvar = customtkinter.CTkButton(frame2,text="Salvar",width=80,text_color="#A8B30F",fg_color="black",hover_color="Green")
salvar.grid(row=4,column=1,pady=5,padx=5,sticky="e")

mensagem5 = customtkinter.CTkLabel(frame1,text="Strawberry Management",width=100,font=("Couvier",15,"bold"),text_color="#A8B30F")
mensagem5.grid(pady=35, padx=10,row=1,column=0)

botao1 = customtkinter.CTkButton(frame1,text="Cadastrar",text_color="#A8B30F",fg_color="black",hover_color="Green",command=abrir_frame2)
botao1.grid(pady=5,padx=5)

botao2 = customtkinter.CTkButton(frame1,text="Editar",text_color="#A8B30F",fg_color="black",hover_color="Green",command=abrir_frame4)
botao2.grid(pady=5,padx=5)

botao3=customtkinter.CTkButton(frame1,text="Saida",text_color="#A8B30F",fg_color="black",hover_color="Green",command=abrir_frame5)
botao3.grid(pady=5,padx=5)

botao4=customtkinter.CTkButton(frame1,text="Entrada",text_color="#A8B30F",fg_color="black",hover_color="Green",command=abrir_frame6)
botao4.grid(pady=5,padx=5)

botao5=customtkinter.CTkButton(frame1,text="Relatorio",text_color="#A8B30F",fg_color="black",hover_color="Green",command=abrir_frame7)
botao5.grid(pady=5,padx=5)

# frame 4, editar

lista_editar = customtkinter.CTkScrollableFrame(frame4)
lista_editar.grid(pady=0,padx=20,row=2,column=0,rowspan=4)

items = ["ola,mundo" , "ola,mund2o" ,"ola,mundo","ola,mundo" ,"ola,mundo", "ola,mundo"]

for items in items:
    box = customtkinter.CTkCheckBox(lista_editar,text=items)
    box.grid(pady=5)

pesquisa_editar = customtkinter.CTkEntry(frame4,placeholder_text="pesquisar por produto",width=250)
pesquisa_editar.grid(row=1, column=0, pady=20, padx=20,columnspan=4,sticky="w")

nome_do_produto = customtkinter.CTkEntry(frame4,placeholder_text="nome do produto",width=200)
nome_do_produto.grid(pady=0,padx=5,row=2,column=1,sticky="w",columnspan=3)

valor = customtkinter.CTkEntry(frame4,placeholder_text="0.00",width=100)
valor.grid(padx=5,pady=0,row=3,column=1,sticky="w",columnspan=3)

nome = customtkinter.CTkTextbox(frame4,width=300,height=80)
nome.grid(padx=5,pady=0,row=4,column=1,sticky="w",columnspan=3)

botao_excluir=customtkinter.CTkButton(frame4, text="Excluir", width=80, fg_color=("Red"), hover_color="green")
botao_excluir.grid(padx=5, pady=5, row=5, column=1, stick="w")

botao_cancelar=customtkinter.CTkButton(frame4, text="Cancelar", width=80, fg_color=("black"), hover_color="green")
botao_cancelar.grid(padx=0, pady=5, row=5, column=2)

botao_salvar=customtkinter.CTkButton(frame4, text="Salvar", width=80, fg_color=("black"), hover_color="green")
botao_salvar.grid(padx=5, pady=5, row=5, column=3, stick="e")


#frame 5, saida


pesquisar_saida = customtkinter.CTkEntry(frame5,placeholder_text="pesquisar Saida",width=220)
pesquisar_saida.grid(padx=20,pady=20,column=0,row=1,sticky="w")

lista_saida = customtkinter.CTkScrollableFrame(frame5)
lista_saida.grid(padx=20,pady=0,column=0,row=2,rowspan=4)



for items2 in items2:
    box1 = customtkinter.CTkCheckBox(lista_saida,text=items2)
    box1.grid(pady=5)

nome_e_quantidade = customtkinter.CTkEntry(frame5,placeholder_text="nome e quantidade em estoque",width=300)
nome_e_quantidade.grid(padx=0,pady=0,column=1,row=1,sticky="w",columnspan=2)

saida_retirada = customtkinter.CTkEntry(frame5,placeholder_text="quantidade a ser retirada",width=190)
saida_retirada.grid(padx=0,pady=0,column=1,row=2,sticky="w")

cancelar_saida = customtkinter.CTkButton(frame5,text="cancelar",width=80,fg_color="red",hover_color="green")
cancelar_saida.grid(padx=5,pady=5,row=5,column=1,sticky="w")

salvar_saida = customtkinter.CTkButton(frame5,text="salvar",width=80,fg_color="black",hover_color="green")
salvar_saida.grid(padx=5,pady=5,row=5,column=2,sticky="e")


#caixinha do produto
line_frame = customtkinter.CTkScrollableFrame(frame5, height=100, width=300)
line_frame.grid(pady=0, row=3, column=1, columnspan=2, stick="we")


def on_trash_icon_click(item_number):
    print(f"ícone de lixeira linha {item_number} clicado")

def create_line(text, item_number):

    label = customtkinter.CTkLabel(line_frame, text="item 1")
    label.grid(pady=0, padx=5, row=item_number, column=0, stick="w")

    trash_icon = customtkinter.CTkButton(line_frame, text="🗑", command=lambda: on_trash_icon_click(item_number), width=20)
    trash_icon.grid(padx=0, pady=5, row=item_number, column=1, stick="e")

    line_frame.grid_columnconfigure(0, weight=1)
    line_frame.grid_columnconfigure(1, weight=0)


botao_salvar=customtkinter.CTkButton(frame5, text="Adicionar item", width=50, fg_color=("black"), hover_color="#2f394a", command=lambda: create_line(item, 1))
botao_salvar.grid(padx=0, pady=5, row=2, column=2, stick="e")

items1 = [f"Item {i + 1}" for i in range(5)]
for i, item in enumerate(items1):
    create_line(item, i+5)

#Frame6
pesquisar_entrada2 = customtkinter.CTkEntry(frame6,placeholder_text="pesquisar produto",width=220)
pesquisar_entrada2.grid(padx=20,pady=20,column=0,row=1,sticky="w")

lista_entrada2 = customtkinter.CTkScrollableFrame(frame6)
lista_entrada2.grid(padx=20,pady=0,column=0,row=2,rowspan=4)
items2 = ["ola,mundo" , "ola,mund2o" ,"ola,mundo","ola,mundo" ,"ola,mundo", "ola,mundo"]
for items2 in items2:
    box2 = customtkinter.CTkCheckBox(lista_entrada2,text=items2)
    box2.grid(pady=5)

nome_e_quantidade_entrada = customtkinter.CTkEntry(frame6,placeholder_text="nome e quantidade do produto",width=300)
nome_e_quantidade_entrada.grid(padx=0,pady=0,column=1,row=1,sticky="w",columnspan=2)

entrada = customtkinter.CTkEntry(frame6,placeholder_text="quantidade recebida",width=190)
entrada.grid(padx=0,pady=0,column=1,row=2,sticky="w")

cancelar_entrada = customtkinter.CTkButton(frame6,text="cancelar",width=80,fg_color="red",hover_color="green")
cancelar_entrada.grid(padx=5,pady=5,row=5,column=1,sticky="w")

salvar_entrada = customtkinter.CTkButton(frame6,text="salvar",width=80,fg_color="black",hover_color="green")
salvar_entrada.grid(padx=5,pady=5,row=5,column=2,sticky="e")


#caixinha do produto
line_frame2 = customtkinter.CTkScrollableFrame(frame6, height=100, width=300)
line_frame2.grid(pady=0, row=3, column=1, columnspan=2, stick="we")


def on_trash_icon_click(item_number2):
    print(f"ícone de lixeira linha {item_number2} clicado")

def create_line(text, item_number2):

    label2 = customtkinter.CTkLabel(line_frame2, text="item 1")
    label2.grid(pady=0, padx=5, row=item_number2, column=0, stick="w")

    trash_icon2= customtkinter.CTkButton(line_frame2, text="🗑", command=lambda: on_trash_icon_click(item_number2), width=20)
    trash_icon2.grid(padx=0, pady=5, row=item_number2, column=1, stick="e")

    line_frame2.grid_columnconfigure(0, weight=1)
    line_frame2.grid_columnconfigure(1, weight=0)


botao_salvar2=customtkinter.CTkButton(frame6, text="Adicionar item", width=50, fg_color=("black"), hover_color="#2f394a", command=lambda: create_line(item, 1))
botao_salvar2.grid(padx=0, pady=5, row=2, column=2, stick="e")

items2 = [f"Item {i + 1}" for i in range(5)]
for i, items2 in enumerate(items1):
    create_line(items2, i+5)


# frame 7 relatorio


buscar_produto7 = customtkinter.CTkEntry(frame7,placeholder_text="Buscar Produto",width=220)
buscar_produto7.grid(column=0,row=1,padx=20,pady=20,sticky="w")

botao_exportar = customtkinter.CTkButton(frame7,text="Exportar",width=80,fg_color=("black"), hover_color="#2f394a",command=abrir_poppup)
botao_exportar.grid(column=3,row=1,padx=0,pady=5,sticky="w")

caixa_cubrindo = customtkinter.CTkTextbox(frame7,width=550,height=150)
caixa_cubrindo.grid(row=2,padx=20,pady=5,column=0,columnspan=4,sticky="wsne")

boataoestoque=customtkinter.CTkButton(frame7,text="estoque",width=80,fg_color=("black"), hover_color="#2f394a",command=abrir_frame7)
boataoestoque.grid(column=1,row=3,padx=0,pady=5,sticky="w")

botaosaida = customtkinter.CTkButton(frame7,text="Saída",width=80,fg_color=("black"), hover_color="#2f394a",command=abrir_frame8)
botaosaida.grid(column=2,row=3,padx=0,pady=5,sticky="w")

botaoentrada=customtkinter.CTkButton(frame7,text="entrada",width=80,fg_color=("black"), hover_color="#2f394a",command=abrir_frame9)
botaoentrada.grid(column=3,row=3,padx=0,pady=5,sticky="w")


###frame 8
frame8 = customtkinter.CTkFrame(janela,width=590,height=380,corner_radius=0,fg_color="Gray")
frame8.grid_propagate(False)

mensagem_frame8 = customtkinter.CTkLabel(frame8,text="relatorio de saida",font=("Couvier", 18, "bold"), text_color="#A8B30F")
mensagem_frame8.grid(pady=30,padx=30,row=0,column=0,columnspan=4)

buscar_produto8 = customtkinter.CTkEntry(frame8,placeholder_text="Buscar Produto",width=220)
buscar_produto8.grid(column=0,row=1,padx=20,pady=20,sticky="w")

botao_exportar8 = customtkinter.CTkButton(frame8,text="Exportar",width=80,fg_color=("black"), hover_color="#2f394a",command=abrir_poppup)
botao_exportar8.grid(column=3,row=1,padx=0,pady=5,sticky="w")

caixa_cubrindo8 = customtkinter.CTkTextbox(frame8,width=550,height=150)
caixa_cubrindo8.grid(row=2,padx=20,pady=5,column=0,columnspan=4,sticky="wsne")

boataoestoque8=customtkinter.CTkButton(frame8,text="estoque",width=80,fg_color=("black"), hover_color="#2f394a",command=abrir_frame7)
boataoestoque8.grid(column=1,row=3,padx=0,pady=5,sticky="w")

botaosaida8 = customtkinter.CTkButton(frame8,text="Saída",width=80,fg_color=("black"), hover_color="#2f394a",command=abrir_frame8)
botaosaida8.grid(column=2,row=3,padx=0,pady=5,sticky="w")

botaoentrada8=customtkinter.CTkButton(frame8,text="entrada",width=80,fg_color=("black"), hover_color="#2f394a",command=abrir_frame9)
botaoentrada8.grid(column=3,row=3,padx=0,pady=5,sticky="w")



#frame 9

frame9 = customtkinter.CTkFrame(janela,width=590,height=380,corner_radius=0,fg_color="Gray")
frame9.grid_propagate(False)

mensagem_frame9 = customtkinter.CTkLabel(frame9,text="relatorio de entrada",font=("Couvier", 18, "bold"), text_color="#A8B30F")
mensagem_frame9.grid(pady=30,padx=30,row=0,column=0,columnspan=4)

buscar_produto9 = customtkinter.CTkEntry(frame9,placeholder_text="Buscar Produto",width=220)
buscar_produto9.grid(column=0,row=1,padx=20,pady=20,sticky="w")

botao_exportar9 = customtkinter.CTkButton(frame9,text="Exportar",width=80,fg_color=("black"), hover_color="#2f394a",command=abrir_poppup)
botao_exportar9.grid(column=3,row=1,padx=0,pady=5,sticky="w")

caixa_cubrindo9 = customtkinter.CTkTextbox(frame9,width=550,height=150)
caixa_cubrindo9.grid(row=2,padx=20,pady=5,column=0,columnspan=4,sticky="wsne")

boataoestoque9=customtkinter.CTkButton(frame9,text="estoque",width=80,fg_color=("black"), hover_color="#2f394a",command=abrir_frame7)
boataoestoque9.grid(column=1,row=3,padx=0,pady=5,sticky="w")

botaosaida9 = customtkinter.CTkButton(frame9,text="Saída",width=80,fg_color=("black"), hover_color="#2f394a",command=abrir_frame8)
botaosaida9.grid(column=2,row=3,padx=0,pady=5,sticky="w")

botaoentrada9=customtkinter.CTkButton(frame9,text="entrada",width=80,fg_color=("black"), hover_color="#2f394a",command=abrir_frame9)
botaoentrada9.grid(column=3,row=3,padx=0,pady=5,sticky="w")










janela.mainloop()