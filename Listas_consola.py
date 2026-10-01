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
        self.P = P
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
        self.P = P
        return self.P

    def Recorre_Iterativo(self):
        Q = self.P
        while Q != None:
            print (Q.info)
            Q = Q.liga # Apunta al siguiente nodo de la lista

    def Recorre_Recursivo(self, P):
        if P != None:
            print (P.info)
            self.Recorre_Recursivo(P.liga)
        

    def Inserta_Inicio(self, dato):
        # Este algoritmo inserta al inicio de una lista simplemente ligada. 
        # P es el apuntador al primer nodo de la misma, y DATO es la informacion
        # que se almacenara en el nuevo nodo.
        # Q es una variable de tipo apuntador, INFO y LIGA son los campos de cada nodo
        # de la lista.
        Q = Nodo(dato)
        Q.liga = self.P
        self.P = Q
        return self.P
        
    def Inserta_Final(self, dato):
        # Inserta un nodo al final de una lista simplemente ligada
        # Esto es cuando la lista ya tiene elementos
        #while T.liga != None:
        #    T = T.liga
        #Q = Nodo(dato)
        #Q.liga = None
        #T.liga = Q
        Q = Nodo(dato)
        #Si esta vacia
        if self.P is None:
            self.P = Q
            return self.P
        # Si la lista ya tiene elementos, recorremos hasta el ultimo nodo
        T = self.P
        while T.liga != None:
            T = T.liga
        # El nuevo nodo se conecta al final
        T.liga = Q
        return self.P

    def Inserta_antes_X(self, dato, X):
        # Este algoritmo unserta un nodo antes de un nodo dado como referencia en una lista
        # simplemente ligada. P es el apuntador al primer nodo de la lista, DATO indica la informacion
        # q se almacenara en el nuevo nodo, y X representa el contenido - informacion - del nodo dado como referencia
        # AL IGUAL Q LOS ANTERIORES HAY QUE VALIDAR QYE LA LISTA NO ESTE VACIA
        if self.P is None:
            print("La lista está vacía. No se puede buscar el nodo de referencia.")
            return
            
        Q = self.P
        Band = 1
        #Se busca X en la lisa
        while Q.info != X and Band == 1:
            if Q.liga != None:
                T = Q
                Q = Q.liga
            else:
                Band = 0
        # sE HACE la insercion
        if  Band == 1:
            NUEVO = Nodo (dato) # Al principio se define X como el valor del contenido, pero en el paso 4 usa X como el puntero del nuevo nodo
            if self.P == Q: # El nodo dado como referencia es el primero
                NUEVO.liga = self.P
                self.P = NUEVO
            else:
                T.liga = NUEVO
                NUEVO.liga = Q
        else:
            print ("El nodo dado como referencia no se encuentra en la lista")

    def Inserta_despues_X(self, dato, X):
        # Este algoritmo inserta un nodo despues de otro dado como referencia en una lista simplemente ligada
        # P es el apuntador al primer nodo de la lista. DATO indica la informaci[on que se almacenara en el nuevo nodo
        # y X representa el contenido -informacion- del nodo dado como referencia
        # Qy P son variables de tipo apuntador. INFO y LIGA son los campos de los nodos de la lista BAND es una variable de tipo entero.
        if self.P is None:
            print("La lista está vacía. No se encuentra el nodo de referencia.")
            return
        Q = self.P
        Band = 1
        # Buscar nodo en lista
        while Q.info != X and Band == 1:
            if Q.liga != None:
                Q = Q.liga
            else:
                Band = 0
        #Insertamos despues de Q
        if Band == 1:
            T = Nodo(dato)
            T.liga = Q.liga
            Q.liga = T
        else:
            print ("El nodo dado como referencia no se encuentra en la lista")

# Para probar unicamente en consola "__name__" quiere decir que se ejecuta desde la terminal
# en caso contrario que se importe por ejemplo entonces no se cumple la condicion y el codigo dentro del bloque se omite,
if __name__=="__main__": 
    lista = Listas()
    while True:
        print("\nMENU LISTA SIMPLEMENTE LIGADA")
        print("1. Crear lista por el Inicio")
        print("2. Crear lista por el Final")
        print("3. Insertar al Inicio")
        print("4. Insertar al Final")
        print("5. Insertar antes de X")
        print("6. Insertar después de X")
        print("7. Recorrer (Iterativo)")
        print("8. Recorrer (Recursivo)")
        print("9. Salir")

        opcion = input("Selcciona una opcion: ")

        if opcion == "1":
            lista.Crea_Inicio()
        elif opcion == "2":
            lista.Crea_Final()
        elif opcion == "3":
            dato = input("Ingresa el dato a insertar al inicio: ")
            lista.Inserta_Inicio(dato)
        elif opcion == "4":
            dato = input("Ingresa el dato a insertar al final: ")
            lista.Inserta_Final(dato)
        elif opcion == "5":
            dato = input("Ingresa el nuevo dato: ")
            X = input("Ingresa el dato de referencia X: ")
            lista.Inserta_antes_X(dato, X)
        elif opcion == "6":
            dato = input("Ingresa el nuevo dato: ")
            X = input("Ingresa el dato de referencia X: ")
            lista.Inserta_despues_X(dato, X)
        elif opcion == "7":
            print("\nElementos de la lista (Iterativo):")
            lista.Recorre_Iterativo()
        elif opcion == "8":
            print("\nElementos de la lista (Recursivo):")
            lista.Recorre_Recursivo(lista.P)
        elif opcion == "9":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
