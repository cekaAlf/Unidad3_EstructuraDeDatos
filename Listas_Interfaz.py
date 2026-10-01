import customtkinter as ctk


class Nodo:
    def __init__(self, dato=None):
        self.info = dato  # Campo INFO
        self.liga = None  # Campo LIGA


class Listas:
    def __init__(self):
        self.P = None  # Apuntador al primer nodo de la lista

    def Inserta_Inicio(self, dato):
        Q = Nodo(dato)
        Q.liga = self.P
        self.P = Q
        return self.P

    def Inserta_Final(self, dato):
        Q = Nodo(dato)
        if self.P is None:
            self.P = Q
            return self.P
        T = self.P
        while T.liga is not None:
            T = T.liga
        T.liga = Q
        return self.P

    def Inserta_antes_X(self, dato, X):
        if self.P is None:
            return False, "La lista está vacía."

        Q = self.P
        Band = 1
        T = None
        while Q.info != X and Band == 1:
            if Q.liga is not None:
                T = Q
                Q = Q.liga
            else:
                Band = 0

        if Band == 1:
            NUEVO = Nodo(dato)
            if self.P == Q:
                NUEVO.liga = self.P
                self.P = NUEVO
            else:
                T.liga = NUEVO
                NUEVO.liga = Q
            return True, f"Nodo '{dato}' insertado antes de '{X}'."
        else:
            return False, f"El nodo '{X}' no se encuentra en la lista."

    def Inserta_despues_X(self, dato, X):
        if self.P is None:
            return False, "La lista está vacía."

        Q = self.P
        Band = 1
        while Q.info != X and Band == 1:
            if Q.liga is not None:
                Q = Q.liga
            else:
                Band = 0

        if Band == 1:
            T = Nodo(dato)
            T.liga = Q.liga
            Q.liga = T
            return True, f"Nodo '{dato}' insertado después de '{X}'."
        else:
            return False, f"El nodo '{X}' no se encuentra en la lista."

    def Recorre_Iterativo(self):
        elementos = []
        Q = self.P
        while Q is not None:
            elementos.append(str(Q.info))
            Q = Q.liga
        return elementos

    def Recorre_Recursivo(self, P, elementos=None):
        if elementos is None:
            elementos = []
        if P is not None:
            elementos.append(str(P.info))
            self.Recorre_Recursivo(P.liga, elementos)
        return elementos


class ListasInterfaz:
    def __init__(self, master_frame):
        self.master = master_frame
        self.lista = Listas()

        # Título principal
        self.lbl_titulo = ctk.CTkLabel(
            master=self.master,
            text="Listas Simplemente Ligadas",
            font=("Courier New", 20, "bold"),
            text_color="#000000",
        )
        self.lbl_titulo.pack(pady=10)

        # Frame para entradas de texto
        self.frame_inputs = ctk.CTkFrame(
            master=self.master, fg_color="transparent"
        )
        self.frame_inputs.pack(pady=10)

        self.lbl_dato = ctk.CTkLabel(
            master=self.frame_inputs, text="Dato:", text_color="#000000"
        )
        self.lbl_dato.grid(row=0, column=0, padx=5, pady=5)
        self.entry_dato = ctk.CTkEntry(master=self.frame_inputs, width=120)
        self.entry_dato.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_ref = ctk.CTkLabel(
            master=self.frame_inputs,
            text="Referencia (X):",
            text_color="#000000",
        )
        self.lbl_ref.grid(row=0, column=2, padx=5, pady=5)
        self.entry_ref = ctk.CTkEntry(master=self.frame_inputs, width=120)
        self.entry_ref.grid(row=0, column=3, padx=5, pady=5)

        # Frame para botones de operación
        self.frame_botones = ctk.CTkFrame(
            master=self.master, fg_color="transparent"
        )
        self.frame_botones.pack(pady=10)

        btn_params = {
            "fg_color": "#000000",
            "hover_color": "#222222",
            "text_color": "#75BBD6",
            "border_color": "#000000",
            "border_width": 1,
            "corner_radius": 15,
            "font": ("Courier New", 12, "bold"),
            "width": 160,
            "height": 35,
        }

        ctk.CTkButton(
            master=self.frame_botones,
            text="Inserta Inicio",
            command=self.btn_inserta_inicio,
            **btn_params,
        ).grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkButton(
            master=self.frame_botones,
            text="Inserta Final",
            command=self.btn_inserta_final,
            **btn_params,
        ).grid(row=0, column=1, padx=5, pady=5)
        ctk.CTkButton(
            master=self.frame_botones,
            text="Inserta antes X",
            command=self.btn_inserta_antes_x,
            **btn_params,
        ).grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkButton(
            master=self.frame_botones,
            text="Inserta después X",
            command=self.btn_inserta_despues_x,
            **btn_params,
        ).grid(row=1, column=1, padx=5, pady=5)
        ctk.CTkButton(
            master=self.frame_botones,
            text="Recorre Iterativo",
            command=self.btn_recorre_iterativo,
            **btn_params,
        ).grid(row=2, column=0, padx=5, pady=5)
        ctk.CTkButton(
            master=self.frame_botones,
            text="Recorre Recursivo",
            command=self.btn_recorre_recursivo,
            **btn_params,
        ).grid(row=2, column=1, padx=5, pady=5)

        # Estado de operaciones
        self.lbl_estado = ctk.CTkLabel(
            master=self.master,
            text="",
            font=("Courier New", 12, "bold"),
            text_color="#EF1313",
        )
        self.lbl_estado.pack(pady=5)

        # Visor gráfico de la lista ligada
        self.lbl_visor_titulo = ctk.CTkLabel(
            master=self.master,
            text="Representación de la Lista:",
            font=("Courier New", 14, "bold"),
            text_color="#000000",
        )
        self.lbl_visor_titulo.pack(pady=(10, 5))

        self.txt_visor = ctk.CTkTextbox(
            master=self.master, width=550, height=80, font=("Courier New", 14)
        )
        self.txt_visor.pack(pady=5)
        self.actualizar_visor()

    def actualizar_visor(self):
        elementos = self.lista.Recorre_Iterativo()
        self.txt_visor.configure(state="normal")
        self.txt_visor.delete("1.0", "end")
        if not elementos:
            self.txt_visor.insert("1.0", "P -> NIL (Lista Vacía)")
        else:
            cadena = "P -> " + " -> ".join(elementos) + " -> NIL"
            self.txt_visor.insert("1.0", cadena)
        self.txt_visor.configure(state="disabled")

    def btn_inserta_inicio(self):
        dato = self.entry_dato.get().strip()
        if dato:
            self.lista.Inserta_Inicio(dato)
            self.lbl_estado.configure(
                text=f"Dato '{dato}' insertado al inicio.", text_color="#00AA00"
            )
            self.entry_dato.delete(0, "end")
            self.actualizar_visor()
        else:
            self.lbl_estado.configure(
                text="Por favor ingresa un dato.", text_color="#EF1313"
            )

    def btn_inserta_final(self):
        dato = self.entry_dato.get().strip()
        if dato:
            self.lista.Inserta_Final(dato)
            self.lbl_estado.configure(
                text=f"Dato '{dato}' insertado al final.", text_color="#00AA00"
            )
            self.entry_dato.delete(0, "end")
            self.actualizar_visor()
        else:
            self.lbl_estado.configure(
                text="Por favor ingresa un dato.", text_color="#EF1313"
            )

    def btn_inserta_antes_x(self):
        dato = self.entry_dato.get().strip()
        X = self.entry_ref.get().strip()
        if dato and X:
            exito, msg = self.lista.Inserta_antes_X(dato, X)
            color = "#00AA00" if exito else "#EF1313"
            self.lbl_estado.configure(text=msg, text_color=color)
            if exito:
                self.entry_dato.delete(0, "end")
                self.actualizar_visor()
        else:
            self.lbl_estado.configure(
                text="Ingresa el dato y la referencia X.", text_color="#EF1313"
            )

    def btn_inserta_despues_x(self):
        dato = self.entry_dato.get().strip()
        X = self.entry_ref.get().strip()
        if dato and X:
            exito, msg = self.lista.Inserta_despues_X(dato, X)
            color = "#00AA00" if exito else "#EF1313"
            self.lbl_estado.configure(text=msg, text_color=color)
            if exito:
                self.entry_dato.delete(0, "end")
                self.actualizar_visor()
        else:
            self.lbl_estado.configure(
                text="Ingresa el dato y la referencia X.", text_color="#EF1313"
            )

    def btn_recorre_iterativo(self):
        elementos = self.lista.Recorre_Iterativo()
        self.lbl_estado.configure(
            text=f"Recorrido Iterativo: {', '.join(elementos)}"
            if elementos
            else "Lista vacía.",
            text_color="#000000",
        )
        self.actualizar_visor()

    def btn_recorre_recursivo(self):
        elementos = self.lista.Recorre_Recursivo(self.lista.P)
        self.lbl_estado.configure(
            text=f"Recorrido Recursivo: {', '.join(elementos)}"
            if elementos
            else "Lista vacía.",
            text_color="#000000",
        )
        self.actualizar_visor()

  # Para el menu
  self.btn_Listas = ctk.CTkButton(
            master=self.frameWidgets,
            text="Listas Ligadas",
            command=self.Pro_Listas,
            **self.parametrosBotones,
        )
        self.btn_Listas.grid(row=2, column=0, padx=20, pady=20)

  def Pro_Listas(self):
        from Unidad3.Listas_Interfaz import ListasInterfaz

        self.limpiarPanel_derecho()
        ListasInterfaz(self.frameWidgets) 
