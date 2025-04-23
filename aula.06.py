import customtkinter
import customtkinter as ctk


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

tabview = ctk.CTkTabview(janela, width= 500,height= 200, fg_color="Blue")
tabview.grid(pady=100,padx=100)

tabview.add("Nome")#Adiciona uma tabela chamada nomes
tabview.add("Idade")#Adiciona uma tabela chamada idade
tabview.add("Genero")#Adiciona uma tabela chamada Genero
tabview.tab("Nome")#Adiciona a tabela nome
tabview.tab("Idade")# adiciona a tabela idade
tabview.tab("Genero")# Adiciona a tabela genero

text=ctk.CTkLabel(tabview.tab("Nome"),text="Leo\nEduardo\nAlice\nFernanda") # Adiciona os nomes atraves da chamada do tabview.tab
text.grid(pady=0,padx=0,stick="nsew")
text2=ctk.CTkLabel(tabview.tab("Idade"),text="21 years\n22 years\n17 years\n15 years")
text2.grid(pady=0,padx=0,stick="nsew")
text3=ctk.CTkLabel(tabview.tab("Genero"),text="Masculino\nMasculino\nFeminino\nFeminino")
text3.grid(pady=0,padx=0,stick="nsew")



janela.mainloop()