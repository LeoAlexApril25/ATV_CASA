import customtkinter as ctk


janela = ctk.CTk()
janela.title("App teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)# Aqui tem usar a altura e largura para antigir a maxima altura e largura feita por essa variavel/codigo
janela.minsize(width=500, height= 350)# Aqui tem usar a altura e largura para antigir a minima altura e largura feita por essa variavel/codigo
janela.resizable(width=True,height=False)# Funciona em Booleano, se estiver em Falso altura ou largura ele impedi que aja alteração de tamanho
janela.iconify()# Fecha a janelano momento que ela é aberta
janela.deiconify()# Abre a janela depois do fechamento do iconify

janela.mainloop()