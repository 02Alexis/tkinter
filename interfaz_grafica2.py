import tkinter as tk

window = tk.Tk()
window.title("Interfaz Grafica")
window.geometry("400x300")

# ----- Funcion para acceder al contenido del campo del texto
def view_name():
    name = text_field.get()
    lastName = lastname_field.get()
    # -------- Condicional para verificar si hay un campo vacio
    if name.strip() == "":
        tag.config(text="Campo vacio, Por favor ingrese un nombre")
    else:
        tag.config(text=f"Hola, {name} {lastName}")

text_field = tk.Entry(window)
text_field.pack()

lastname_field = tk.Entry(window)
lastname_field.pack()

tag = tk.Label(window, text="")
tag.pack()

button = tk.Button(window, text="Mostrar Nombre", command=view_name)
button.pack()

window.mainloop() #------ mantiene la ventana abierta