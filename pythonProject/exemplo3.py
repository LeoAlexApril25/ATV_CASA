import customtkinter
def resultado():
        var_ImC = float(entrada1.get())/float(entrada2.get())**2
        IMC = var_ImC
        label_sainda.configure(text=f"IMC:{IMC:.2f}")
        if IMC <= 18.4:
            label_sainda2.configure(text="Abaixo do peso")

        elif 18.5 < IMC < 25:
            label_sainda2.configure(text="Peso normal")

        elif 25 < IMC < 29.9:
            label_sainda2.configure(text="Sobrepeso")

        elif 30 < IMC < 34.4:
            label_sainda2.configure(text="Obesidade 1")

        elif 35 < IMC < 39.9:
            label_sainda2.configure(text="Obesidade 2")

        elif IMC > 40:
            label_sainda2.configure(text="Obesidade 3")

customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('green')

janela = customtkinter.CTk()
janela.title("Calculadora de IMC")
janela.geometry("400x400")

label_entrada = customtkinter.CTkLabel(janela, text="Calculadora de IMC ")
label_entrada.pack()

entrada1 = customtkinter.CTkEntry(janela, placeholder_text=" Peso(kg)")
entrada1.pack(pady=15)

entrada2 = customtkinter.CTkEntry(janela, placeholder_text=" Altura(m)")
entrada2.pack(pady=15)

botao = customtkinter.CTkButton(janela, text="Clique aqui", command=resultado)
botao.pack()

label_sainda = customtkinter.CTkLabel(janela, text=" IMC ")
label_sainda.pack()

label_sainda2 = customtkinter.CTkLabel(janela, text=" Classificação")
label_sainda2.pack()

janela.mainloop()