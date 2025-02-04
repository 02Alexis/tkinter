import tkinter as tk

window = tk.Tk()
window.title("Interfaz Grafica")
window.geometry("400x300")

tag = tk.Label(window, text="Hola")
tag.pack() # ---- posiciona los widgets dentro de la ventana

# ---- funcion para cambiar el color de la etiqueta
def change_color():
    tag.config(fg="red")

# ---- funcion para cambiar el color de la etiqueta
def change_text():
    tag.config(text="Adios Interfaz Grafica")

button = tk.Button(window, text="Cambiar Texto", command=change_color)
button.pack()

button_bye = tk.Button(window, text="Adios Interfaz Grafica", command=change_text)
button_bye.pack()

window.mainloop() #------ mantiene la ventana abierta