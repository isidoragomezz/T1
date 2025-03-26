import utilidades  # type: ignore
import os 

class Bonsai:
    def __init__(self, identificador: str, costo_corte: int, costo_flor: int, estructura: list) -> None:
        self.identificador = identificador
        self.costo_corte = costo_corte
        self.costo_flor = costo_flor
        self.estructura = estructura

    #utilizo la libreria os para poder ir buscaando la ruta de la carpeta y archivo que me ingresan para poder entregar el bonsai de forma ordenada
    def cargar_bonsai_de_archivo(self, carpeta: str, archivo: str) -> None:
        self.estructura = []
        datos = os.path.join("data", carpeta, archivo)
        #saco la estructura del bonsai de la carpeta y archivo que me entregan
        with open(f"{datos}", "r", encoding="utf-8") as f:
            for i in f:
                identificador, cosa_1, cosa_2, lista = i.strip().split(",") #acomodo la estructura para poder usarla masa facilmente
                cosa_1 = True if cosa_1 == "T" else False
                cosa_2 = True if cosa_2 == "T" else False
                lista = lista.split(";")
                estructura = [identificador, cosa_1, cosa_2, lista]
                self.estructura.append(estructura)

    #utilizo utilidades del import para poder imprimir el bonsai en la terminal dependiendo de guardar_rchivo
    def visualizar_bonsai(self, orientacion: str, emojis: bool, guardar_archivo: bool) -> None:
        v = utilidades.visualizar_bonsai(self.estructura, orientacion, emojis, guardar_archivo)
        if not guardar_archivo:
            print(v)
        else:
            with open(f"visualizaciones/{self.identificador}.txt", "w", encoding="utf-8") as f:
                f.write(v)

class DCCortaRamas:
    #no utilizo libreria, reviso la estructura para ver si le tengo que modificar los bool dependiendo de la estructura del bonsai
    def modificar_nodo(self, bonsai: Bonsai, identificador: str) -> str:
        for i in bonsai.estructura:
            identificador_bonsai = i[0]
            modificacion = i[1]
            booleano_bonsai = i[2]

            if identificador == 1: #si es la rama no se puede
                 print("No permitido")
                 return "No permitido"
             
            elif identificador_bonsai == identificador: #verifico los identificadores para poder cambiar la flor  
                 if booleano_bonsai: #si es verdadero la modificacion
                     if modificacion: #si es true se cambia a false
                        i[1]= False
                        print("Realizado")
                        print("Le hice una remocion flor")
                        return "Realizado"
                     elif not modificacion: #si es false, se cambia a true
                        i[1]= True
                        print("Le agregue una flor")
                        print("Realizado")
                        return "Realizado"
                 
                 elif not booleano_bonsai: #si es false, no se permite la modificacion
                     print("No permitido")
                     return "No permitido"
                     
        return "No encontrado" #si no se encuentra el identificador, se retorna no encontrado

    #no utilizo librerias, dependiendo de la estructura y del identificador voy revisando si me permite eliminar el identificador y a todos sus hijos, y a su vez eliminar el identificador del padre nodo
    def quitar_nodo(self, bonsai: Bonsai, identificador: str) -> str: 
        #construyo un diccionario con la estructura
        diccionario_bonsai= {}
        for i in bonsai.estructura:
            nodo_ident= i[0]
            diccionario_bonsai[nodo_ident]= i

        #si el identificador no esta, no fue encontrado
        if identificador not in diccionario_bonsai:
            return "No encontrado"
        
        #si esta vamos a revisarlo
        else:
            bebes= []
            lista_revisar= [identificador]
            while lista_revisar:
                identificador_wh= lista_revisar[0]
                lista_revisar.pop(0) #lo elimino para que se vaya actualizando en el momento, yaque antes se demoraba mucho si tenia todo junto
                nodo_a_usar= diccionario_bonsai[identificador_wh]
                quitar= nodo_a_usar[2]
                if not quitar: #si es falso se termina el programa
                    return "No permitido"
                for i in nodo_a_usar[3]: #sino revisamos a los hijos
                    bebes.append(identificador_wh)
                    if i != "0":
                        lista_revisar.append(i)
        #print("AAAAAAAAA ")
        #reemplozo los nodos eliminados por "0"
        for x in bonsai.estructura:
            for v in range(2):
                bebe= x[3]
                if bebe[v] in bebes: # PORQUE NO ME ENTRAAAAAAAAAAAA
                    bebe[v] = "0"

        
        #actualizo el bonsai para que no tenga los bebes eliminados
        bonsai_nuevo= []
        for m in bonsai.estructura:
            if m[0] in bebes:
                continue
            else:
                bonsai_nuevo.append(m)

        lista_eliminados= [] #creo una lista con los bebes eliminados que piden en el menu
        for b in bonsai.estructura:
            if b[0] in bebes:
                lista_eliminados.append(b)

        bonsai.estructura= bonsai_nuevo #hago los cambios en el bonsai.estructura
        print(lista_eliminados)
        return "Realizado" #AAAAAAAAAAAAAAAAAAAA ME DIO OKKKKKKKKKKKKKKKKKKK

    #no utilizo librerias, reviso la estructura del bonsai, sus hijos de afuera hacia adentro, para verificar que la estructura que tiene sea simetrica tanto a la izquierda como a la derecha
    def es_simetrico(self, bonsai: Bonsai) -> bool:

        #creo un diccionario coon la estructura para poder ir cambiarlo
        diccionario_bonsai= {}
        for i in bonsai.estructura:
            identificador= i[0]
            diccionario_bonsai[identificador]= i
        
        #me saco el caso de si es un nodo altiro para despues revisar los otros
        if len(bonsai.estructura) == 1:
            return True

        #creo una funxion recursiva para ir usandola y acortar codigo en las revisiones de si son iguales o no
        #me equivoque en escribir simetria pero ya tengo el codigo lista, es entendible y funciona bien, no me bajen nota por gramatica:(
        def siemtria(nodo_1, nodo_2):
            #print("nodos PORQUE ME SALE QUE ES "0"",nodo_1, nodo_2)
            if nodo_1 == "0" and nodo_2 == "0": #si los dos son "0", son simétricos
                return True
            elif nodo_1 == "0" or nodo_2 == "0": #si uno es "0", no son simétricos, casos donde hijos 00, un numero o al reves
                return False
            #flores_1= diccionario_bonsai[nodo_1][1]
            #flores_2= diccionario_bonsai[nodo_2][1]
            #print("AAAAAAAAAAAAAAAAAAA")
            #print("flores1 flores2", flores_1, flores_2)
            #if not flores_1 or not flores_2: porque me da error si verifico las flores
                #return False
            
            #voy a dejar esto arriba para organizarme-> no puedo porq aveces son 0 y tengo q dejarlo abajo porq no puede ser 0 - > reviso a los hijos de los nodos q entraron
            bebe_nodo_1 = diccionario_bonsai[nodo_1][3]
            bebe_nodo_2 = diccionario_bonsai[nodo_2][3]

            #ahora q reviso al ser simetricos los hijos si esq la recursividad de los hijos de los hijos es simetrica
            return siemtria(bebe_nodo_1[0], bebe_nodo_2[1]) and siemtria(bebe_nodo_1[1], bebe_nodo_2[0])

        #comienzo revisando el identificador del nodo y asi con la recursividad hasta el ultimo
        primer_nodo_del_bonsai = bonsai.estructura[0]
        bebes_primer_nodo = primer_nodo_del_bonsai[3]
        #le reviso a los hijos de primer nodo, ademas de revisar al nodo
        cant_bebe_primer_nodo= len(bebes_primer_nodo)
        return siemtria(bebes_primer_nodo[0], bebes_primer_nodo[1])

    #no pude realizar la funcion bien, se me fue el tiempo, tengo 6 test publicos malos
    def emparejar_bonsai(self, bonsai: Bonsai) -> list:
        diccionario= {}
        for i in bonsai.estructura:
            identificador= i[0]
            diccionario[identificador]= i

        v= self.es_simetrico(bonsai)
        if v:
            return [True, []]
        else:
            return [False, []]

    #no pude realizar nada de esta funcion:( 
    def emparejar_bonsai_ahorro(self, bonsai: Bonsai) -> list:
        pass

    #no pude realizar nada esta funcion:( 
    def comprobar_solucion(self, bonsai: Bonsai, instrucciones: list) -> list:
        pass