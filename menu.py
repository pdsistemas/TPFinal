#! /usr/bin/env python3

from datetime import datetime
from datetime import date
format = "%d %m %Y"
import sys
from Listaclientes import ListaClientes
from Listatrabajo import TrabajosLista
from trabajo import Trabajo

class Menu:
    "Muestra ocpiones"
    def __init__(self):
        self.lista_c = ListaClientes()
        self.lista_t = TrabajosLista()
        self.opciones = {
                 "1": self.mostrar_clientes,
                 "2": self.nuevo_clientes,
                 "3": self.buscar_cliente,
                 "4": self.borrar_cliente,
                 "5": self.modificar_datos_particulares,
                 "6": self.cargar_nuevo_trabajo,
                 "7": self.mostrar_trabajos,
                 "0": self.salir
        }

    def mostrar_menu(self):
        print("""
        Menú del sistema: 
        1. Mostrar todos los clientes
        2. Ingrese un nuevo cliente
        3. Buscar un cliente por su ID
        4. Borrar un cliente
        5. Modificar clientes particulares
        6. Cargar nuevo trabajo
        7. Mostrar todos los trabajos
        0. Salir
        """)

    def ejecutar (self):
        "Mostrar y responder opciones"
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")
            print("========================================")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opcion válida")

    def mostrar_clientes(self, lista = None):
        if lista == None:
            lista = self.lista_c.lista_Clientes
        for cliente in lista:
            print(cliente)
            print("========================================")

    def mostrar_trabajos(self, listat = None):
        if listat == None:
            listat = self.lista_t.lista_trabajos
        for trabajo in listat:
            print(trabajo)
            print("========================================")


    def nuevo_clientes(self):
        tipo = "N"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de cliente: C: Corporativo / P: Particular:")
        nombre = input("Ingrese el nombre: ")
        if tipo in ("C", "c"):
            contacto = input("Ingrese el nombre del contacto: ")
            telcon = input("Ingrese el teléfono del contacto: ")
        else:
            apellido = input("Ingrese el apellido: ")
        tel = input("Ingrese el telefono: ")
        mail = input("Ingrese el mail: ")
        if tipo in ("C", "c"):
            c = self.lista_c.nuevo_cliente_corporativo(nombre, contacto, telcon,tel, mail)
        else:
            c = self.lista_c.nuevo_cliente_particular(nombre, apellido,tel, mail)

        if c is None:
            print("Error en la carga del nuevo cliente")
        else:
            print("========================================")
            print(c)
            print("========================================")
            print("Carga exitosa")

    def buscar_cliente(self):
        cne = 0
        lista = self.lista_c.lista_Clientes
        idc = int(input("ingrese el ID del cliente a buscar: "))
        for I in lista:
            if I.id_cliente == idc:
                print("========================================")
                print(I)
                cne = 1
        if cne < 1:
            print("Cliente no encontrado")


    def borrar_cliente(self):
        id_cliente = int(input("ingrese el ID del cliente a borrar: "))
        self.lista_c.eliminar_cliente(id_cliente)
        c = self.lista_c.eliminar_cliente(id_cliente)
        self.lista_c = ListaClientes()
        if c == None:
            print("Error al borrar el cliente")
        else:
            print("Cliente borrado con éxito")

    def modificar_datos_particulares(self):
        lista = self.lista_c.lista_Clientes
        id_cliente = int(input("ingrese el ID del cliente a modificar: "))
        for I in lista:
            if I.id_cliente == id_cliente:
                print("Los datos actuales del cliente son: ")
                print("========================================")
                print(I)
                print("========================================")
                print("Para no modificar algún dato particular, dejar el campo vacío")
                nombre = input("Ingrese el nombre: ")
                if nombre == '':
                    for I in lista:
                        if I.id_cliente == id_cliente:
                            nombre = I.nombre
                apellido = input("Ingrese el apellido: ")
                if apellido == '':
                    for I in lista:
                        if I.id_cliente == id_cliente:
                            apellido = I.apellido
                telefono = input("Ingrese el telefono: ")
                if telefono == '':
                    for I in lista:
                        if I.id_cliente == id_cliente:
                            telefono = I.telefono
                mail = input("Ingrese el mail: ")
                if mail == '':
                    for I in lista:
                        if I.id_cliente == id_cliente:
                            mail = I.mail
                c = self.lista_c.Modificar_datos_particulares(nombre, apellido, telefono, mail, id_cliente)
                if c == None:
                    print("Error al modificar el cliente")
                else:
                    print("Cliente modificado con éxito")
            else:
                print("El cliente solicitado no existe")

    def cargar_nuevo_trabajo(self):
        lista = self.lista_c.lista_Clientes
        for cliente in lista:
            print(cliente)
            print("========================================")
        idc = int(input("Ingrese el id del cliente: "))
        cne = 0
        for I in lista:
            if I.id_cliente == idc:
                print("========================================")
                print(I)
                cliente = I
                cne = 1
        if cne < 1:
            print("Cliente no encontrado")
        fecha_ingreso = datetime.today()
        fecha_entrega_propuesta = input("Ingrese la fecha de entrega propuesta (aaaa/mm/dd): ")
        descripcion =  input("Ingrese una descripción del trabajo: ")
        t = self.lista_t.nuevo_trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, descripcion)
        if t == None:
            print("Error al cargar trabajo")
            print (t)
        else:
            print("Trabajo cargado exitosamente")
            print(t)









    def salir(self):
        print("Gracias por utilizar el sistema")
        sys.exit(0)

if __name__ == "__main__":
    m = Menu()
    m.ejecutar()