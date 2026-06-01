import customtkinter as ctk 

# Tema do App
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# Janela do App
app = ctk.CTk()
app.iconbitmap(r"C:\Users\natan\OneDrive\Documentos\GitHub\Exercicios\projeto ctk\logo.ico")
app.geometry("400x300")
app.title("Calcular Média")

def calcularmedia():
    try:
        n1 = float(nota1.get())
        n2 = float(nota2.get())

        media = (n1+n2)/2
        
        label.resultado.configure(text=f"A média é :{media:.2f}", text_color="white")
    except:
        label.resultado.configure(text="Por favor, digite números válidos!", text_color="red")

# Nota 1
label = ctk.CTkLabel(app, text="Insira nota 1: ", font=("Arial", 16))
label.pack(pady=(20, 0))
nota1 =ctk.CTkEntry(app, placeholder_text="")
nota1.pack(pady=5)

# Nota 2
label = ctk.CTkLabel(app, text="Insira nota 2: ", font=("Arial", 16))
label.pack(pady=(20, 0))
nota2 =ctk.CTkEntry(app, placeholder_text="")
nota2.pack(pady=5)


botao = ctk.CTkButton (app,text="Click aqui", command=calcularmedia)
botao.pack(pady=10)

label.resultado = ctk.CTkLabel(app,text="", font=("Arial", 16, "bold"))
label.resultado.pack(pady=10)
# Rodar o app
app.mainloop()