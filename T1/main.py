import dccortaramas
import prettyprint

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
        nombre_carpeta= input("Ingresa el nombre de la carpeta: ")
        nombre_archivo= input("Ingresa el nombre del archivo: ")
        v= 1
        break
    elif opcion_persona == 2:
         break

while v != 0:
    segundo_menu()
    segunda_opcion_persona= int(input("Ingresa un numero: "))
    if segunda_opcion_persona == 1:
        clase_bonsai= dccortaramas.Bonsai()
        clase_bonsai.visualizar_bonsai()
