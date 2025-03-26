import dccortaramas
import sys
import os

def opciones_inicio_menu():
    print("[1] Cargar bonsái\n[2] Salir del programa\nIndique su opción (1, 2):")
def inicio_menu():
    print("¡Bienvenido a DCCortaramas!\n*** Menu de Inicio ***")
    opciones_inicio_menu()
def opciones_segundo_menu():
    print("*** Menú de Acciones ***\n[1] Visualizar bonsái\n[2] Modificar Hoja\n[3] Cortar Rama\n[4] Verificar Simetría\n[5] Podar bonsái\n[6] Salir del programa\nIndique su opción (1, 2, 3, 4, 5, 6):")
def segundo_menu():
    print("¡Bienvenido a DCCortaramas!\nEs hora de convertir tu bonsái en un hermoso bonsái.")
    opciones_segundo_menu()
def ahorro():
    ahorro= input("¿Quieres podar con ahorro?, ¿si o no? : ")
 
#esta funcion ocupo la libreria os para poder revisar si la carpeta es parte del data
def verificar_existencia_carpeta():
    # Obtener la ruta del directorio donde se encuentra el archivo main.py
    
    verificar_carpeta = os.path.dirname(os.path.abspath(__file__))
    #print(f"Ruta donde se encuentra el script: {verificar_carpeta}\n")
    ver_en_data = os.path.join(verificar_carpeta, "data")
    carpeta = input(f"Ingresa el nombre de la carpeta dentro de {ver_en_data}: ")
    verificar_nombre_carpeta = os.path.join(ver_en_data, carpeta)

    #verifico si existe en el data la carpeta
    if os.path.isdir(verificar_nombre_carpeta):  
        print(f"\nLa carpeta '{carpeta}' existe dentro de 'data'.")
        return verificar_nombre_carpeta
    else:
        print(f"\nLa carpeta '{carpeta}' no existe dentro de 'data'. Por favor verifica el nombre.")
        return None
    
#esta funcion ocupo la libreria os para revisar que el archivo sea de la carpeta que verefique anteriormente en data
def verificar_existencia_archivo(carpeta):
    archivo= input(f"Ingresa el nombre del archivo: ")
    verificar_nombre_archivo = os.path.join(carpeta, archivo)
    
    #verifico el nombre del archivo esta en la carpeta entregada
    if os.path.isfile(verificar_nombre_archivo):
        print(f"\nEl archivo '{archivo}' existe dentro de 'carpeta'.")
        return archivo
    
    else:
        print(f"\nEl archivo '{archivo}' no existe dentro de 'carpeta'. Por favor verifica el nombre.")
        return False
v= 0

while v != 1:
    inicio_menu()
    opcion_persona= input("Ingresa un numero: ")

    #indico menu parte1, se verifica con las funciones que ocupan os
    if opcion_persona == "1":
        #reviso la existencia de la carpeta y a la vez la existencia del archivo
        carpeta = verificar_existencia_carpeta()
        if not carpeta: # el usuario se equivoco al ingresar alguna wea
            print("\nCarpeta equivocada, ingresa nuevamente al menu")
        elif carpeta:
            archivo= verificar_existencia_archivo(carpeta)
            if not archivo: 
                print("\nArchivo equivocado, ingresa al menu nuevamente")
            else:
                v= 1
    
    elif opcion_persona == "2":
        sys.exit()
        v= 1

#segunda parte del menu, en casi todas las funciones se utiliza la libreria sys para terminar el codigo y el menu cerrarlo
#ademas tambien uso el import dccortarama para poder revisar las funciones hechas alla
while v != 0:
    segundo_menu()
    segunda_opcion_persona= int(input("Ingresa un numero: "))
    clase_dcc= dccortaramas.DCCortaRamas()
    clase_bonsai= dccortaramas.Bonsai("victor", 10, 27, [])
    clase_bonsai.cargar_bonsai_de_archivo(carpeta, archivo)

    #verifico con la funcion visualizar_bonsai del import de dccortarama para utilizar la funcion
    if segunda_opcion_persona == 1: #visualizar_bonsai
        clase_bonsai.visualizar_bonsai("Vertical", True, False)
        sys.exit()

    #verifico con la funcion modificar_nodo del import dccortarama
    elif segunda_opcion_persona == 2: #modificar_nodo
        identificador= input("Ingresa un identificador del nodo: ")
        v= clase_dcc.modificar_nodo(clase_bonsai, identificador)
        if v == "No permitido" or v == "No encontrado":
            print("No se pudo realizar")
        else:
            print("Se pudo realizar")
            print(clase_bonsai.estructura)
        sys.exit()

    #verifico con la funcion quitar_nodo del import dccortarama
    elif segunda_opcion_persona == 3: #quitar_nodo
        identificador= input("Ingresa identificador del nodo: ")
        v= clase_dcc.quitar_nodo(clase_bonsai, identificador)
        if v == "No permitido" or v == "No encontrado":
            print("No se pudo realizar")
        else:
            print("Se pudo realizar")
        sys.exit()

    #verifico con la funcion es_simetrico del import dccortarama
    elif segunda_opcion_persona == 4: #es simetrico
        v= clase_dcc.es_simetrico(clase_bonsai)
        if v:
            print("La estructura es simetrica")
        elif not v:
            print("La estructura no es simetrica")
        sys.exit()

    #verifico con la funcion emparejar_bonsai o emparejar_bonsai_ahorro del import dccortarama
    elif segunda_opcion_persona == 5: #esta funcion no la termine

        ahorro= input("¿Quieres podar con ahorro?, ¿si o no? : ")
        if ahorro == "si":
            dccortaramas.emparejar_bonsai_ahorro(clase_bonsai) #falta hacer condiciones de si se logro hacerlo o no
            #no logre hacer la funcion
        elif ahorro == "no":
            dccortaramas.emparejar_bonsai(clase_bonsai) #falta hacer condiciones de si se logro hacerlo o no
            #no logre hacer la funcion
        else:
            ahorro()
        sys.exit()

    #utilizo sys.exit() de la libreria sys para acabar el programa y salir del menu
    elif segunda_opcion_persona == 6: #salir del programa
        v= 1
        sys.exit()