from tkinter import*     #--> importo Todo el contenido de la biblioteca
import random            #para crear un numero aleatorio de recibo
import datetime          #para que en el recibo me figure fecha y hora del dia
from tkinter import filedialog, messagebox     #para poder descargar el recibo en archivo txt

#------------------------------------------------------------------------------------------------------------------------------------------
#creo variables para darle FUNCIONALIDAD a la CALCULADORA y a funcion TOTAL:
operador = ''

#lista de precios:
precios_comida =[3000, 4000, 6000, 5000, 2000, 3000, 3000, 3000]
precios_bebidas =[800, 700, 700, 800, 1000, 2000, 2500, 5000]
precios_postres =[1500, 1500, 1600, 1800, 1900, 2300, 2700, 2500]


def click_boton(numero):         #  --> FUNCION PARA QUE LOS BOTONES DE LA CALCULADORA TENGAN VALOR <--
    global operador              #porque la variable operador se creó fuera de la funcion, se le pone global para q funcione adentro tambien-
    operador = operador + numero
    visor_calculadora.delete(0,END)   #para que en el visor no se muestre el contenido anterior, ni se acumule. borra todo a 0.
    visor_calculadora.insert(END, operador)

def borrar():                    #  --> FUNCION PARA QUE EL BOTON BORRAR DE LA CALCULADORA FUNCIONE <--
    global operador 
    operador = ''                #borra el contenido del visor para que no muestre lo escrito antes-
    visor_calculadora.delete(0, END)    

def obtener_resultado():
    global operador
    resultado = str(eval(operador))         #para que guarde el resultado de la operacion q estoy haciendo y lo convierta a str-
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''
#------------------------------------------------------------------------------------------------------------------------------------------
def revisar_check():

    #PARA COMIDAS:
    x = 0
    for c in cuadros_comida:      #comienza a recorrer la lista de comidas
        if variables_comidas[x].get() == 1:
            cuadros_comida[x].config(state = NORMAL)  #le cambia el estado para q se pueda escribir la cantidad- 
            if cuadros_comida[x].get() == '0':
               cuadros_comida[x].delete(0, END)       #para que borre el numero 0 que aparece cuando se habilita la casilla
            cuadros_comida[x].focus()                 #para que aparezca un CURSOR TITILANDO en la casilla
        else:
            cuadros_comida[x].config(state=DISABLED)  #cuando el cuadro esta deshabilitado
            texto_comida[x].set('0')                  #se borre el valor escrito y vuelva a 0
        x += 1                    #para que recorra toda la lista de comidas
    
    #PARA BEBIDAS:
    x = 0
    for c in cuadros_bebida:      
        if variables_bebidas[x].get() == 1:
            cuadros_bebida[x].config(state = NORMAL)  
            if cuadros_bebida[x].get() == '0':
               cuadros_bebida[x].delete(0, END)          
            cuadros_bebida[x].focus()                
        else:
            cuadros_bebida[x].config(state=DISABLED)  
            texto_bebida[x].set('0')                  
        x += 1     

    #PARA POSTRES:
    x = 0
    for c in cuadros_postre:      
        if variables_postres[x].get() == 1:
            cuadros_postre[x].config(state = NORMAL)  
            if cuadros_postre[x].get() == '0':
               cuadros_postre[x].delete(0, END)          
            cuadros_postre[x].focus()                
        else:
            cuadros_postre[x].config(state=DISABLED)  
            texto_postre[x].set('0')                  
        x += 1       

#-----------------------------------------------------------------------------------------------------------------------------
def total():
    #PARA COMIDAS--
    sub_total_comida = 0
    p = 0                  #contador de precio
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1
      

    #PARA BEBIDAS--
    sub_total_bebida = 0
    p = 0                  #contador de precio
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebidas[p])
        p += 1
    
    
    #PARA POSTRES--
    sub_total_postre =0
    p = 0                  #contador de precio
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre +  (float(cantidad.get()) * precios_postres[p])
        p += 1

    #calculos de total y subtotal 
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set (f'$ {round (sub_total_comida, 2)}')
    var_costo_bebida.set (f'$ {round (sub_total_bebida, 2)}')
    var_costo_postre.set (f'$ {round (sub_total_postre, 2)}')
    var_subtotal.set (f'$ {round (sub_total, 2)}')
    var_impuesto.set(f'$ {round (impuestos, 2)}')
    var_total.set (f'$ {round (total, 2)}')
#-----------------------------------------------------------------------------------------------------------------------------
def recibo():
    texto_recibo.delete(1.0, END)                       #borra cualquier contenido anterior del recibo
    num_recibo = f'Nº - {random.randint(1000, 9999)}'   #tira un numero aleatorio
    fecha = datetime.datetime.now()                     #imprime la fecha de hoy
    fecha_recibo = f'{fecha.day}/ {fecha.month}/ {fecha.year} - {fecha.hour}: {fecha.minute}'  #el formato que imprimo en el recibo
    texto_recibo.insert(END, f'Datos:\t {num_recibo} \t\t {fecha_recibo}\n')
    texto_recibo.insert(END, f'*'*56 + '\n')             #decora con linea de asteriscos
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-'*67 + '\n')             #decora con una lines de guiones

    #PARA COMIDAS--
    x = 0
    for comida in texto_comida:
        if comida.get() != '0':   #para que solo tome en cuenta a las comidas q fueron seleccionadas
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t {comida.get()}\t ${int(comida.get()) *  precios_comida[x]}\n')
        x += 1 

    #PARA BEBIDAS--
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':   #para que solo tome en cuenta a las comidas q fueron seleccionadas
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t {bebida.get()}\t ${int(bebida.get()) *  precios_bebidas[x]}\n')
        x += 1 

    #PARA POSTRES--
    x = 0
    for postre in texto_postre:
        if postre.get() != '0':   #para que solo tome en cuenta a las comidas q fueron seleccionadas
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t {postre.get()}\t ${int(postre.get()) *  precios_postres[x]}\n')
        x += 1     
    texto_recibo.insert(END, f'-'*67 + '\n')             #decora con una lines de guiones  
    texto_recibo.insert(END, f'Costo de Comida: \t\t\t {var_costo_comida.get()}\n')  
    texto_recibo.insert(END, f'Costo de Bebida: \t\t\t {var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de Postre: \t\t\t {var_costo_postre.get()}\n')   
    texto_recibo.insert(END, f'-'*67 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t {var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t {var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t {var_total.get()}\n')
    texto_recibo.insert(END, f'-'*67 + '\n')
    texto_recibo.insert(END, 'Lo Esperamos Pronto!')
#-----------------------------------------------------------------------------------------------------------------------------
#PARA GUARDAR EL RECIBO COMO ARCHIVO DE TEXTO---
def guardar():
    info_recibo = texto_recibo.get(1.0, END)     #guardo el contenido del recibo en una variable
    archivo = filedialog.asksaveasfile(mode='w', defaultextension= '.txt')  #guardo en un archivo txt
    archivo.write(info_recibo)   #escribo el recibo
    archivo.close()              #cierro el archivo
    messagebox.showinfo('Informacion', 'Su Recibo Ha Sido Guardado!') #abre una ventana cuando ya guardé el archivo de texto
#-----------------------------------------------------------------------------------------------------------------------------
#PARA BOTON RESETEAR Y ARRANCAR CON UN NUEVO CLIENTE--
def resetear():
    texto_recibo.delete(0.1, END)   #borra el contenido del panel de recibos
    
    for texto in texto_comida:             #  --->para BORRAR el numero de las CANTIDADES de productos--
        texto.set('0')
    
    for texto in texto_bebida:
        texto.set('0')
    
    for texto in texto_postre:
        texto.set('0')
    #----------------------------
    for cuadro in cuadros_comida:          # -->para CAMBIAR estado de los cuadros y que queden DESHABILITADOS--
        cuadro.config(state=DISABLED)
    
    for cuadro in cuadros_bebida:
        cuadro.config(state= DISABLED)
     
    for cuadro in cuadros_postre:
        cuadro.config(state= DISABLED)        
     #----------------------------
    for variable in variables_comidas:      #para DESACTIVAR los CHECK --
        variable.set(0)
    
    for variable in variables_bebidas:
        variable.set(0)
     
    for variable in variables_postres:
        variable.set(0)
     #----------------------------
    var_costo_comida.set('')                #para BORRRAR el contenido de los cuadros del panel costos
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


#-----------------------------------------------------------------------------------------------------------------------------

#iniciar tkinter--
aplicacion = Tk()        #guardo en una variable el contenido de funcion Tk 
                         #para poder aplicar los métodos en mi programa y para abrir una ventana

#tamaño de la ventana--
aplicacion.geometry ('1020x630+0+0')   # el método geometry recibe 3 parametros: 
                                       #las medidas alto x ancho, la ubicacion en eje "x", la ubicacion en eje "y"                      

#evitar que se le cambie el tamaño a la ventana--
aplicacion.resizable(0,0)              #metodo resizable recibe 2 parametros: eje "x", eje "y".

#titulo de la ventana--
aplicacion.title("Proyecto RESTAURANTE")
aplicacion.iconbitmap('C:\\Users\\usuario\\Desktop\\python\\parte_grafica\\tkinter\\restaurante\\icono.ico')

#color de fondo de la ventana
aplicacion.config(bg='#dac9df')     #bg = background 

#-->PANEL SUPERIOR
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)  #Frame es un constructor: recibe adonde se va a aplicar, bd= borde, relief = apariencia del borde
panel_superior.pack(side=TOP)                          #ubicacion: top -->arriba

#etiqueta titulo--
etiqueta_titulo = Label(panel_superior, text="MI RESTAURANTE", fg="#fbd5e5", font=('Nunito', 47), bg='#81638b', width= 28) #label es etiqueta/ fg= color de fuente/ font= elijo cualquiera
etiqueta_titulo.grid(row=0, column=0)      #grid es grilla/row es fila/column es columna. 

#-->PANEL IZQUIERDO--
panel_izquierdo = Frame(aplicacion, bd=1, relief= FLAT)  #uso el constructor Frame
panel_izquierdo.pack(side=LEFT)                          #la ubicacion con ".pack" es en side left-->izquierdo

#PANEL COSTOS--
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='#b695c0', padx=55)
panel_costos.pack(side=BOTTOM)                            #ubicacion bottom es abajo de todo

#PANEL COMIDAS--
panel_comidas = LabelFrame(panel_izquierdo, text='Comidas', font=('Nunito', 15, 'bold'), bg='#f7bfd8',bd=1, relief=FLAT, fg='#81638b')
panel_comidas.pack(side=LEFT)

#PANEL BEBIDAS--
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font= ('Nunito', 15,'bold'), bg='#f7bfd8', bd=1, relief= FLAT, fg='#81638b')
panel_bebidas.pack(side=LEFT)

#PANEL POSTRES--
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Nunito', 15, 'bold'), bg='#f7bfd8',bd=1, relief=FLAT, fg='#81638b')
panel_postres.pack(side=LEFT)

#-->PANEL DERECHA--
panel_derecha = Frame(aplicacion, bd=1, relief= FLAT)
panel_derecha.pack(side=RIGHT)

#PANEL CALCULADORA--
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='#b695c0')
panel_calculadora.pack()       #-->si no se le pone ubicacion, por defecto va en la parte de arriba

#PANEL RECIBO--
panel_recibo = Frame (panel_derecha, bd=1, relief=FLAT, bg='#b695c0')
panel_recibo.pack()            #-->si no se le pone ubicacion, por defecto va en la parte de arriba

#PANEL BOTONES--
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT,  bg='#b695c0')
panel_botones.pack()           #-->si no se le pone ubicacion, por defecto va en la parte de arriba
#----------------------------------------------------------------------------------------------------------

#lista de productos--
lista_comidas = ['Pollo','Carne', 'Salmón', 'Cordero', 'Ensalada', 'Tarta', 'Pizza', 'Ravioles']
lista_bebidas = ['Agua', 'Jugo', 'Gaseosa naranja', 'Gaseosa cola', 'Cerveza', 'Vino', 'Sidra','Champagne']
lista_postres = ['Helado','Flan','Budin de pan','Tarta de Manzana', 'Tarta de Frutilla', 'Chocotorta','Selva Negra','Tiramisú']

#generar items COMIDAS--
variables_comidas =[]
cuadros_comida =[]
texto_comida = []

contador = 0
for comida in lista_comidas:

    #crear Checkbutton--
    variables_comidas.append('')
    variables_comidas[contador] = IntVar()              #IntVar es una variable integer de Tkinter
    comida = Checkbutton(panel_comidas,                 #el boton check está dentro de un bucle de la lista de comidas
                         text=comida.title(), 
                         font= ('Nunito',14, 'bold'),
                         bg='#f7bfd8', 
                         onvalue=1,                     #onvalue es 1 porque es cuando la casilla está activada/
                         offvalue=0,                    #el valor es 0 cuando esta desactivada
                         variable=variables_comidas[contador],
                         command= revisar_check)   #llama a la funcion revisar
                  
    comida.grid(row=contador,                           #--> ".grid"es donde se va a ubicar dentro del panel
                column=0,                               # las filas son segun el contador
                sticky=W)                               #sticky es la ubicacion este
                                                  
    #Crear Cuadros de entrada--   
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()                #variable del tipo string propia de Tkinter
    texto_comida[contador].set(0)
    cuadros_comida[contador] = Entry (panel_comidas,                   #es la ubicacion.
                                      font=('Nunito', 13, 'bold'),     #fuente, tamaño y tipo negrita
                                      bd=1,                            #borde
                                      width= 5,                        #ancho
                                      state=DISABLED,                  #estado_desahbilitado
                                      textvariable=texto_comida[contador])    
    cuadros_comida[contador].grid(row= contador,
                                  column=1
                                  )
    contador +=1    #-->para que cada vez q recorre el for, incremente y se posicione uno debajo del otro.                                           

#generar items BEBIDAS--
variables_bebidas =[]
cuadros_bebida =[]
texto_bebida = []

contador = 0
for bebida in lista_bebidas:

    #crear Checkbutton--
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton (panel_bebidas, 
                          text= bebida.title(),
                          font= ('Nunito',14, 'bold'),
                          bg='#f7bfd8', 
                          onvalue=1, 
                          offvalue=0, 
                          variable= variables_bebidas[contador],
                          command= revisar_check)
    
    bebida.grid(row= contador, 
                column= 0, 
                sticky=W)
    #Crear Cuadros de entrada--   
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()                #variable del tipo string propia de Tkinter
    texto_bebida[contador].set(0)
    cuadros_bebida[contador] = Entry (panel_bebidas,                   #es la ubicacion.
                                      font=('Nunito', 13, 'bold'),     #fuente, tamaño y tipo negrita
                                      bd=1,                            #borde
                                      width= 5,                        #ancho
                                      state=DISABLED,                  #estado_desahbilitado
                                      textvariable=texto_bebida[contador])    
    cuadros_bebida[contador].grid(row= contador,
                                  column=1
                                  )
    contador +=1

#generar items POSTRES--
variables_postres =[]
cuadros_postre =[]
texto_postre = []
   
contador = 0
for postre in lista_postres:

    #crear Checkbutton--
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton (panel_postres, 
                          text= postre.title(),
                          font= ('Nunito',14, 'bold'),
                          bg='#f7bfd8', 
                          onvalue=1, 
                          offvalue=0, 
                          variable= variables_postres[contador],
                          command= revisar_check)
    
    postre.grid(row=contador, 
                column=0, 
                sticky=W)
    
    #Crear Cuadros de entrada--   
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()                #variable del tipo string propia de Tkinter
    texto_postre[contador].set(0)
    cuadros_postre[contador] = Entry (panel_postres,                   #es la ubicacion.
                                      font=('Nunito', 13, 'bold'),     #fuente, tamaño y tipo negrita
                                      bd=1,                            #borde
                                      width= 5,                        #ancho
                                      state=DISABLED,                  #estado_desahbilitado
                                      textvariable=texto_postre[contador])    
    cuadros_postre[contador].grid(row= contador,
                                  column=1
                                  )
    contador +=1
#-----------------------------------------------------------------------------------------------------------------------
#lista de variables:
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

#etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Nunito', 12, 'bold'),
                              bg='#b695c0',
                              fg='#fbd5e5')
etiqueta_costo_comida.grid(row=0,
                           column=0)
texto_costo_comida = Entry(panel_costos,
                           font=('Nunito', 12, 'bold'),
                           bd=1,
                           width=10,
                           state= 'readonly',   #para que el estado sea de solo lectura
                           textvariable= var_costo_comida)
texto_costo_comida.grid(row=0,
                        column=1,
                        padx=41)

#etiquetas de costo y campos de entrada
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Nunito', 12, 'bold'),
                              bg='#b695c0',
                              fg='#fbd5e5')
etiqueta_costo_bebida.grid(row=1,
                           column=0)
texto_costo_bebida = Entry(panel_costos,
                           font=('Nunito', 12, 'bold'),
                           bd=1,
                           width=10,
                           state= 'readonly',   #para que el estado sea de solo lectura
                           textvariable= var_costo_bebida)
texto_costo_bebida.grid(row=1,
                        column=1,
                        padx=41)

#etiquetas de costo y campos de entrada
etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postre',
                              font=('Nunito', 12, 'bold'),
                              bg='#b695c0',
                              fg='#fbd5e5')
etiqueta_costo_postre.grid(row=2,
                           column=0)
texto_costo_postre = Entry(panel_costos,
                           font=('Nunito', 12, 'bold'),
                           bd=1,
                           width=10,
                           state= 'readonly',   #para que el estado sea de solo lectura
                           textvariable= var_costo_postre)
texto_costo_postre.grid(row=2,
                        column=1,
                        padx=41)

#etiquetas de costo y campos de entrada
etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Nunito', 12, 'bold'),
                              bg='#b695c0',
                              fg='#fbd5e5')
etiqueta_subtotal.grid(row=0,
                           column=2)
texto_subtotal = Entry(panel_costos,
                           font=('Nunito', 12, 'bold'),
                           bd=1,
                           width=10,
                           state= 'readonly',   #para que el estado sea de solo lectura
                           textvariable= var_subtotal)
texto_subtotal.grid(row=0,
                    column=3,
                    padx=41)

#etiquetas de costo y campos de entrada
etiqueta_impuestos = Label(panel_costos,
                              text='Impuestos',
                              font=('Nunito', 12, 'bold'),
                              bg='#b695c0',
                              fg='#fbd5e5')
etiqueta_impuestos.grid(row=1,
                           column=2)
texto_impuestos = Entry(panel_costos,
                           font=('Nunito', 12, 'bold'),
                           bd=1,
                           width=10,
                           state= 'readonly',   #para que el estado sea de solo lectura
                           textvariable= var_impuesto)
texto_impuestos.grid(row=1,
                    column=3,
                    padx=41)

#etiquetas de costo y campos de entrada
etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Nunito', 12, 'bold'),
                              bg='#b695c0',
                              fg='#fbd5e5')
etiqueta_total.grid(row=2,
                           column=2)
texto_total = Entry(panel_costos,
                           font=('Nunito', 12, 'bold'),
                           bd=1,
                           width=10,
                           state= 'readonly',   #para que el estado sea de solo lectura
                           textvariable= var_total)
texto_total.grid(row=2,
                 column=3,
                 padx=41)
#----------------------------------------------------------------------------------------------------------------------
#BOTONES --
botones = ['Total', 'Recibo', 'Guardar', 'Borrar']
botones_creados =[]

columnas = 0   #contador para ubicar botones
for boton in botones:
    boton = Button(panel_botones,
                   text= boton.title(),
                   font= ('Nunito',12, 'bold'),
                   fg='white',
                   bg='#f7bfd8',
                   bd=1,
                   width=8)
    botones_creados.append(boton)

    boton.grid(row=0,
               column= columnas)
    columnas +=1

botones_creados[0].config(command = total)    
botones_creados[1].config(command = recibo)
botones_creados[2].config(command = guardar)
botones_creados[3].config(command = resetear)  #para borrar el contenido de un cliente y que todos los items vuelvan a 0.
#----------------------------------------------------------------------------------------------------------------------
#area recibo--
texto_recibo = Text(panel_recibo,
                   font= ('Nunito',11, 'bold'),
                   bd=1,
                   width=42,
                   height=10)
texto_recibo.grid(row=0,
                 column=0)
#----------------------------------------------------------------------------------------------------------------------
#CALCULADORA --
visor_calculadora = Entry(panel_calculadora,
                          font=('Nunito',14, 'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)  #para que ocupe todas las columnas

#botones de calculadora--
botones_calculadora = ['7','8','9', '+', '4', '5', '6', '-', '1', '2','3','x', '=', 'Borrar', '0', '/']

botones_guardados = [] #lista vacía para almacenar el valor de CADA BOTON.

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text= boton.title(),
                   font= ('Nunito', 13, 'bold'),
                   fg='white',
                   bg= '#dac9df',
                   bd=1,
                   width=8)
    botones_guardados.append(boton)  #guarda en la lista cada boton.

    boton.grid(row= fila,
               column= columna)
    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))        #llamo a la funcion click_boton para que el 7 tenga valor en la calculadora
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)                 #command llama a la funcion creada arriba
botones_guardados[13].config(command=borrar)                            #command llama a la funcion creada arriba
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))



#-----------------------------------------------------------------------------------------------------------------------
#evitar que la pantalla se cierre--
aplicacion.mainloop()            # -->crea un bucle que hace que la ventana permanezca abierta                         

