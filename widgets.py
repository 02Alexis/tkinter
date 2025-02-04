import tkinter as tk

window = tk.Tk()
window.title("Interfaz Grafica")
window.geometry("400x300")

# tag = tk.Label(window, text="Etiqueta 1")
# tag.grid(row=0, column=0)

# ta2 = tk.Label(window, text="Etiqueta 2")
# ta2.grid(row=0, column=1)

# ta3 = tk.Label(window, text="Etiqueta 3")
# ta3.grid(row=1, column=0)

tag = tk.Label(window, text="Etiqueta 1")
tag.place(x=50, y=50)

ta2 = tk.Label(window, text="Etiqueta 2")
ta2.place(x=150, y=150)

ta3 = tk.Label(window, text="Etiqueta 3")
ta3.place(x=250, y=100)

ta4 = tk.Label(window, text="Etiqueta 4")
ta4.place(x=200, y=280)


window.mainloop() #------ mantiene la ventana abierta