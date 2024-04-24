#libreria de edición
from multiprocessing import Value
import tkinter as tk
#modulos de libreria
from tkinter import*
from tkinter import ttk,Label,Entry,messagebox
from tkinter import ttk, Scrollbar

from Informacion import *
from CONEXION import *

class Troncal:
    global search_entry,tree,tree1,combo,base,groupBox,textBoxEqDs,textBoxTD, textBoxTx1,textBoxTkR,textBoxEqRou,textBoxRx1,textBoxEq1,textBoxRx2,textBoxEq2,textBoxTx2,textBoxRx3,textBoxEq3,textBoxTx3,textBoxRx4,textBoxEq4,textBoxTx4,textBoxRx5,textBoxEq5,textBoxTx5,textBoxUbiDs,textBoxUbiRou#,textBoxid
    tree=None
    #tree1=None
    combo=None
    base=None
    groupBox=None
    textBoxEqDs = None
    textBoxTD=None
    textBoxTx1=None
    textBoxTkR=None
    textBoxEqRou=None
    textBoxRx1=None
    textBoxEq1=None
    textBoxRx2=None
    textBoxEq2=None
    textBoxTx2=None
    textBoxRx3=None
    textBoxEq3=None
    textBoxTx3=None
    textBoxRx4=None
    textBoxEq4=None
    textBoxTx4=None
    textBoxRx5=None
    textBoxEq5=None
    textBoxTx5=None
    textBoxUbiDs=None
    textBoxUbiRou=None
    textBoxid=None

def Formulario():
    global  search_entry,tree,tree1,combo,base,groupBox,textBoxEqDs,textBoxTD, textBoxTx1,textBoxTkR,textBoxEqRou,textBoxRx1,textBoxEq1,textBoxRx2,textBoxEq2,textBoxTx2,textBoxRx3,textBoxEq3,textBoxTx3,textBoxRx4,textBoxEq4,textBoxTx4,textBoxRx5,textBoxEq5,textBoxTx5,textBoxUbiDs,textBoxUbiRou, textBoxid      
    
   
    try:


        base = Tk()
        base.geometry("1200x600")
        base.title("Formulario")
        base.configure(bg="salmon") 

        groupBox = LabelFrame(base,text="DATOS DE LA TRONCAL", padx=5,pady=5)
        groupBox.grid(row=0,column=0,padx=10,pady=10)
 
        LabelEqDs=Label(groupBox,text="Equipo  destino: ",width=13,font=("arial",12)).grid(row=0,column=0)
        textBoxEqDs= Entry (groupBox,width=45)
        textBoxEqDs.grid(row=0,column=1)

        LabelTD=Label(groupBox,text="TrunkDest: ",width=13,font=("arial",12)).grid(row=0,column=2)
        textBoxTD= Entry (groupBox)
        textBoxTD.grid(row=0,column=3)

        LabelTkR=Label(groupBox,text="TrkROU: ",width=13,font=("arial",12)).grid(row=0,column=4)
        textBoxTkR= Entry (groupBox)
        textBoxTkR.grid(row=0,column=5)

        LabelEqRou=Label(groupBox,text="Equipo ROU: ",width=13,font=("arial",12)).grid(row=0,column=6)
        textBoxEqRou= Entry (groupBox,width=45)
        textBoxEqRou.grid(row=0,column=7)

        LabelRx1=Label(groupBox,text="TrkRx1: ",width=13,font=("arial",12)).grid(row=2,column=0)
        textBoxRx1= Entry (groupBox)
        textBoxRx1.grid(row=2,column=1)

        LabelEq1=Label(groupBox,text="EquipoTx1: ",width=13,font=("arial",12)).grid(row=2,column=2)
        textBoxEq1= Entry (groupBox)
        textBoxEq1.grid(row=2,column=3)

        LabelTx1=Label(groupBox,text="TrkTx1: ",width=13,font=("arial",12)).grid(row=2,column=4)
        textBoxTx1= Entry (groupBox)
        textBoxTx1.grid(row=2,column=5)

        LabelRx2=Label(groupBox,text="TrkRx2: ",width=13,font=("arial",12)).grid(row=3,column=0)
        textBoxRx2= Entry (groupBox)
        textBoxRx2.grid(row=3,column=1)

        LabelEq2=Label(groupBox,text="EquipoTx2: ",width=13,font=("arial",12)).grid(row=3,column=2)
        textBoxEq2= Entry (groupBox)
        textBoxEq2.grid(row=3,column=3)

        LabelTx2=Label(groupBox,text="TrkTx2: ",width=13,font=("arial",12)).grid(row=3,column=4)
        textBoxTx2= Entry (groupBox)
        textBoxTx2.grid(row=3,column=5)

        LabelRx3=Label(groupBox,text="TrkRx3: ",width=13,font=("arial",12)).grid(row=4,column=0)
        textBoxRx3= Entry (groupBox)
        textBoxRx3.grid(row=4,column=1)

        LabelEq3=Label(groupBox,text="EquipoTx3: ",width=13,font=("arial",12)).grid(row=4,column=2)
        textBoxEq3= Entry (groupBox)
        textBoxEq3.grid(row=4,column=3)

        LabelTx3=Label(groupBox,text="TrkTx3: ",width=13,font=("arial",12)).grid(row=4,column=4)
        textBoxTx3= Entry (groupBox)
        textBoxTx3.grid(row=4,column=5)

        LabelRx4=Label(groupBox,text="TrkRx4: ",width=13,font=("arial",12)).grid(row=5,column=0)
        textBoxRx4= Entry (groupBox)
        textBoxRx4.grid(row=5,column=1)

        LabelEq4=Label(groupBox,text="EquipoTx4: ",width=13,font=("arial",12)).grid(row=5,column=2)
        textBoxEq4= Entry (groupBox)
        textBoxEq4.grid(row=5,column=3)

        LabelTx4=Label(groupBox,text="TrkTx4: ",width=13,font=("arial",12)).grid(row=5,column=4)
        textBoxTx4= Entry (groupBox)
        textBoxTx4.grid(row=5,column=5)

        LabelRx5=Label(groupBox,text="TrkRx5: ",width=13,font=("arial",12)).grid(row=6,column=0)
        textBoxRx5= Entry (groupBox)
        textBoxRx5.grid(row=6,column=1)

        LabelEq5=Label(groupBox,text="EquipoTx5: ",width=13,font=("arial",12)).grid(row=6,column=2)
        textBoxEq5= Entry (groupBox)
        textBoxEq5.grid(row=6,column=3)

        LabelTx5=Label(groupBox,text="TrkTx5: ",width=13,font=("arial",12)).grid(row=6,column=4)
        textBoxTx5= Entry (groupBox)
        textBoxTx5.grid(row=6,column=5)

        LabelTEC=Label(groupBox,text="Tecnología: ",width=13,font=("arial",12)).grid(row=7,column=0)
        selecTec = tk.StringVar()
        combo = ttk.Combobox(groupBox,values=["FTTH","FTTO","CMTS"],textvariable=selecTec)
        combo.grid(row=7,column=1)
        selecTec.set("FTTH")# Definir por defecto tecnología tipo FTTH

        LabelUbiDs=Label(groupBox,text="UbicaciónDest: ",width=13,font=("arial",12)).grid(row=7,column=2)
        textBoxUbiDs= Entry (groupBox)
        textBoxUbiDs.grid(row=7,column=3)

        LabelUbiRou=Label(groupBox,text="UbicaciónROU: ",width=13,font=("arial",12)).grid(row=7,column=4)
        textBoxUbiRou= Entry (groupBox)
        textBoxUbiRou.grid(row=7,column=5)
            
        Labelnuevo_id=Label(groupBox,text="id: ",width=13,font=("arial",12)).grid(row=7,column=6)
        textBoxid= Entry (groupBox)
        textBoxid.grid(row=7,column=7)

        #botones 

        Button(groupBox,text="GUARDAR",width=10,command=guardarRegistros).grid(row=8,column=2)
        Button(groupBox,text="Editar",width=10,command=modificarRegistros).grid(row=8,column=4)
        Button(groupBox,text="Borrar",width=10).grid(row=8,column=6)   

        #tabla
        groupBox1= LabelFrame(base,text="TRONCALES",padx=5,pady=5)
        groupBox1.place(x=10,y=450,width=1300,height=200)

        groupBox2=LabelFrame(base,text="ULTIMO REGISTRO GUARDADO",padx=10,pady=10)
        groupBox2.place(x=10,y=250,width=1300,height=130)

       # Frame para la barra de búsqueda
        search_frame = Frame(base)
        search_frame.place(x=10, y=400, width=1300, height=40)

        # Barra de búsqueda
        search_label = Label(search_frame, text="Buscar:")
        search_label.grid(row=0, column=0, padx=(10, 5))

        search_entry = Entry(search_frame, width=180)
        search_entry.grid(row=0, column=1)

        search_button = Button(search_frame, text="Buscar", width=10, command=buscar)

        search_button.grid(row=0, column=2, padx=(5, 10))

        # Centrar la barra de búsqueda dentro de search_frame
        search_frame.grid_rowconfigure(0, weight=1)
        search_frame.grid_columnconfigure(1, weight=1)

         #treeview realizar tabla 

        tree=ttk.Treeview(groupBox1,columns=("Equipo  destino","TrunkDest","TrkROU","Equipo ROU","TrkRx1","EquipoTx1","TrkTx1","TrkRx2"
                                                ,"EquipoTx2",	"TrkTx2",	"TrkRx3",	"EquipoTx3",	"TrkTx3",	"TrkRx4",	"EquipoTx4",
                                                "TrkTx4",	"TrkRx5",	"EquipoTx5",	"TrkTx5",	"Tecnologia","UbicaciónDest","UbicaciónRou,nuevo_id"),show="headings",height=5)
        
        column_headers = [
            ("Equipo destino", 100),
            ("TrunkDest", 100),
            ("TrkROU", 100),
            ("Equipo ROU", 100),
            ("TrkRx1", 100),
            ("EquipoTx1", 100),
            ("TrkTx1", 100),
            ("TrkRx2", 100),
            ("EquipoTx2", 100),
            ("TrkTx2", 100),
            ("TrkRx3", 100),
            ("EquipoTx3", 100),
            ("TrkTx3", 100),
            ("TrkRx4", 100),
            ("EquipoTx4", 100),
            ("TrkTx4", 100),
            ("TrkRx5", 100),
            ("EquipoTx5", 100),
            ("TrkTx5", 100),
            ("Tecnologia", 100),
            ("UbicaciónDest", 100),
            ("UbicaciónRou", 100),
        ]

        # Configurar columnas y encabezados de la tabla
        for index, (header_text, width) in enumerate(column_headers, start=1):
            tree.column("#" + str(index), anchor=CENTER, width=width)
            tree.heading("#" + str(index), text=header_text)
       

        #----ejecutar la funcion de seleccionar  haciendo click
        tree.bind("<<TreeviewSelect>>",seleccionarRegistro)
             
        # Crear la barra de desplazamiento horizontal
        scrollbar_x = Scrollbar(groupBox1, orient='horizontal', command=tree.xview)
        scrollbar_x.pack(side='bottom', fill='x')

        # Configurar la barra de desplazamiento para controlar el Treeview
        tree.configure(xscrollcommand=scrollbar_x.set)

        # Empaquetar el Treeview
        tree.pack(side='top', fill='both', expand=True)

        # Crear la nueva tabla en groupBox2
        tree1 = ttk.Treeview(groupBox2, columns=("Equipo  destino","TrunkDest","TrkROU","Equipo ROU","TrkRx1","EquipoTx1","TrkTx1","TrkRx2"
                                                ,"EquipoTx2",	"TrkTx2",	"TrkRx3",	"EquipoTx3",	"TrkTx3",	"TrkRx4",	"EquipoTx4",
                                                "TrkTx4",	"TrkRx5",	"EquipoTx5",	"TrkTx5",	"Tecnologia","UbicaciónDest","UbicaciónRou,nuevo_id"), show="headings", height=1)

            # Configurar las columnas y cabeceras de la tabla
        columns_and_headings = [
        ("# 1", "Equipo destino"),
        ("# 2", "TrunkDest"),
        ("# 3", "TrkROU"),
        ("# 4", "Equipo ROU"),
        ("# 5", "TrkRx1"),
        ("# 6", "EquipoTx1"),
        ("# 7", "TrkTx1"),
        ("# 8", "TrkRx2"),
        ("# 9", "EquipoTx2"),
        ("# 10", "TrkTx2"),
        ("# 11", "TrkRx3"),
        ("# 12", "EquipoTx3"),
        ("# 13", "TrkTx3"),
        ("# 14", "TrkRx4"),
        ("# 15", "EquipoTx4"),
        ("# 16", "TrkTx4"),
        ("# 17", "TrkRx5"),
        ("# 18", "EquipoTx5"),
        ("# 19", "TrkTx5"),
        ("# 20", "Tecnologia"),
        ("# 21", "UbicaciónDest"),
        ("# 22", "UbicaciónRou")
    ]

        for idx, (column, heading) in enumerate(columns_and_headings, start=1):
            tree1.column(column, anchor="center")
            tree1.heading(column, text=heading)

        # Insertar datos en la nueva tabla
        for row in Topologias.mostrarUltimo():
            tree1.insert("","end",values=row)
        # Configurar la barra de desplazamiento horizontal
        scrollbar_x2 = Scrollbar(groupBox2, orient='horizontal', command=tree1.xview)
        scrollbar_x2.pack(side='bottom', fill='x')

        # Configurar la barra de desplazamiento para controlar el Treeview
        tree1.configure(xscrollcommand=scrollbar_x2.set)

        # Empaquetar la nueva tabla
        tree1.pack(side='top', fill='both', expand=True)
        base.mainloop()#cerrar ventana
    except ValueError as error:
            print ("ERROR AL MOSTRAR LA INTERFAZ, ERROR: {}".format(error))

#grabar datos en la base de datos
def guardarRegistros():
     #variables globales
     global  combo,groupBox,textBoxEqDs,textBoxTD, textBoxTx1,textBoxTkR,textBoxEqRou,textBoxRx1,textBoxEq1,textBoxRx2,textBoxEq2,textBoxTx2,textBoxRx3,textBoxEq3,textBoxTx3,textBoxRx4,textBoxEq4,textBoxTx4,textBoxRx5,textBoxEq5,textBoxTx5,textBoxUbiDs,textBoxUbiRou
     # Lista de nombres de los campos de entrada
     fields = [
        textBoxEqDs, textBoxTD, textBoxTkR, textBoxEqRou,
        textBoxRx1, textBoxEq1, textBoxTx1,
        textBoxRx2, textBoxEq2, textBoxTx2,
        textBoxRx3, textBoxEq3, textBoxTx3,
        textBoxRx4, textBoxEq4, textBoxTx4,
        textBoxRx5, textBoxEq5, textBoxTx5,
        textBoxUbiDs, textBoxUbiRou]
    
     try:
        # Verificar si los campos de entrada están inicializados
        if any(field is None for field in fields) or combo is None:
            print("Los Widgets no están inicializados")
            return
        
        # Obtener valores de los campos de entrada
        values = [field.get() for field in fields]
        Tec = combo.get()
        
        # Llamar a una función para ingresar los registros
        Topologias.ingresarTroncal(*values, Tec)
        
        # Mostrar mensaje de información
        messagebox.showinfo("Información - Claro CO", "Los datos fueron guardados en el repositorio")
        
        # Actualizar la vista de tabla
        actualizarTreeview()
        
        # Limpiar los campos de entrada
        for field in fields:
            field.delete(0, END)
         
     except ValueError as error:
         print("Error al ingresar los datos,intentelo de nuevo{}".format(error))


def actualizarTreeview():###########error
    global tree,tree1

    try:
        #-----borrar elementos actuales de la tabla de visualizacion 
        tree.delete(*tree.get_children())#borrar todo el contenido excepto las cabeceras
        tree1.delete(*tree1.get_children())

        #obtener los nuevos datos a mostrar que se acaban de ingresar
        datosTroncal = Topologias.mostrarTroncal()
        datosUltimo = Topologias.mostrarUltimo()

        #insertar datos en treeview
        for row in datosTroncal:
         tree.insert("","end",values=row)

        for row in datosUltimo:
         tree1.insert("","end",values=row)
         
    except ValueError as error:
        print("Error al actualizar tabla{}".format(error))    


def seleccionarRegistro(event):
    try:
        itemSeleccionado=tree.focus()
        
        if itemSeleccionado:

            values = tree.item(itemSeleccionado)['values']
            # Definir los widgets y sus valores correspondientes
            widgets = [textBoxEqDs, textBoxTD, textBoxEqRou, textBoxRx1, textBoxEq1, textBoxTx1,
                       textBoxRx2, textBoxEq2, textBoxTx2, textBoxRx3, textBoxEq3, textBoxTx3,
                       textBoxRx4, textBoxEq4, textBoxTx4, textBoxRx5, textBoxEq5, textBoxTx5,
                       combo, textBoxUbiDs, textBoxUbiRou, textBoxid]
            # Definir los índices correspondientes a los valores en 'values'
            indices = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
            # Establecer los valores de los widgets
            for widget, index in zip(widgets, indices):
                widget.delete(0, END)
                widget.insert(0, values[index])
    except ValueError as error:
        print("Error al seleccionar registro{}".format(error))   
@staticmethod
def modificarRegistros():
     
     #variables globales
     global  combo,groupBox,textBoxEqDs,textBoxTD, textBoxTx1,textBoxTkR,textBoxEqRou,textBoxRx1,textBoxEq1,textBoxRx2,textBoxEq2,textBoxTx2,textBoxRx3,textBoxEq3,textBoxTx3,textBoxRx4,textBoxEq4,textBoxTx4,textBoxRx5,textBoxEq5,textBoxTx5,textBoxUbiDs,textBoxUbiRou,textBoxid
     try:
         #verificar si los elementos de interfaz estan iniciados
         if textBoxid is None or textBoxTD is None or combo is None:
             print("Los Widgets no estan inicializados")
             return
         EqDs =textBoxEqDs.get()
         TD = textBoxTD.get()
         TkR = textBoxTkR.get()
         EqRou = textBoxEqRou.get()
         Rx1 = textBoxRx1.get()
         Eq1 = textBoxEq1.get()
         Tx1 = textBoxTx1.get()
         Rx2 = textBoxRx2.get()
         Eq2 = textBoxEq2.get()
         Tx2 = textBoxTx2.get()
         Rx3 = textBoxRx3.get()
         Eq3 = textBoxEq3.get()
         Tx3 = textBoxTx3.get()
         Rx4 = textBoxRx4.get()
         Eq4 = textBoxEq4.get()
         Tx4 = textBoxTx4.get()
         Rx5 = textBoxRx5.get()
         Eq5 = textBoxEq5.get()
         Tx5 = textBoxTx5.get()
         UbiDs = textBoxUbiDs.get()
         UbiRou =textBoxUbiRou.get()
         Tec=combo.get()
         nuevo_id=textBoxid.get()#posible error definir variable en informacion nuevo_id    


         Topologias.modificarTroncal(EqDs,	TD,	TkR,	EqRou,	Rx1,	Eq1,	Tx1,	Rx2,	Eq2,	Tx2,	Rx3,	Eq3,	Tx3,	Rx4,	Eq4,	Tx4,	Rx5,	Eq5,	Tx5, Tec,	UbiDs, UbiRou,nuevo_id)
         messagebox.showinfo("Información - Claro CO","Los datos fueron guardados en el repositorio")

         actualizarTreeview()

         #limpiar pantalla
         textBoxEqDs,textBoxTD,textBoxTkR,textBoxEqRou,textBoxRx1,textBoxEq1,textBoxTx1,textBoxRx2,textBoxEq2,textBoxTx2,textBoxRx3,textBoxEq3,textBoxTx3,textBoxRx4,textBoxEq4,textBoxTx4,textBoxRx5,textBoxEq5,textBoxTx5,combo,textBoxUbiDs,textBoxUbiRou,textBoxid.delete(0,END)
         
         
     except ValueError as error:
         print("Error al ingresar los datos,intentelo de nuevo{}".format(error)) 


def buscar():
    global search_entry
    # Acceder al texto ingresado en el widget Entry
    term = search_entry.get()
    
    # Realizar búsqueda en la base de datos utilizando el término ingresado
    resultados = Topologias.mostrarTroncal(term)
    
    if resultados:
        # Limpiar árbol actual en groupBox1
        tree.delete(*tree.get_children())
        # Insertar los resultados de la búsqueda en el árbol
        for row in resultados:
            tree.insert("", "end", values=row)
    else:
        messagebox.showinfo("Búsqueda", "No se encontraron resultados para el término ingresado.")




Formulario()