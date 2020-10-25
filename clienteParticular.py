#! /usr/bin/env python3
from cliente import Cliente

class ClienteParticular(Cliente):
    '''Representa un cliente particular'''
    def __init__(self, nombre, apellido, telefono, mail, id_cliente = None):
        self.nombre = nombre
        self.apellido = apellido
        super().__init__(telefono, mail, id_cliente)

    def __str__(self):
        cadena = f"ID: {self.id_cliente}\nNombre: {self.nombre}\nApellido: {self.apellido}\nTipo: Cliente Particular\n"
        cadena+= f"Tel: {self.telefono}\n"
        cadena+= f"Mail: {self.mail}"
        return cadena