# Este algoritmo permite crear una lista simplemente ligada, agregando
#cada nuevo nodo al inicio de la misma

#P y Q son variables de tipo puntero. Los campos del nodo son INFO, que
#será del tipo de datos que se quiera almacenar en la lista, y LIGA de tipo apuntador.
#P apunta al inicio de la lista. RES es una variable de tipo entero.
class Nodo():
    def __init__(self, dato = None):
        self.info = dato # Campo de INFO
        self.liga = None #Campo LIGA

class Listas:
    def __init__(self, dato = None):
        self.P = None # P al primer nodo de la lista

    def Crea_Inicio (self):
        # Este algoritmo permite crear una lista simplemente ligada, agregando cada nuevo nodo
        # al inicio de la misma
        # P y Q son variables de tipo puntero. Los campos del nodo son INFO, que sera del tipo
        # de datos que se quiera almacenar en la lista, y LIGA de tipo apuntador. P apunta al
        # inicio de la lista. RES es una variable de tipo entero.
        P = Nodo()
        P.info = input("Ingresa un dato: ")
        P.liga = None
        res = int(input("¿Desea ingresar más números? (si:1/no:0)"))
        while res == 1:
            Q = Nodo()
            Q.info = input("Ingresa un dato: ")
            Q.liga = P
            P=Q
            res = int(input("¿Desea ingresar más números? (si:1/no:0)"))
        return P # Retornan la cabeza de la lista

    def Crea_Final(self):
        # Este algoritmo permite crear una lista simplemente ligada, agregando cada nuevo final de la misma
        # P, Q y T son variables de tipo apuntador. Los campos del nodo son INFO, que será del tipo de datos
        # que se quiera almacenar en la lista, y LIGA de tipo apuntador
        # P apunta al inicio de la lista. RES es una variable de tipo entero.
        P = Nodo()
        P.info = input("Inserta un dato: ")
        P.liga = None
        T = P
        res = int(input("¿Desea ingresar más números? (si:1/no:0)"))
        while res == 1:
            Q = Nodo()
            Q.info = input("Ingresa un dato: ")
            Q.liga = None
            T.liga = Q
            T = Q # T apunta al ultimo nodo
            res = int(input("¿Desea ingresar más números? (si:1/no:0)"))
        return T

    def Inserta_Inicio(self, dato):
        # Este algoritmo inserta al inicio de una lista simplemente ligada. 
        # P es el apuntador al primer nodo de la misma, y DATO es la informacion
        # que se almacenara en el nuevo nodo.
        # Q es una variable de tipo apuntador, INFO y LIGA son los campos de cada nodo
        # de la lista.
        Q = Nodo(dato)
        Q.info = dato
        Q.liga = self.P
        self.P = Q

    def 
