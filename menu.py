#! /usr/bin/env python3

import datetime
from datetime import datetime
from datetime import date
import sys
from Listaclientes import ListaClientes
from Listatrabajo import TrabajosLista
from repositorioTrabajos import RepositorioTrabajos

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
                 "5": self.modificar_datos_clientes,
                 "6": self.cargar_nuevo_trabajo,
                 "7": self.mostrar_trabajos,
                 "8": self.establecer_entrega,
                 "9": self.establecer_final,
                 "10": self.buscar_trabajo,
                 "11": self.modificar_datos_trabajos,
                 "12": self.eliminar_trabajo,
                 "13": self.proximos_trabajos,
                 "14": self.buscar_trabajos_por_cliente,
                 "0": self.salir
        }

    def mostrar_menu(self):
        print("""
        Menú del sistema:
                        
                                SISTEMA DE GESTIÓN DE TRABAJOS
        
                MENÚ CLIENTES                                           MENÚ TRABAJOS 
                                         
        1. Mostrar todos los clientes                            6. Cargar nuevo trabajo
        2. Ingrese un nuevo cliente                              7. Mostrar todos los trabajos
        3. Buscar un cliente por su ID                           8. Establecer entrega
        4. Borrar un cliente                                     9. Establecer finalizacion de trabajo
        5. Modificar datos de un cliente                         10. Buscar un trabajo por ID
                                                                 11. Modificar datos de trabajo
                                                                 12. Eliminar trabajo
                                                                 13. Motrar proximos trabajos a entregarse
                                                                 14. Buscar trabajos de un cliente
                
        
                                Ingrese '0' para salir del sistema
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

    def buscar_trabajos_por_cliente(self):
        while True:
            try:
                id_cliente = int(input("Ingrese el ID del cliente: "))
            except ValueError:
                print('Ingresó un dato inválido')
                continue
            break
        con = 0
        c = self.lista_c.buscar_por_id(id_cliente)
        if c:
            for i in self.lista_t.lista_trabajos:
                if i.cliente.id_cliente == id_cliente:
                        print("========================================")
                        print(i)
                        con = 1
            if con == 0:
                print("\nEl cliente no cuenta \ncon trabajos asignados.")
        else:
            print("Cliente no encontrado")
        print("========================================")
        input("\nPresione cualquier tecla para volver al menú")


    def proximos_trabajos(self):
        global dias
        ptrab = []
        listat = self.lista_t.lista_trabajos
        while True:
            try:
                dias = int(input("Ingrese la cantidad de días para establecer\nuna lista de proximos trabajos a entregar: "))
            except ValueError:
                print('Ingresó un dato inválido')
                continue
            break
        alertas = self.lista_t.alerta_trabajos(dias)
        for i in listat:
            for a in alertas:
                if a == i.fecha_entrega_propuesta and i.retirado == False:
                    ptrab.append(i)
        if ptrab:
            print("\n\nLos trabajos a entregar en los proximos", dias, "días son:")
            for t in ptrab:
                print("========================================")
                print(t)
        else:
            print("\nNo hay trabajos a entregar en los próximos", dias, "días")

        input("\nPresione cualquier tecla para volver al menú")





    def mostrar_clientes(self):
        if self.lista_c.lista_Clientes:
            for cliente in self.lista_c.lista_Clientes:
                print(cliente)
                print("========================================")
        else:
            print("No hay clientes cargados")
        input("\nPresione cualquier tecla para volver al menú")

    def mostrar_trabajos(self):
        if self.lista_t.lista_trabajos:
            for trabajo in self.lista_t.lista_trabajos:
                print(trabajo)
                print("========================================")
        else:
            print("No hay trabajos cargados")
        input("\nPresione cualquier tecla para volver al menú")

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
            print("             Carga exitosa              ")
            print("========================================")
        input("\nPresione cualquier tecla para volver al menú")


    def buscar_cliente(self):
        while True:
            try:
                idc = int(input("ingrese el ID del cliente a buscar: "))
            except ValueError:
                print('Ingresó un dato inválido')
                continue
            break
        c = self.lista_c.buscar_por_id(idc)
        if c == None:
            print("ID de cliente no encontrado")
        else:
            print("========================================")
            print(c)
            print("========================================")
        input("\nPresione cualquier tecla para volver al menú")



    def borrar_cliente(self):
        while True:
            try:
                id_cliente = int(input("ingrese el ID del cliente a borrar: "))
            except ValueError:
                print('Ingresó un dato inválido')
                continue
            break
        c = self.lista_c.buscar_por_id(id_cliente)
        if c == None:
            print("ID de cliente no encontrado")
        else:
            con = 0
            if self.lista_t.lista_trabajos:
                for i in self.lista_t.lista_trabajos:
                    if i.cliente.id_cliente == id_cliente:
                        if con == 0:
                            print("\nEl cliente aún cuenta con los siguientes trabajos pendientes, no se puede eliminar el cliente.\n")
                        print("========================================")
                        print(i)
                        con = 1
            if con == 0:
                print("========================================")
                print(c)
                print("========================================")
                seg = input("\nEsta seguro que quiere eliminar el cliente? (S/N): ")
                if seg == 'S' or seg == 's':
                    self.lista_c.eliminar_cliente(id_cliente)
                    c = self.lista_c.eliminar_cliente(id_cliente)
                    self.lista_c = ListaClientes()
                    if c == None:
                        print("Error al borrar el cliente")
                    else:
                        print("Cliente borrado con éxito")
                else:
                    print("\nOperación cancelada por el usuario")
        input("\nPresione cualquier tecla para volver al menú")


    def modificar_datos_clientes(self):
        lista = self.lista_c.lista_Clientes
        while True:
            try:
                id_cliente = int(input("Ingrese el ID del cliente: "))
            except ValueError:
                print('Ingresó un dato inválido')
                continue
            break
        c = self.lista_c.buscar_por_id(id_cliente)
        if c == None:
            print("\nCliente no encontrado")
        else:
            result = self.lista_c.modificar_clientes(id_cliente)
            if result == 1:
                print("El cliente es corporativo: ")
                print(c)
                print("========================================")
                print("\nPara NO modificar algún dato en particular, dejar el campo vacío\n")
                nombre_empresa = input("Ingrese el nombre de empresa: ")
                if nombre_empresa == '':
                    for I in lista:
                        if I.id_cliente == id_cliente:
                            nombre_empresa = I.nombre_empresa

                nombre_contacto = input("Ingrese el nombre del contacto: ")
                if nombre_contacto == '':
                    for I in lista:
                        if I.id_cliente == id_cliente:
                            nombre_contacto = I.nombre_contacto

                telefono_contacto = input("Ingrese el teléfono del contacto: ")
                if telefono_contacto == '':
                    for I in lista:
                        if I.id_cliente == id_cliente:
                            telefono_contacto = I.telefono_contacto

                telefono = input("Ingrese el teléfono: ")
                if telefono == '':
                    for I in lista:
                        if I.id_cliente == id_cliente:
                            telefono = I.telefono

                mail = input("Ingrese el mail: ")
                if mail == '':
                    for I in lista:
                        if I.id_cliente == id_cliente:
                            mail = I.mail
                c = self.lista_c.Modificar_datos_corporativos(nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail, id_cliente)
                if c == None:
                    print("Error al modificar el cliente")
                else:
                    print("\nCliente modificado con éxito")
            if result == 0:
                print("El cliente es particular:")
                print(c)
                print("========================================")
                print("\nPara NO modificar algún dato particular, dejar el campo vacío\n")
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
                    print("\nCliente modificado con éxito")
        input("\nPresione cualquier tecla para volver al menú")




    def modificar_datos_particulares(self):
        lista = self.lista_c.lista_Clientes
        while True:
            try:
                id_cliente = int(input("ingrese el ID del cliente a modificar: "))
            except ValueError:
                print('Ingresó un dato inválido')
                continue
            break
        c = self.lista_c.buscar_por_id(id_cliente)
        if c == None:
            print("ID cliente no encontrado")
        else:
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
        input("\nPresione cualquier tecla para volver al menú")

    def cargar_nuevo_trabajo(self):
        lista = self.lista_c.lista_Clientes
        if lista:
            for cliente in lista:
                print(cliente)
                print("========================================")
            while True:
                try:
                    idc = int(input("Ingrese el id del cliente: "))
                except ValueError:
                    print('Ingresó un dato inválido')
                    continue
                break
            cne = 0
            for I in lista:
                if I.id_cliente == idc:
                    print("========================================")
                    cliente = I
                    cne = 1
            if cne < 1:
                print("Cliente no encontrado")
            else:
                print(cliente)
                fecha_ingreso = datetime.today()
                fecha_ingreso = date(fecha_ingreso.year, fecha_ingreso.month, fecha_ingreso.day)
                print("Ingrese la fecha de entrega propuesta: ")
                while True:
                    try:
                        dia = int(input("Día (1-31): "))
                    except ValueError:
                        print('Ingresó un dato inválido')
                        continue
                    break
                while True:
                    try:
                        mes = int(input("Mes (1-12): "))
                    except ValueError:
                        print('Ingresó un dato inválido')
                        continue
                    break
                while True:
                    try:
                        anio = int(input("Año: "))
                    except ValueError:
                        print('Ingresó un dato inválido')
                        continue
                    break
                fecha_entrega_propuesta = date(anio, mes, dia)
                descripcion = input("Ingrese una descripción del trabajo: ")
                t = self.lista_t.nuevo_trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, descripcion)
                if t == None:
                    print("Error al cargar trabajo")
                    print(t)
                else:
                    print("Trabajo cargado exitosamente")
                    print(t)
        else:
            print("No hay clientes dados de alta, primero de el alta del cliente")
        input("\nPresione cualquier tecla para volver al menú")


    def establecer_entrega(self):
        while True:
            try:
                id_trabajo = int(input("Ingrese el ID del trabajo que quiere establecer como 'entregado': "))
            except ValueError:
                print('Ingresó un dato inválido')
                continue
            break
        t = self.lista_t.buscar_por_id(id_trabajo)
        if t == None:
            print("ID de trabajo no encontrado")
        else:
            s = input("SI ESTA SEGURO de establecer retirado ingrese (S): ")
            if s == 'S' or s == 's':
                print("El estado era: ", t.retirado)
                retirado = True
                et = self.lista_t.establecer_entrega(id_trabajo, retirado)
                if et == None:
                    print("Error al establecer entrega")
                else:
                    t = self.lista_t.buscar_por_id(id_trabajo)
                    print ("El estado ahora es: ", t.retirado)
            else:
                print("Operación cancelada por el usuario")
        input("\nPresione cualquier tecla para volver al menú")
        self.lista_t = TrabajosLista()



    def establecer_final(self):
        while True:
            try:
                id_trabajo = int(input("Ingrese el ID del trabajo que quiere establecer como 'finalizado': "))
            except ValueError:
                print('Ingresó un dato inválido')
                continue
            break
        t = self.lista_t.buscar_por_id(id_trabajo)
        if t == None:
            print("ID de trabajo no encontrado")
        else:
            s = input("SI ESTA SEGURO de establecer como 'finalizado' ingrese (S): ")
            if s == 'S' or s == 's':
                ef = self.lista_t.establecer_final(id_trabajo)
                if ef == None:
                    print("Error al establecer finalización de trabajo")
                else:
                    print("La fecha real de finalización ha sido establecida en: ", self.lista_t.buscar_por_id(id_trabajo).fecha_entrega_real)
            else:
                print("Operación cancelada por el usuario")
        self.lista_t = TrabajosLista()
        input("\nPresione cualquier tecla para volver al menú")

    def buscar_trabajo(self):
        while True:
            try:
                id_trabajo = int(input("Ingrese el ID del trabajo: "))
            except ValueError:
                print('Ingresó un dato inválido')
                continue
            break
        trabajo = self.lista_t.buscar_por_id(id_trabajo)
        if trabajo == None:
            print("ID no encontrado")
        else:
            print(trabajo)
        input("\nPresione cualquier tecla para volver al menú")

    def modificar_datos_trabajos(self):
        while True:
            try:
                id_trabajo = int(input("ingrese el ID del trabajo a modificar: "))
            except ValueError:
                print('Ingresó un dato inválido')
                continue
            break
        trabajo = self.lista_t.buscar_por_id(id_trabajo)
        if trabajo == None:
            print("ID no encontrado")
        else:
            print("Los datos actuales del cliente son: ")
            print("========================================")
            print(trabajo)
            print("========================================")
            conf = input("Desea modificar la fecha de ingreso? S/N: ")
            if conf == 'S' or conf == 's':
               print("Ingrese la nueva fecha de ingreso a establecer: ")
               while True:
                   try:
                       dia = int(input("Día: "))
                   except ValueError:
                       print('Ingresó un dato inválido')
                       continue
                   break
               while True:
                   try:
                       mes = int(input("Mes: "))
                   except ValueError:
                       print('Ingresó un dato inválido')
                       continue
                   break
               while True:
                   try:
                       anio = int(input("Año: "))
                   except ValueError:
                       print('Ingresó un dato inválido')
                       continue
                   break
               fecha_ingreso = date(anio, mes, dia)
            else:
               fecha_ingreso = trabajo.fecha_ingreso
            conf = input("Desea modificar la fecha de entrega propuesta? S/N: ")
            if conf == 'S' or conf == 's':
                print("Ingrese la nueva fecha de entrega propuesta: ")
                while True:
                    try:
                        dia = int(input("Día: "))
                    except ValueError:
                        print('Ingresó un dato inválido')
                        continue
                    break
                while True:
                    try:
                        mes = int(input("Mes: "))
                    except ValueError:
                        print('Ingresó un dato inválido')
                        continue
                    break
                while True:
                    try:
                        anio = int(input("Año: "))
                    except ValueError:
                        print('Ingresó un dato inválido')
                        continue
                    break
                fecha_entrega_propuesta = date(anio, mes, dia)
            else:
                fecha_entrega_propuesta = trabajo.fecha_entrega_propuesta
            conf = input("Desea modificar la fecha de entrega real? S/N: ")
            if conf == 'S' or conf == 's':
                print("Ingrese la nueva fecha de entrega real: ")
                while True:
                    try:
                        dia = int(input("Día: "))
                    except ValueError:
                        print('Ingresó un dato inválido')
                        continue
                    break
                while True:
                    try:
                        mes = int(input("Mes: "))
                    except ValueError:
                        print('Ingresó un dato inválido')
                        continue
                    break
                while True:
                    try:
                        anio = int(input("Año: "))
                    except ValueError:
                        print('Ingresó un dato inválido')
                        continue
                    break
                fecha_entrega_real = date(anio, mes, dia)
            else:
                fecha_entrega_real = trabajo.fecha_entrega_real

            descripcion = input("Ingrese la nueva descripción o deje vacío para mantener datos: ")
            if descripcion == '':
                descripcion = trabajo.descripcion
            ret = input("Ingrese si el trabajo ha si retirado' (Retirado: Ingrese 'True' - No retirado: Ingrese 'False'")
            if ret == 'True' or ret == 'true':
                retirado = True
            else:
                if ret == 'False' or ret == 'false':
                    retirado = False
                else:
                    print("\nADVERTENCIA: No se ingresó opción válida, no se modificó el estado de retiro\n")
                    retirado = trabajo.retirado
            c = self.lista_t.modificar_datos_trabajos(id_trabajo, fecha_ingreso, fecha_entrega_propuesta, fecha_entrega_real, descripcion, retirado)
            if c == None:
                print("Error al modificar el trabajo")
            else:
                print("============================")
                print("Trabajo modificado con éxito")
                print("============================")
        self.lista_t = TrabajosLista()
        input("\nPresione cualquier tecla para volver al menú")

    def eliminar_trabajo(self):
        while True:
            try:
                id_trabajo = int(input("Ingrese el ID del trabajo que desea eliminar: "))
            except ValueError:
                print('Ingresó un dato inválido')
                continue
            break
        trabajo = self.lista_t.buscar_por_id(id_trabajo)
        if trabajo == None:
            print("ID del trabajo no encontrado")
        else:
            print(trabajo)
            elim = input("Seguro desea eliminar este trabajo? (S/N): ")
            if elim == 'S' or elim == 's':
                et = self.lista_t.eliminar_trabajo(id_trabajo)
                if et == None:
                   print("Error al eliminar el trabajo")
                else:
                   print("El trabajo ha sido eliminado")
            else:
                print("Operación cancelada por el usuario")
            self.lista_t = TrabajosLista()
            input("\nPresione cualquier tecla para volver al menú")










    def salir(self):
        print("Gracias por utilizar el sistema")
        sys.exit(0)

if __name__ == "__main__":
    m = Menu()
    m.ejecutar()