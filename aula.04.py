import customtkinter
import customtkinter as ctk


def nova_janela():
    nova_janela = ctk.CTkToplevel(janela) #Cria uma nova janela
    label = ctk.CTkLabel(nova_janela, text="Nova janela", font=("Couvier",18))
    label.grid(pady=5,padx=200,row=0, column=0,stick="w")
    texto = ctk.CTkEntry(nova_janela, placeholder_text="Insera seu nome", font=("Couvier",18), corner_radius=0)
    texto.grid(pady=5,padx=20,row=1,column=0,stick="we")
    botao_nova_janela = ctk.CTkButton(nova_janela,text="Apertar",font=("Couvier",18), corner_radius=0)
    botao_nova_janela.grid(pady=5,padx=20,row=2,column=0)
    label_1 = ctk.CTkLabel(nova_janela, text="Parabens seu nome inserindo", font=("Couvier", 18))
    label_1.grid(pady=5, padx=3, row=0, column=0, stick="w")
    nova_janela.geometry("480x240")


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

janela = ctk.CTk()
janela.title("App teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)# Aqui tem usar a altura e largura para antigir a maxima altura e largura feita por essa variavel/codigo
janela.minsize(width=500, height= 350)# Aqui tem usar a altura e largura para antigir a minima altura e largura feita por essa variavel/codigo
janela.resizable(width=True,height=False)# Funciona em Booleano, se estiver em Falso altura ou largura ele impedi que aja alteração de tamanho
#janela.iconify()# Fecha a janelano momento que ela é aberta
#janela.deiconify()# Abre a janela depois do fechamento do iconify

botao = ctk.CTkButton(master= janela, text="Abrir Janela", command= nova_janela).place(x=250,y=80)

janela.mainloop()