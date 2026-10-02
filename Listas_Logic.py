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

    def Elimina_Inicio(self):
        # Este algoritmo permite eliminar el primer elemento de una lista simplemente ligada.
        # P es el apuntador al primer elemento de la lista. Q es una variable de tipo apuntador,
        # INFO y LIGA son los campos de los nodos de la lista.
        Q = self.P
        # Si la lista tuviera s[olo un elemento entonces a P se le asignaria NULO , que es el valor
        # de Q.liga En caso contrario, queda con la direccion del siguiente elemento.
        P = Q.liga

    def Elimina_Ultimo(self):
        # Este algoritmo elimina el ultimo nodo de la lista simplemente ligada
        Q = self.P
        if P.liga == None: # Se verifica si la lista tiene solo un nodo
            P = None
        else:
            while Q.liga is not None:
                T = Q
                Q = Q.liga
        T = None

    def Elimina_X(self):
        # Este algoritmo permite eliminar un nodo con informacion X d euna lista simplemente ligada.
        Q = self.P
        Band = 1
        while Q.info != X and Band == 1:
            if Q.liga is not None:
                T = Q
                Q = Q.liga
            else:
                Band = 0
        if Band == 0:
            print (f"El elemento con informacion: {X}(X), no se encuentra en la lista.")
        else:
            if P == Q:
                P = Q.liga
            else:
                T.liga = Q.liga

    def Elimina_antes_X(self):
        # Eliminar un nodo anterior al nodo con informacion X en una lista simplemente ligada
        if self.P.info == X:
            print(f"No existe un nodo que preceda al que contiene a {X} (X)")
        else:
            Q = self.P
            T = self.P
            Band = 1
            while Q.info != X and Band ==1:
                if Q.liga is not None:
                    R = T
                    T = Q
                    Q = Q.liga
                else:
                    Band = 0
            if Band == 0:
                print ("El elemento no se encuentra en la lista.")
            else:
                if self.P.liga == Q: # El elemento a eliminar es el primero
                    self.P = Q
                else:
                    R.liga = Q
    def Eliminar_despues_X(self):
        print("")
    # BUSQUEDA EN LISTAS SIMPLEMENTE LIGADAS
    def Busqueda_Desordenada(self, X):
        # Buscar elemento con la informacion X en una lista simplemente ligada que se encuentra desordenada.
        Q = self.P
        while Q is not None and Q.info != X:
            Q = Q.liga
        if Q is None:
            print ("El elemento no se encuentra en la lista.")
        else:
            print ("El elemento sí se encuentra en la lista.")

    def Busqueda_Ordenada(self, X):
        # Buscar elemento con la informacion X en una lista simplemente ligada que se encuentra ORDENADA DE FORMA ASCENDENTE.
        Q = self.P
        while Q is not None and Q.info < X:
            Q = Q.liga
        if Q is None:
            print ("El elemento no se encuentra en la lista.")
        else:
            print ("El elemento sí se encuentra en la lista.")

    # LOS ALGORITMOS DE BUSQUEDA, INSERCION Y ELIMINACION se pueden implementar de  FORMA RECURSIVA.
    def Busqueda_Recursivo(self, X):
        # De manera recursiva en una lista simplemente ligada q se encuentra DESORDENADA.
        if self.P is not None:
            if self.P.info == X:
                print ("El elemento se encuentra en la lista.")
            else:
                self.Busqueda_Recursivo(X)
        else:
            print("El elemento no se encuentra en la lista.")
