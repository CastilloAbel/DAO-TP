
from tkinter import ttk
from tkinter import *

class AgregarPrestamo:
    def __init__(self, datos=[]):
        self.window = Tk()
        self.window.title("Alta de Prestamos")
        self.datos = datos

        frame1 = Frame(self.window)
        frame1.pack(pady=20, padx=10)
        frame2 = Frame(self.window)
        frame2.pack(pady=5, padx=5)

        self.dni = StringVar()
        self.codigo = StringVar()
        self.fechaPrestamo = StringVar()
        self.diasPactados = StringVar()

        Label(frame1, text="Dni del Socio:").grid(row=0, column=0)
        Entry(frame1, textvariable=self.dni).grid(row=0, column=1)
        Label(frame1, text="Codigo del libro:").grid(row=1, column=0)
        Entry(frame1, textvariable=self.codigo).grid(row=1, column=1) 
        Label(frame1, text="Fecha del Prestamo:").grid(row=2, column=0)
        Entry(frame1, textvariable=self.fechaPrestamo).grid(row=2, column=1)
        Label(frame1, text="Dias Pactados:").grid(row=3, column=0)
        Entry(frame1, textvariable=self.diasPactados).grid(row=3, column=1)

        if self.datos == []:
            Button(frame2, text="Agregar", command=self.agregar_Prestamo).pack(side="left", padx=10)
        else:
            Button(frame2, text="Editar", command=self.editar_Prestamo).pack(side="left", padx=10)
        
        Button(frame2, text="Cancelar", command=self.window.destroy).pack(side="right", padx=10)


    def mostrar(self):
        self.window.mainloop()

        # Función para agregar un Prestamo a la lista
    def agregar_Prestamo(self):
        dni = self.dni.get()
        codigo = self.codigo.get()
        fechaPrestamo = self.fechaPrestamo.get("")
        diasPactados = self.diasPactados.get("")
        # self.lista_Prestamos.insert("", "end", values=(dni, codigo, fechaPrestamo, diasPactados))
        dni = self.dni.set("")
        codigo = self.codigo.set("")
        fechaPrestamo = self.fechaPrestamo.set("")
        diasPactados = self.diasPactados.set("")


    # Función para editar un Prestamo seleccionado
    def editar_Prestamo(self):
        # selected_item = self.lista_Prestamos.selection()[0]
        dni = self.datos[0]
        codigo = self.datos[1]
        fechaPrestamo = self.datos[2]
        diasPactados = self.datos[3]
        # self.lista_Prestamos.insert("", "end", values=(dni, codigo, fechaPrestamo, diasPactados))
        dni = self.dni.set("")
        codigo = self.codigo.set("")
        fechaPrestamo = self.fechaPrestamo.set("")
        diasPactados = self.diasPactados.set("")