from tkinter import *
from tkinter import ttk
import sqlite3


#constructor y la ventana
class Tienda: #clase
     
    def __init__(self, ventana):

        self.ventana=ventana
        self.ventana.geometry("1000x900")
        self.ventana.title("SUPERMERCADO TZUZUL CODE")
        self.ventana.configure(background="tomato")
        self.widget()
    def widget(self):
        #-----------------------------------------------------------------
        #Seccion imagen y nombre del supermercado
        Label(self.ventana, text=" '' SUPERMERCADO TZUZUL CODE '' ", fg="black", font="curier 15").pack() # se crea un forn
        Label(self.ventana, text=" EL MEJOR LUGAR PARA REALIZAR SUS COMPRAS", fg="black", font="curier 10").pack()
        self.img = PhotoImage(file="logo.gif") 
        Label(self.ventana, image=self.img ).pack() 
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        #Seccion etiquetas y entrada de producto.
        etiquetaProducto = Label(self.ventana, text=" Ingrese el Producto: ", bd=4, bg="white", font="Curier 10")
        etiquetaProducto.place(x=15, y=200)
        self.entradaProducto = Entry(self.ventana, bd=4, font="Curier 10")
        self.entradaProducto.place(x=175, y=200)
        #Secciom boton entrada producto
        botonProducto = Button(self.ventana, text="Agregar producto",command=self.registrar_producto)
        botonProducto.place(x=355, y=200)
        #-----------------------------------------------------------------
        #Secciom boton reiniciar base de datos
        botonProducto = Button(self.ventana, text="Eliminar producto",command=self.borrar)
        botonProducto.place(x=355, y=250)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        #Seccion etiquetas y entrada de cantidad.
        etiquetaCantidad = Label(self.ventana, text=" Ingrese la Cantidad: ", bd=4, bg="white", font="Curier 10")
        etiquetaCantidad.place(x=15, y=230)
        self.entradaCantidad = Entry(self.ventana, bd=4, font="Curier 10")
        self.entradaCantidad.place(x=175, y=230)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        #Seccion etiquetas y entrada de precio.
        etiquetaPrecio = Label(self.ventana, text=" Ingrese el Precio:    ", bd=4, bg="white", font="Curier 10")
        etiquetaPrecio.place(x=15, y=260)
        self.entradaPrecio = Entry(self.ventana, bd=4, font="Curier 10")
        self.entradaPrecio.place(x=175, y=260)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        #Seccion tabla de muestra
        self.tabla=ttk.Treeview(height=10,columns=('#0','#1','#2','#3','#4'))
        self.tabla.place(x=0,y=350)
        self.tabla.heading("#0",text="Id",anchor=CENTER)
        self.tabla.heading("#1",text="Producto",anchor=CENTER)
        self.tabla.heading("#2",text="Cantidad",anchor=CENTER)
        self.tabla.heading("#3",text="Precio",anchor=CENTER)
        self.tabla.heading("#4",text="Total",anchor=CENTER)
        self.recorrer() #Apenas inicie nuestra aplicacion nos traiga los valores de nuesta base de datos.
        #-----------------------------------------------------------------
     
      #Funcion conexion base de datos  
    def run_query(self, consulta, parametros = ()): 
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor() 
        result = cursor.execute(consulta, parametros)
        conn.commit() 
        return result

    def recorrer(self): 
        #Limpienza de los datos en nuestra tabla o recorido en nuestra tabla
        records = self.tabla.get_children() 
        #Recorre los elementos de la tabla
        for elementos in records: 
            self.tabla.delete(elementos)        
        #Consultando los datos en nuestra base de datos y recorrido
        consulta = 'SELECT * FROM proyecto ORDER BY id DESC'    
        filas_bd = self.run_query(consulta)
        #recorrer nuestra tabla
        for fila in filas_bd: #recorre las filas e inserta los valores 
            self.tabla.insert('', 0, text=fila[0], values=(fila[1], fila[2], fila[3],fila[4]))
    
    
    def validar(self):
        return len(self.entradaPrecio.get())!=0 and len(self.entradaCantidad.get())!=0 and len(self.entradaProducto.get())!=0 

    def registrar_producto(self):
        if self.validar(): #SI al ejecutar esto, es truu has esto     
            consulta="INSERT INTO proyecto VALUES(?,?,?,?,?)"
            parametros=(None,self.entradaProducto.get(),
            self.entradaCantidad.get(),self.entradaPrecio.get(),
            float(self.entradaCantidad.get())*float(self.entradaPrecio.get()))

            self.run_query(consulta,parametros)
            self.recorrer()
        else:
            self.recorrer()
        
    def borrar(self):
        if self.validar():
            consulta="DELETE FROM proyecto "
            self.run_query(consulta)
            self.recorrer()
if __name__=="__main__": #  Hacemos la comprobacion, para iniciar nuestra aplicacion
    ventana = Tk() #Vetana principal
    aplicacion=Tienda(ventana)  #aplicacion por si nos arroja algun dato
   
    ventana.mainloop()

