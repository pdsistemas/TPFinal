#! /usr/bin/env python3


from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo
from repositorioClientes import RepositorioClientes


class ListaClientes:
    def __init__(self):
        self.rc = RepositorioClientes()
        self.lista_Clientes = self.rc.get_all()


    def modificar_clientes(self, id_cliente):
        #Recibe un ID y devuelve un 1 si es un cliente corporativo y 0 si es cliente particular.
        lc = self.rc.get_all_corporativos()
        lp = self.rc.get_all_particulares()
        for l in lc:
            if l.id_cliente == id_cliente:
                return (1)
        for l in lp:
            if l.id_cliente == id_cliente:
                return (0)




    def nuevo_cliente_corporativo(self, nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail):
        c = ClienteCorporativo(nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail)
        c.id_cliente = self.rc.store(c)
        if c.id_cliente == 0:
            return None
        else:
            self.lista_Clientes.append(c)
            return c

    def nuevo_cliente_particular(self, nombre, apellido, telefono, mail):
        c = ClienteParticular(nombre, apellido, telefono, mail)
        c.id_cliente = self.rc.store(c)
        if c.id_cliente == 0:
            return None
        else:
            self.lista_Clientes.append(c)
            return c

    def buscar_por_id(self, id_cliente):
        """Buscar el cliente con el ID dado"""
        for T in self.lista_Clientes:
            if T.id_cliente == int(id_cliente):
                return (T)
        return None

    def eliminar_cliente(self, id_cliente):
        c = self.buscar_por_id(id_cliente)
        if c:
            return self.rc.delete(c)
        return None

    def Modificar_datos_particulares(self, nombre, apellido, telefono ,mail, id_cliente):
        """Modificar o corregir los datos del cliente particular"""
        c = self.buscar_por_id(id_cliente)
        if c:
            c.nombre = nombre
            c.apellido = apellido
            c.telefono = telefono
            c.mail = mail
            return self.rc.update(c)

    def Modificar_datos_corporativos(self, nombre_empresa, nombre_contacto, telefono_contacto, telefono , mail, id_cliente):
        """Modificar o corregir los datos del cliente particular"""
        c = self.buscar_por_id(id_cliente)
        if c:
            c.nombre_empresa = nombre_empresa
            c.nombre_contacto = nombre_contacto
            c.telefono_contacto = telefono_contacto
            c.telefono = telefono
            c.mail = mail
            return self.rc.update(c)
        return None