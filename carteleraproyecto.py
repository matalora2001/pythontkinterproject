from tkinter import Tk, Entry, Button
import tkinter as Tk
from tkinter import messagebox

ventana = Tk.Tk()
ventana.title("Cartelera Marianny Mata")
ventana.geometry("760x620")
ventana.configure(background="antique white")


#-----------------------
precios = (250, 53.25, 200.13, 182.70)

def agregar_pelicula(label_text, precio):
    global total_precio
    pelicula = f"{label_text} ~ Precio: RD$ {precio}"
    listbox.insert(Tk.END, pelicula)
    total_precio += precio
    actualizarprecio()

#dune
pelicula11 = Tk.Frame(ventana, width=200, height=300, bg="lightcoral")
pelicula11.grid(row=0, column=0, padx=5, pady=5)
label11_text = "DUNE: PART 2"
label11 = Tk.StringVar(value=label11_text)
label11_label = Tk.Label(ventana, bg="white", textvariable=label11)
label11_label.grid(column=0, row=0, sticky=Tk.NW, padx=10, pady=10)
Tk.Label(ventana, bg="beige", text='Produced by: Denis Villeneuve').grid(column=0, row=0, sticky=Tk.NW, padx=10, pady=30)
Tk.Label(ventana, bg="beige", text='Cast: Timothée Chalamet, Zendaya... ').grid(column=0, row=0, sticky=Tk.NW, padx=10, pady=50)
btn_agregar11 = Tk.Button(ventana, bg="beige", text="Agregar película", command=lambda: agregar_pelicula(label11_text, precios[0]))
btn_agregar11.grid(column=0, row=0, padx=40, pady=40, sticky=Tk.S)
Tk.Label(ventana, bg="lightcoral", text=f"Precio: {precios[0]}").grid(column=0, row=0, padx=50, pady=50)

#pastlives
pelicula21 = Tk.Frame(ventana, width=200, height=300, bg="darkblue")
pelicula21.grid(row=0, column=1, padx=5, pady=5)
label21_text = "PAST LIVES"
label21 = Tk.StringVar(value=label21_text)
label21_label = Tk.Label(ventana, bg="white", textvariable=label21)
label21_label.grid(column=1, row=0, sticky=Tk.NW, padx=10, pady=10)
Tk.Label(ventana, bg="lightblue", text='Produced by: Celine Song').grid(column=1, row=0, sticky=Tk.NW, padx=10, pady=30)
Tk.Label(ventana, bg="lightblue", text='Cast: Creta Lee, Teo Yoo').grid(column=1, row=0, sticky=Tk.NW, padx=10, pady=50)
btn_agregar21 = Tk.Button(ventana, bg="lightblue", text="Agregar película", command=lambda: agregar_pelicula(label21_text, precios[1]))
btn_agregar21.grid(column=1, row=0, padx=40, pady=40, sticky=Tk.S)
Tk.Label(ventana, fg="white", bg="darkblue", text=f"Precio: {precios[1]}").grid(column=1, row=0, padx=50, pady=50)

#soiedad de la nieve
pelicula12 = Tk.Frame(ventana, width=200, height=300, bg="lightyellow")
pelicula12.grid(row=1, column=0, padx=5, pady=5)
label12_text = "SOCIETY OF THE SNOW"
label12 = Tk.StringVar(value=label12_text)
label12_label = Tk.Label(ventana, bg="white", textvariable=label12)
label12_label.grid(column=0, row=1, sticky=Tk.NW, padx=10, pady=10)
Tk.Label(ventana, bg="lightcoral", text='Produced by: J. A. Bayona').grid(column=0, row=1, sticky=Tk.NW, padx=10, pady=30)
Tk.Label(ventana, bg="lightcoral", text='Cast: Felipe Gonzalez, Matías R... ').grid(column=0, row=1, sticky=Tk.NW, padx=10, pady=50)
btn_agregar12 = Tk.Button(ventana, bg="lightcoral", text="Agregar película", command=lambda: agregar_pelicula(label12_text, precios[2]))
btn_agregar12.grid(column=0, row=1, padx=40, pady=40, sticky=Tk.S)
Tk.Label(ventana, bg="lightyellow", text=f"Precio: {precios[2]}").grid(column=0, row=1, padx=50, pady=50)

#kung fu pand
pelicula22 = Tk.Frame(ventana, width=200, height=300, bg="lightblue")
pelicula22.grid(row=1, column=1, padx=5, pady=5)
label22_text = "KUNG FU PANDA 4"
label22 = Tk.StringVar(value=label22_text)
label22_label = Tk.Label(ventana, bg="white", textvariable=label22)
label22_label.grid(column=1, row=1, sticky=Tk.NW, padx=10, pady=10)
Tk.Label(ventana, bg="turquoise", text='Produced by: DreamWorks').grid(column=1, row=1, sticky=Tk.NW, padx=10, pady=30)
Tk.Label(ventana, bg="turquoise", text='Cast: Viola Davis, Awkwafina... ').grid(column=1, row=1, sticky=Tk.NW, padx=10, pady=50)
btn_agregar22 = Tk.Button(ventana, bg="turquoise", text="Agregar película", command=lambda: agregar_pelicula(label22_text, precios[3]))
btn_agregar22.grid(column=1, row=1, padx=40, pady=40, sticky=Tk.S)
Tk.Label(ventana, bg="lightblue", text=f"Precio: {precios[3]}").grid(column=1, row=1, padx=50, pady=50)

lista = Tk.Frame(ventana)
lista.grid(row=0, column=2, rowspan=2, padx=10, pady=10)
listbox = Tk.Listbox(lista, width=50, height=20)
listbox.pack(expand=True, fill=Tk.BOTH)
#---- ---------- --------
total_precio = 0
def actualizarprecio():
    suma.config(text=f"Total: RD$ {total_precio}")

Tk.Label(ventana)
suma = Tk.Label(ventana, text="Total: RD$")
suma.grid(row=0, column=2, rowspan=2, padx=10, pady=100, sticky=Tk.SW)


def devuelta():
        efectivodev = float(numefectivo.get())
        resul = efectivodev - total_precio
        lblDev.config(text=f"Devuelta: {resul}")
        
        if total_precio > efectivodev:
                lblDev.config(text="ERROR")
                messagebox.showerror("Error", "El monto ingresado debe ser mayor al total :)  ")
                
        if total_precio == efectivodev:
                lblDev.config(text="No tienes devuelta")
                
        
efectivo = Tk.Label(ventana, text="Ingresa tu efectivo: ")
efectivo.grid(row=0, column=2, rowspan=5, padx=10, pady=65, sticky=Tk.SW)
numefectivo = Entry(ventana, bg="white")
numefectivo.grid(row=0, column=2, rowspan=2, padx=10, pady=40, sticky=Tk.SW)

btn_devuelta = Button(ventana, text="Devolver efectivo", command=devuelta)
btn_devuelta.grid(row=0, column=2, rowspan=2, padx=3, pady=65, sticky=Tk.SE)
lblDev= Tk.Label(ventana, text="")
lblDev.grid(row=0, column=2, rowspan=2, padx=3, pady=40, sticky=Tk.SE)

def borrar():
    listbox.delete(0, Tk.END)
    lblDev.config(text="")
    numefectivo.delete(0, Tk.END)
    
    global total_precio
    total_precio = 0  
    actualizarprecio() 

lblBorrar = Button(ventana, text="Limpiar Todo", command=borrar)
lblBorrar.grid(row=0, column=2, rowspan=2, padx=3, pady=10, sticky=Tk.S)


ventana.mainloop()
