import tkinter
from tkinter import *
from tkinter import filedialog, ttk
import xml.etree.ElementTree as ET
from xml import etree
from Matriz import matriz_ortogonal
from ListaSimple import ListaSimple
from graphviz import Digraph, Graph

matrices_ortogonales = ListaSimple()
contador_filas = 1
contador_columnas = 1
cont = 0
#Operaciones principales
def cargar_archivos():
    global contador_filas, contador_columnas
    try:
        ventana = tkinter.Tk()
        ruta = filedialog.askopenfilename(title="Seleccione un archivo", 
                filetypes = (("xml files","*.xml"),("all files","*.*")))
        ventana.destroy()

        tree = ET.parse(ruta)
        root = tree.getroot()

        for elemento in root:
            nombre = ''
            fila = 0
            columna = 0
            contador_elementos = 0
            matriz = matriz_ortogonal()
            for subelemento in elemento:
                
                if subelemento.tag == 'nombre':
                    nombre = subelemento.text
                elif subelemento.tag == 'filas':
                    fila = int(subelemento.text)
                elif subelemento.tag == 'columnas':
                    columna = int(subelemento.text)
                elif subelemento.tag == 'imagen':
                    lista = subelemento.text.split('\n')
                    
                    for x in lista:
                        for y in x:
                            if y == '*' or y == '-':
                                #print('Fila: ',str(contador_filas),'\tColumna: ',str(contador_columnas),'\tValor: ',y)
                                matriz.insertar(contador_filas,contador_columnas,y)
                                contador_columnas += 1
                                contador_elementos += 1
                            else:
                                continue
                        contador_columnas = 1
                        if x != '':
                            contador_filas += 1
                    contador_filas = 1

            if contador_elementos == fila*columna:
                if matrices_ortogonales.verificar_nombre(nombre):
                    print('Ya existe una matriz con este nombre')
                else:
                    print(fila, columna, contador_elementos, nombre)
                    matrices_ortogonales.insertar_simple(nombre,fila,columna,matriz)
            else:
                print('Los tamaños de la matriz no coinciden')  
    except IOError:
        print('Error al leer el archivo')

def operaciones():
    ventanaOperaciones = tkinter.Tk()
    ventanaOperaciones.title('Operaciones')
    ventanaOperaciones.resizable(1,1)
    ventanaOperaciones.geometry('880x160')

    '''frameOperaciones = tkinter.Frame(ventanaOperaciones,width='567',height='476',bg='green')
    frameOperaciones.pack()'''

    nb = ttk.Notebook(ventanaOperaciones)
    nb.pack(fill='both',expand='yes')

    p1 = ttk.Frame(nb)
    p2 = ttk.Frame(nb)
    p3 = ttk.Frame(nb)
    p4 = ttk.Frame(nb)
    p5 = ttk.Frame(nb)
    p6 = ttk.Frame(nb)
    p7 = ttk.Frame(nb)
    p8 = ttk.Frame(nb)

    #Agregrar todas las pestañas al frame
    nb.add(p1, text='Rotación horizontal')
    nb.add(p2, text='Rotación vertical')
    nb.add(p3, text='Transpuesta')
    nb.add(p4, text='Limpiar zona')
    nb.add(p5, text='Agregar linea horizontal')
    nb.add(p6, text='Agregar linea vertical')
    nb.add(p7, text='Agregar rectangulo')
    nb.add(p8, text='Agregar triangulo rectangulo')

    #Rotacion Horizontal -------------------
    var1 = Entry(p1)
    var1.place(x=100,y=15)

    def obtener1():
        nombres = rotacionHorizontal(var1.get())
        imagenes = nombres.split(',')

        rt = Toplevel()
        rt.title('Horizontal')

        miImagen = PhotoImage(file=imagenes[0]+'.png')
        Label(rt, image=miImagen).pack(side='left')

        miImagen2 = PhotoImage(file=imagenes[1]+'.png')
        Label(rt, image=miImagen2).pack(side='right')

        rt.mainloop()

    #Rotacion Vertical ---------------------
    var2 = Entry(p2)
    var2.place(x=100,y=15)
    def obtener2():
        nombres = rotacionVertical(var2.get())
        imagenes = nombres.split(',')

        rt = Toplevel()
        rt.title('Vertical')

        miImagen = PhotoImage(file=imagenes[0]+'.png')
        Label(rt, image=miImagen).pack(side='left')

        miImagen2 = PhotoImage(file=imagenes[1]+'.png')
        Label(rt, image=miImagen2).pack(side='right')

        rt.mainloop()

    #Transpuesta ---------------------------
    var3 = Entry(p3)
    var3.place(x=100,y=15)
    def obtener3():
        nombres = transpuesta(var3.get())
        imagenes = nombres.split(',')

        rt = Toplevel()
        rt.title('Transpuesta')

        miImagen = PhotoImage(file=imagenes[0]+'.png')
        Label(rt, image=miImagen).pack(side='left')

        miImagen2 = PhotoImage(file=imagenes[1]+'.png')
        Label(rt, image=miImagen2).pack(side='right')

        rt.mainloop()

    #Limpiar Zona --------------------------
    var4 = Entry(p4)
    var4.place(x=100,y=15)

    Label(p4, text='Fila inicio').place(x=400,y=15)
    varLimp0 = Entry(p4)
    varLimp0.place(x=250,y=15)

    Label(p4, text='Columna inicio').place(x=400,y=45)
    varLimp1 = Entry(p4)
    varLimp1.place(x=250,y=45)

    Label(p4, text='Fila final').place(x=400,y=75)
    varLimp2 = Entry(p4)
    varLimp2.place(x=250,y=75)

    Label(p4, text='Columna final').place(x=400,y=105)
    varLimp3 = Entry(p4)
    varLimp3.place(x=250,y=105)


    def obtener4():
        nombres = limpiar_zona(var4.get(), varLimp0.get(), varLimp1.get(), varLimp2.get(), varLimp3.get())
        imagenes = nombres.split(',')

        rt = Toplevel()
        rt.title('Limpiar Zona')

        miImagen = PhotoImage(file=imagenes[0]+'.png')
        Label(rt, image=miImagen).pack(side='left')

        miImagen2 = PhotoImage(file=imagenes[1]+'.png')
        Label(rt, image=miImagen2).pack(side='right')

        rt.mainloop()

    #Agregar linea horizontal --------------
    var5 = Entry(p5)
    var5.place(x=100,y=15)

    Label(p5,text='x').place(x=375,y=14)
    varLH0 = Entry(p5)
    varLH0.place(x=250,y=15)

    Label(p5, text='y').place(x=375,y=39)
    varLH1 = Entry(p5)
    varLH1.place(x=250,y=40)

    Label(p5, text='Elementos').place(x=375,y=64)
    varLH2 = Entry(p5)
    varLH2.place(x=250,y=65)

    def obtener5():
        nombres = agregar_linea_horizontal(var5.get(), varLH0.get(), varLH1.get(), varLH2.get())
        imagenes = nombres.split(',')

        rt = Toplevel()
        rt.title('Agregar linea horizontal')

        miImagen = PhotoImage(file=imagenes[0]+'.png')
        Label(rt, image=miImagen).pack(side='left')

        miImagen2 = PhotoImage(file=imagenes[1]+'.png')
        Label(rt, image=miImagen2).pack(side='right')

        rt.mainloop()

    #Agregar linea vertical ----------------
    var6 = Entry(p6)
    var6.place(x=100,y=15)

    Label(p6,text='x').place(x=375,y=14)
    varLV0 = Entry(p6)
    varLV0.place(x=250,y=15)

    Label(p6, text='y').place(x=375,y=39)
    varLV1 = Entry(p6)
    varLV1.place(x=250,y=40)

    Label(p6, text='Elementos').place(x=375,y=64)
    varLV2 = Entry(p6)
    varLV2.place(x=250,y=65)

    def obtener6():
        nombres = agregar_linea_vertical(var6.get(), varLV0.get(), varLV1.get(), varLV2.get())
        imagenes = nombres.split(',')

        rt = Toplevel()
        rt.title('Agregar linea vertical')

        miImagen = PhotoImage(file=imagenes[0]+'.png')
        Label(rt, image=miImagen).pack(side='left')

        miImagen2 = PhotoImage(file=imagenes[1]+'.png')
        Label(rt, image=miImagen2).pack(side='right')

        rt.mainloop()

    #Agregar Rectangulo ---------------------
    var7 = Entry(p7)
    var7.place(x=100,y=15)

    Label(p7, text='x').place(x=400,y=15)
    varRec0 = Entry(p7)
    varRec0.place(x=250,y=15)

    Label(p7, text='y').place(x=400,y=45)
    varRec1 = Entry(p7)
    varRec1.place(x=250,y=45)

    Label(p7, text='Filas').place(x=400,y=75)
    varRec2 = Entry(p7)
    varRec2.place(x=250,y=75)

    Label(p7, text='Columnas').place(x=400,y=105)
    varRec3 = Entry(p7)
    varRec3.place(x=250,y=105)

    def obtener7():
        nombres = agregar_rectangulo(var7.get(),varRec0.get(), varRec1.get(),varRec2.get(),varRec3.get())
        imagenes = nombres.split(',')

        rt = Toplevel()
        rt.title('Agregar rectangulo')

        miImagen = PhotoImage(file=imagenes[0]+'.png')
        Label(rt, image=miImagen).pack(side='left')

        miImagen2 = PhotoImage(file=imagenes[1]+'.png')
        Label(rt, image=miImagen2).pack(side='right')

        rt.mainloop()

    #Agregar triangulo rectangulo ----------
    var8 = Entry(p8)
    var8.place(x=100,y=15)

    Label(p8, text='x').place(x=400,y=15)
    varT0 = Entry(p8)
    varT0.place(x=250,y=15)

    Label(p8, text='y').place(x=400,y=45)
    varT1 = Entry(p8)
    varT1.place(x=250,y=45)

    Label(p8, text='Filas').place(x=400,y=75)
    varT2 = Entry(p8)
    varT2.place(x=250,y=75)

    Label(p8, text='Columnas').place(x=400,y=105)
    varT3 = Entry(p8)
    varT3.place(x=250,y=105)

    def obtener8():
        nombres = agregar_triangulo_rectangulo(var8.get(), varT0.get(), varT1.get(), varT2.get(), varT3.get())
        imagenes = nombres.split(',')

        rt = Toplevel()
        rt.title('Agregar triangulo rectangulo')

        miImagen = PhotoImage(file=imagenes[0]+'.png')
        Label(rt, image=miImagen).pack(side='left')

        miImagen2 = PhotoImage(file=imagenes[1]+'.png')
        Label(rt, image=miImagen2).pack(side='right')

        rt.mainloop()

    Button(p1, text='Elegir matriz', command=obtener1).place(x=10,y=10)
    Button(p2, text='Elegir matriz', command=obtener2).place(x=10,y=10)
    Button(p3, text='Elegir matriz', command=obtener3).place(x=10,y=10)
    Button(p4, text='Elegir matriz', command=obtener4).place(x=10,y=10)
    Button(p5, text='Elegir matriz', command=obtener5).place(x=10,y=10)
    Button(p6, text='Elegir matriz', command=obtener6).place(x=10,y=10)
    Button(p7, text='Elegir matriz', command=obtener7).place(x=10,y=10)
    Button(p8, text='Elegir matriz', command=obtener8).place(x=10,y=10)

    ventanaOperaciones.mainloop()

def operaciones_dos_imagenes():
    ventana_dos_operaciones = tkinter.Tk()
    ventana_dos_operaciones.title('Dos operaciones')
    ventana_dos_operaciones.resizable(1,1)
    ventana_dos_operaciones.geometry('400x150')

    nb = ttk.Notebook(ventana_dos_operaciones)
    nb.pack(fill='both',expand='yes')

    p1 = ttk.Frame(nb)
    p2 = ttk.Frame(nb)
    p3 = ttk.Frame(nb)
    p4 = ttk.Frame(nb)

    nb.add(p1, text='Unión')
    nb.add(p2, text='Intersección')
    nb.add(p3, text='Diferencia')
    nb.add(p4, text='Diferencia simétrica')

    #panel 1
    Label(p1, text='Matriz A').place(x=30, y=15)
    var1 = Entry(p1)
    var1.place(x=100,y=15)

    Label(p1, text='Matriz B').place(x=30, y=50)
    var2 = Entry(p1)
    var2.place(x=100,y=50)

    #panel 2
    Label(p2, text='Matriz A').place(x=30, y=15)
    var3 = Entry(p2)
    var3.place(x=100,y=15)

    Label(p2, text='Matriz B').place(x=30, y=50)
    var4 = Entry(p2)
    var4.place(x=100,y=50)

    #panel 3
    Label(p3, text='Matriz A').place(x=30, y=15)
    var5 = Entry(p3)
    var5.place(x=100,y=15)

    Label(p3, text='Matriz B').place(x=30, y=50)
    var6 = Entry(p3)
    var6.place(x=100,y=50)

    #panel 4
    Label(p4, text='Matriz A').place(x=30, y=15)
    var7 = Entry(p4)
    var7.place(x=100,y=15)

    Label(p4, text='Matriz B').place(x=30, y=50)
    var8 = Entry(p4)
    var8.place(x=100,y=50)

    def obtener_union():
        nombres = union_AB(var1.get(), var2.get())

        imagenes = nombres.split(',')

        rt = Toplevel()
        rt.resizable(0,0)
        rt.title('Union')

        miImagen = PhotoImage(file=imagenes[0]+'.png')
        Label(rt, image=miImagen).pack(side='left')

        miImagen2 = PhotoImage(file=imagenes[1]+'.png')
        Label(rt, image=miImagen2).pack(side='left')

        miImagen3 = PhotoImage(file=imagenes[2]+'.png')
        Label(rt, image=miImagen3).pack(side='left')

        rt.mainloop()


    def obtener_interseccion():
        nombres = interseccion_AB(var3.get(), var4.get())
        imagenes = nombres.split(',')

        rt = Toplevel()
        rt.resizable(0,0)
        rt.title('Intersección')

        miImagen = PhotoImage(file=imagenes[0]+'.png')
        Label(rt, image=miImagen).pack(side='left')

        miImagen2 = PhotoImage(file=imagenes[1]+'.png')
        Label(rt, image=miImagen2).pack(side='left')

        miImagen3 = PhotoImage(file=imagenes[2]+'.png')
        Label(rt, image=miImagen3).pack(side='left')

        rt.mainloop()

    def obtener_diferencia():
        nombres = diferencia_AB(var5.get(), var6.get())
        imagenes = nombres.split(',')

        rt = Toplevel()
        rt.resizable(0,0)
        rt.title('Intersección')

        miImagen = PhotoImage(file=imagenes[0]+'.png')
        Label(rt, image=miImagen).pack(side='left')

        miImagen2 = PhotoImage(file=imagenes[1]+'.png')
        Label(rt, image=miImagen2).pack(side='left')

        miImagen3 = PhotoImage(file=imagenes[2]+'.png')
        Label(rt, image=miImagen3).pack(side='left')

        rt.mainloop()
    def obtener_diferencia_simetrica():
        nombres = diferencia_simetrica_AB(var7.get(), var8.get())
        imagenes = nombres.split(',')

        rt = Toplevel()
        rt.resizable(0,0)
        rt.title('Intersección')

        miImagen = PhotoImage(file=imagenes[0]+'.png')
        Label(rt, image=miImagen).pack(side='left')

        miImagen2 = PhotoImage(file=imagenes[1]+'.png')
        Label(rt, image=miImagen2).pack(side='left')

        miImagen3 = PhotoImage(file=imagenes[2]+'.png')
        Label(rt, image=miImagen3).pack(side='left')

        rt.mainloop()

    Button(p1, text='Elegir matriz', command=obtener_union).place(x=250,y=25)
    Button(p2, text='Elegir matriz', command=obtener_interseccion).place(x=250,y=25)
    Button(p3, text='Elegir matriz', command=obtener_diferencia).place(x=250,y=25)
    Button(p4, text='Elegir matriz', command=obtener_diferencia_simetrica).place(x=250,y=25)

    

    ventana_dos_operaciones.mainloop()

def reportes():
    print('reportes')

def ayuda():
    print('Jelpmi')


#Generar imagenes --------------*****

def generar_imagen_original(matriz,nombre , fila, columna):
    global cont
    cadena = '< <table><tr>'+'<td>'+nombre+'</td>'
    for c in range(0,columna):
        cadena += '<td>'+str(c+1)+'</td>'
    cadena+='</tr>'

    for x in range(0,fila):
        cadena += '<tr>'+ '<td>'+str(x+1)+'</td>'
        for y in range(0,columna):
            if matriz.mostrar_uni(x+1,y+1) == '-':
                cadena += '<td></td>'
            else:
                cadena += '<td>'+ str(matriz.mostrar_uni(x+1,y+1)) +'</td>'
        cadena += '</tr>'
    cadena += '</table> >'

    g = Digraph('G',format='png')
    g.attr(label='Imagen original')
    g.node('S',label=cadena,shape='none')
    nombre = 'grafo'+str(cont)
    g.render(nombre)
    cont += 1

    return nombre

def generar_imagen(matriz,nombre , fila, columna):
    global cont

    cadena = '< <table><tr>'+'<td>'+nombre+'</td>'

    for c in range(0,columna):
        cadena += '<td>'+str(c+1)+'</td>'
    cadena+='</tr>'

    for x in range(0,fila):
        cadena += '<tr>'+ '<td>'+str(x+1)+'</td>'
        for y in range(0,columna):
            if matriz.mostrar_uni(x+1,y+1) == '-':
                cadena += '<td></td>'
            else:
                cadena += '<td>'+ str(matriz.mostrar_uni(x+1,y+1)) +'</td>'
        cadena += '</tr>'
    cadena += '</table> >'

    g = Digraph('G',format='png')
    g.attr(label='Resultado')
    g.node('S',label=cadena,shape='none')
    nombre = 'grafo'+str(cont)
    g.render(nombre)
    cont += 1
    return nombre

#Fin generar imagenes ----------*****


#Operaciones --------------------------------------------------------------

def rotacionHorizontal(nombre_de_matriz):
    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    matrizAux = matriz_ortogonal()
    filas = matriz0.x
    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar_como_vengan(filas,y+1,contenido)
        filas -= 1
    #matrizAux.recorrerFilas()

    nombreO = generar_imagen_original(matriz0.matriz,matriz0.nombre,matriz0.x, matriz0.y)
    nombreE = generar_imagen(matrizAux,matriz0.nombre, matriz0.x, matriz0.y)
    return nombreO+','+nombreE

def rotacionVertical(nombre_de_matriz):
    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    matrizAux = matriz_ortogonal()

    columnas = matriz0.y
    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar(x+1,columnas,contenido)
            columnas -= 1
        columnas = matriz0.y

    #matrizAux.recorrerFilas()
    nombreO = generar_imagen_original(matriz0.matriz,matriz0.nombre,matriz0.x, matriz0.y)
    nombreE = generar_imagen(matrizAux,matriz0.nombre, matriz0.x, matriz0.y)
    return nombreO+','+nombreE

def transpuesta(nombre_de_matriz):
    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    matrizAux = matriz_ortogonal()

    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar(y+1,x+1,contenido)

    #matrizAux.recorrerFilas()
    nombreO = generar_imagen_original(matriz0.matriz,matriz0.nombre,matriz0.x, matriz0.y)
    nombreE = generar_imagen(matrizAux,matriz0.nombre, matriz0.y, matriz0.x)
    return nombreO+','+nombreE

def limpiar_zona(nombre_de_matriz, filaA, columnaA, filaB, columnaB):
    
    fila0 = int(filaA)
    columna0 = int(columnaA)
    fila1 = int(filaB)
    columna1 = int(columnaB)

    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    print(matriz0.nombre)

    matrizAux = matriz_ortogonal()

    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar_como_vengan(x+1,y+1,contenido)

    for x in range(fila0,fila1+1):
        print('X: ',x)
        for y in range(columna0,columna1+1):
            print('Y: ',y)
            matrizAux.reemplazar_valor(x,y,'-')

    nombreO = generar_imagen_original(matriz0.matriz,matriz0.nombre,matriz0.x, matriz0.y)
    nombreE = generar_imagen(matrizAux,matriz0.nombre, matriz0.x, matriz0.y)
    return nombreO+','+nombreE

def agregar_linea_horizontal(nombre_de_matriz, x, y, elemento):

    fila = int(x)
    columna = int(y)
    columna1 = columna + int(elemento)-1
    

    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    print(matriz0.nombre)

    matrizAux = matriz_ortogonal()

    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar_como_vengan(x+1,y+1,contenido)

    for x in range(0,1):
        print('X: ',x)
        for y in range(columna,columna1+1):
            print('Y: ',y)
            matrizAux.reemplazar_valor(fila,y,'*')

    nombreO = generar_imagen_original(matriz0.matriz,matriz0.nombre,matriz0.x, matriz0.y)
    nombreE = generar_imagen(matrizAux,matriz0.nombre, matriz0.x, matriz0.y)
    return nombreO+','+nombreE

def agregar_linea_vertical(nombre_de_matriz, x, y, elemento):

    fila = int(x)
    columna = int(y)
    columna1 = columna + int(elemento)-1
    
    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    print(matriz0.nombre)

    matrizAux = matriz_ortogonal()

    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar_como_vengan(x+1,y+1,contenido)

    for x in range(fila,columna1):
        print('X: ',x)
        for y in range(0,1):
            print('Y: ',y)
            matrizAux.reemplazar_valor(x,columna,'*')

    nombreO = generar_imagen_original(matriz0.matriz,matriz0.nombre,matriz0.x, matriz0.y)
    nombreE = generar_imagen(matrizAux,matriz0.nombre, matriz0.x, matriz0.y)
    return nombreO+','+nombreE

def agregar_rectangulo(nombre_de_matriz, x, y, fila, columna):
    fila0 = int(x)
    columna0 = int(y)

    fila1 = fila0+(int(fila)-1)
    columna1 = columna0+(int(columna)-1)

    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    print(matriz0.nombre)

    matrizAux = matriz_ortogonal()

    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar_como_vengan(x+1,y+1,contenido)

    for x in range(fila0,fila1+1):
        #print('X: ',x)
        for y in range(columna0,columna1+1):
            #print('Y: ',y)
            matrizAux.reemplazar_valor(x,y,'*')

    nombreO = generar_imagen_original(matriz0.matriz,matriz0.nombre,matriz0.x, matriz0.y)
    nombreE = generar_imagen(matrizAux,matriz0.nombre, matriz0.x, matriz0.y)
    return nombreO+','+nombreE

def agregar_triangulo_rectangulo(nombre_de_matriz, x, y, fila, columna):

    Finicio = int(x) 
    Cinicio = int(y)

    filas = Finicio + int(fila)-1
    columnas = Cinicio + int(columna)-1

    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    print(matriz0.nombre)

    matrizAux = matriz_ortogonal()

    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar_como_vengan(x+1,y+1,contenido)
    pos = 1
    for x in range(Finicio, filas+1):
        print('X: ',x)
        for y in range(Cinicio,Cinicio+pos):
            print('Y: ',y)
            matrizAux.reemplazar_valor(x, y, '*')
        pos += 1
        
    nombreO = generar_imagen_original(matriz0.matriz,matriz0.nombre,matriz0.x, matriz0.y)
    nombreE = generar_imagen(matrizAux,matriz0.nombre, matriz0.x, matriz0.y)
    return nombreO+','+nombreE
            
#Fin operaciones ---------------------------------------------------------

#Operaciones con dos imágenes ********************************************

def union_AB(matrizA, matrizB):
    
    filas = 0
    columnas = 0

    matriz0 = matrices_ortogonales.mostrar_elemento(matrizA)
    matriz1 = matrices_ortogonales.mostrar_elemento(matrizB)

    matrizAux = matriz_ortogonal()

    if matriz0.x > matriz1.x:
        filas = matriz0.x
    else:
        filas = matriz1.x

    if matriz0.y > matriz1.y:
        columnas = matriz0.y
    else:
        columnas = matriz1.y

    for x in range(0, filas):
        for y in range(0, columnas):
            if matriz0.matriz.mostrar_uni(x+1,y+1) == '*' or matriz1.matriz.mostrar_uni(x+1,y+1) == '*':
                matrizAux.insertar(x+1,y+1,'*')
            else:
                matrizAux.insertar(x+1,y+1,'-')
    
    nombreA = generar_imagen_original(matriz0.matriz, matriz0.nombre,matriz0.x, matriz0.y)
    nombreB = generar_imagen_original(matriz1.matriz, matriz1.nombre,matriz1.x, matriz1.y)
    nombreC = generar_imagen(matrizAux,'Union', filas, columnas)
    return nombreA+','+nombreB+','+nombreC

def interseccion_AB(matrizA, matrizB):
    filas = 0
    columnas = 0

    matriz0 = matrices_ortogonales.mostrar_elemento(matrizA)
    matriz1 = matrices_ortogonales.mostrar_elemento(matrizB)

    matrizAux = matriz_ortogonal()

    if matriz0.x > matriz1.x:
        filas = matriz0.x
    else:
        filas = matriz1.x

    if matriz0.y > matriz1.y:
        columnas = matriz0.y
    else:
        columnas = matriz1.y

    for x in range(0, filas):
        for y in range(0, columnas):
            if matriz0.matriz.mostrar_uni(x+1,y+1) == '*' and matriz1.matriz.mostrar_uni(x+1,y+1) == '*':
                matrizAux.insertar(x+1,y+1,'*')
            else:
                matrizAux.insertar(x+1,y+1,'-')
    
    nombreA = generar_imagen_original(matriz0.matriz, matriz0.nombre,matriz0.x, matriz0.y)
    nombreB = generar_imagen_original(matriz1.matriz, matriz1.nombre,matriz1.x, matriz1.y)
    nombreC = generar_imagen(matrizAux,'Intersección', filas, columnas)
    return nombreA+','+nombreB+','+nombreC

def diferencia_AB(matrizA, matrizB):
    filas = 0
    columnas = 0

    matriz0 = matrices_ortogonales.mostrar_elemento(matrizA)
    matriz1 = matrices_ortogonales.mostrar_elemento(matrizB)

    matrizAux = matriz_ortogonal()

    if matriz0.x > matriz1.x:
        filas = matriz0.x
    else:
        filas = matriz1.x

    if matriz0.y > matriz1.y:
        columnas = matriz0.y
    else:
        columnas = matriz1.y

    for x in range(0, filas):
        for y in range(0, columnas):
            if matriz0.matriz.mostrar_uni(x+1,y+1) == '*' and matriz1.matriz.mostrar_uni(x+1,y+1) != '*':
                matrizAux.insertar(x+1,y+1,'*')
            else:
                matrizAux.insertar(x+1,y+1,'-')
    
    nombreA = generar_imagen_original(matriz0.matriz, matriz0.nombre,matriz0.x, matriz0.y)
    nombreB = generar_imagen_original(matriz1.matriz, matriz1.nombre,matriz1.x, matriz1.y)
    nombreC = generar_imagen(matrizAux,'Diferencia', filas, columnas)
    return nombreA+','+nombreB+','+nombreC

def diferencia_simetrica_AB(matrizA, matrizB):
    filas = 0
    columnas = 0

    matriz0 = matrices_ortogonales.mostrar_elemento(matrizA)
    matriz1 = matrices_ortogonales.mostrar_elemento(matrizB)

    matrizAux = matriz_ortogonal()
    matrizAux2 = matriz_ortogonal()

    matrizFinal = matriz_ortogonal()

    if matriz0.x > matriz1.x:
        filas = matriz0.x
    else:
        filas = matriz1.x

    if matriz0.y > matriz1.y:
        columnas = matriz0.y
    else:
        columnas = matriz1.y

    for x in range(0, filas):
        for y in range(0, columnas):
            if matriz0.matriz.mostrar_uni(x+1,y+1) == '*' and matriz1.matriz.mostrar_uni(x+1,y+1) != '*':
                matrizAux.insertar(x+1,y+1,'*')
            else:
                matrizAux.insertar(x+1,y+1,'-')
    
    for x in range(0, filas):
        for y in range(0, columnas):
            if matriz1.matriz.mostrar_uni(x+1,y+1) == '*' and matriz0.matriz.mostrar_uni(x+1,y+1) != '*':
                matrizAux2.insertar(x+1,y+1,'*')
            else:
                matrizAux2.insertar(x+1,y+1,'-')

    for x in range(0, filas):
        for y in range(0, columnas):
            if matrizAux.mostrar_uni(x+1,y+1) == '*' or matrizAux2.mostrar_uni(x+1,y+1) == '*':
                matrizFinal.insertar(x+1,y+1,'*')
            else:
                matrizFinal.insertar(x+1,y+1,'-')

    matrizAux.recorrerFilas()
    matrizAux2.recorrerFilas()
    
    
    nombreA = generar_imagen_original(matriz0.matriz, matriz0.nombre,matriz0.x, matriz0.y)
    nombreB = generar_imagen_original(matriz1.matriz, matriz1.nombre,matriz1.x, matriz1.y)
    nombreC = generar_imagen(matrizFinal,'Dif. Simetrica', filas, columnas)
    return nombreA+','+nombreB+','+nombreC

#Fin operaciones con dos imagenes ***************************************

root = tkinter.Tk()
root.title('Ventana Principal')
#root.geometry('1000x600')
root.resizable(0,0)

frame_principal = tkinter.Frame(root,width='751',height='250',bg='green')
frame_principal.pack()

tkinter.Button(frame_principal,text='Cargar Archivo', command=cargar_archivos, bg='gray',font=('Comic Sans MS',18)).place(x=0,y=0)

tkinter.Button(frame_principal,text='Operaciones', command=operaciones, bg='gray',font=('Comic Sans MS',18)).place(x=190,y=0)

tkinter.Button(frame_principal, text='Operaciones 2', command=operaciones_dos_imagenes,bg='gray', font=('Comic Sans MS',18)).place(x=352,y=0)

tkinter.Button(frame_principal,text='Reportes', command=reportes, bg='gray',font=('Comic Sans MS',18)).place(x=536,y=0)

tkinter.Button(frame_principal,text='Ayuda', command=ayuda, bg='gray',font=('Comic Sans MS',18)).place(x=660,y=0)

root.mainloop()