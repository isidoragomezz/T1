import utilidades # type: ignore

class Bonsai:
    def __init__(
        self,
        identificador: str,
        costo_corte: int,
        costo_flor: int,
        estructura: list
    ) -> None:
        self.identificador = identificador
        self.costo_corte = costo_corte
        self.costo_flor = costo_flor
        self.estructura = estructura

    def cargar_bonsai_de_archivo(self, carpeta: str, archivo: str) -> None:
        self.estructura= []
        with open (f"data/{carpeta}/{archivo}", "r", encoding= "utf-8") as f:
            for i in f:
                identificador, cosa_1, cosa_2, lista= i.strip().split(",")
                if cosa_1 == "T":
                    cosa_1= True
                else:
                    cosa_1= False
                if cosa_2 == "T":
                    cosa_2= True
                else:
                    cosa_2= False
                lista= lista.split(";")
                estructura= [identificador,cosa_1, cosa_2, lista]
                self.estructura.append(estructura)

    def visualizar_bonsai(self, orientacion: str, emojis: bool, guardar_archivo: bool) -> None:
        if guardar_archivo == False:
            v= utilidades.visualizar_bonsai(self.estructura, orientacion, emojis, guardar_archivo)
            print(v)
        elif guardar_archivo == True :
            v= utilidades.visualizar_bonsai(self.estructura, orientacion, emojis, guardar_archivo)
            with open (f"visualizaciones/{self.identificador}.txt", "w", encoding= "utf-8") as f:
                f.write(v)

class DCCortaRamas:
    def modificar_nodo(self, bonsai: Bonsai, identificador: str) -> str:
        for i in bonsai.estructura:
            identificador_bonsai= i[0]
            modificacion= i[1]
            booleano_bonsai= i[2]

            if identificador == 1: #si es la rama no se puede
                print("No permitido")
                return "No permitido"
            
            elif identificador_bonsai == identificador: #verifico los identificadores para poder cambiar la flor  
                if booleano_bonsai: #si es verdadero la modificacion
                    if modificacion: #si es true se cambia a false
                        i[1]= False
                        print("Realizado")
                        return "Realizado"
                    elif not modificacion: #si es false, se cambia a true
                        i[1]= True
                        print("Realizado")
                        return "Realizado"
                
                elif not booleano_bonsai: #si es false, no se permite la modificacion
                    print("No permitido")
                    return "No permitido"
                    
        return "No encontrado" #si no se encuentra el identificador, se retorna no encontrado
        
    def quitar_nodo(self, bonsai: Bonsai, identificador: str) -> str:
        cont= 0
        for i in bonsai.estructura:
            identificador_bonsai= i[0]
            booleano_bonsai= i[2]
            bebes_nodos= i[3]
            print(i, identificador)

            if identificador == "1": #si es 1 no se puede
                print("No permitido")
                return "No permitido"
    
            if identificador_bonsai == identificador: #si encontraba el identificador
                if booleano_bonsai: #si se permite edicion
                    del bonsai.estructura[cont] #elimino la lista 
                    cont-= 1
                    for v in bebes_nodos:
                         if v != "0":
                            v= int(v)
                            del bonsai.estructura[v-1]
                            identificador_padre, bool_no, bool_si, bebes_padres= bonsai.estructura[cont-1]
                            cont_2= 0
                            for i in bebes_padres:
                                if i == str(cont):
                                    bebes_padres[cont_2]= "0"
                                cont_2+= 1
                            print("Realizado")
                            return "Realizado"
                elif not booleano_bonsai:
                    print("No permitido")
                    return "No permitido"

        return "No encontrado"

    def es_simetrico(self, bonsai: Bonsai) -> bool:
        for i in bonsai.estructura:
            if len(bonsai.estructura) == 1:
                return True
            


    def emparejar_bonsai(self, bonsai: Bonsai) -> list:
        pass

    def emparejar_bonsai_ahorro(self, bonsai: Bonsai) -> list:
        pass

    def comprobar_solucion(self, bonsai: Bonsai, instrucciones: list) -> list:
        pass
