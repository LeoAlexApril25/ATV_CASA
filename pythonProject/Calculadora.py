import customtkinter

def resultado():
    var_resultado = float(Valor_horas.get()) * float(Qtd_horas.get())
    var_Sindicato = var_resultado * 0.03
    var_FGTS = var_resultado * 0.11

    if var_resultado <= 900:
        var_ir = 0
        var_INSS = var_resultado * 0.10
    elif var_resultado <= 1500:
        var_ir = var_resultado * 0.05
        var_INSS = var_resultado * 0.10
    elif var_resultado <= 2500:
        var_ir = var_resultado * 0.10
        var_INSS = var_resultado * 0.10
    else:
        var_ir = var_resultado * 0.20
        var_INSS = var_resultado * 0.10

    var_Totaldesconto = var_ir + var_INSS + var_Sindicato
    var_Liquido = var_resultado - var_Totaldesconto

    Label_sainda1.configure(text=f"Salario Bruto: R${var_resultado:.2f}")
    Label_sainda2.configure(text=f"O IR é: R${var_ir:.2f}")
    Label_sainda3.configure(text=f"O INSS é: R${var_INSS:.2f}")
    Label_sainda4.configure(text=f"O FGTS é: R${var_FGTS:.2f} (não descontado)")
    Label_sainda5.configure(text=f"O Total de desconto é: {var_Totaldesconto}")
    Label_sainda6.configure(text=f"O Salario Liquido é: {var_Liquido}")

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.title("Imposto de renda")
janela.geometry("1200x720")

Label_entrada = customtkinter.CTkLabel(janela, text="Imposto de renda")
Label_entrada.pack(pady=20)

Valor_horas = customtkinter.CTkEntry(janela, placeholder_text="Digite o numero de horas:")
Valor_horas.pack(pady=20)

Qtd_horas = customtkinter.CTkEntry(janela, placeholder_text="Digite a quantidade de horas:")
Qtd_horas.pack(pady=20)

botao = customtkinter.CTkButton(janela, text="Resultado do salario liquido", command=resultado)
botao.pack(pady=20)

Label_sainda1 = customtkinter.CTkLabel(janela, text="Salario Bruto:")
Label_sainda1.pack(pady=20)

Label_sainda2 = customtkinter.CTkLabel(janela, text="IR (5%):")
Label_sainda2.pack(pady=20)

Label_sainda3 = customtkinter.CTkLabel(janela, text="INSS (10%):")
Label_sainda3.pack(pady=20)

Label_sainda4 = customtkinter.CTkLabel(janela, text="FGTS (11%):")
Label_sainda4.pack(pady=20)

Label_sainda5 = customtkinter.CTkLabel(janela, text="Total de desconto:")
Label_sainda5.pack(pady=20)

Label_sainda6 = customtkinter.CTkLabel(janela, text="Salario Liquido:")
Label_sainda6.pack(pady=20)

janela.mainloop()

