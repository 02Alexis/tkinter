import tkinter as tk

window = tk.Tk()
window.title("Interfaz Grafica")
window.geometry("400x300")

navbar = tk.Menu(window)
window.config(menu = navbar)

menu_file = tk.Menu(navbar, tearoff=0)
navbar.add_cascade(label="Archivo", menu=menu_file)
menu_file.add_command(label="Nuevo Archivo")
menu_file.add_separator()
menu_file.add_command(label="Salir del programa", command=window.quit)
menu_file.config(bg="lightgreen")

menu_help = tk.Menu(navbar, tearoff=0)
navbar.add_cascade(label="Ayuda", menu=menu_help)
menu_help.add_command(label="Información")

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