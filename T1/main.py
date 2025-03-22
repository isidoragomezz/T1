import dccortaramas
import sys

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
v= 0
while v != 1:
    inicio_menu()
    opcion_persona= int(input("Ingresa un numero: "))
    if opcion_persona == 1:
        carpeta= input("Ingresa el nombre de la carpeta: ")
        archivo= input("Ingresa el nombre del archivo: ")
        v= 1
        break
    elif opcion_persona == 2:
        sys.exit()
        v= 1

while v != 0:
    segundo_menu()
    segunda_opcion_persona= int(input("Ingresa un numero: "))
    clase_dcc= dccortaramas.DCCortaRamas()
    clase_bonsai= dccortaramas.Bonsai("victor", 10, 27, [])

    if segunda_opcion_persona == 1:
        clase_bonsai.cargar_bonsai_de_archivo(carpeta, archivo)
        clase_bonsai.visualizar_bonsai("Vertical", True, False)
        sys.exit()
    elif segunda_opcion_persona == 2:
        clase_dcc.modificar_nodo(clase_bonsai, 3)
        sys.exit()
    elif segunda_opcion_persona == 3:
        clase_dcc.quitar_nodo(clase_bonsai, "4")
        sys.exit()

    elif segunda_opcion_persona == 4:
        clase_dcc.es_simetrico(clase_bonsai)
        sys.exit()

    elif segunda_opcion_persona == 6:
        sys.exit()
        v= 0
