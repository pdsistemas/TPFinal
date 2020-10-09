#! /usr/bin/env python3
class Cliente:
    '''Clase madre para todos los clientes, tanto corporativos como
    particulares'''

    def __init__(self, telefono, mail, id_cliente=None):
        # Si no se provee de un id, se crea el objeto con id "None"
        self.id_cliente = id_cliente 
        self.telefono = telefono
        self.mail = mail 
        
