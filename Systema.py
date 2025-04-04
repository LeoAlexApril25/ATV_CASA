import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


janela = customtkinter.CTk()
janela.title("Teste")
janela.geometry("800x400")
btn = customtkinter.CTkButton(janela,text="teste aqui")
btn.grid(pady=5,padx=5)

janela.mainloop()