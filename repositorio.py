#! /usr/bin/env python3
import sqlite3

class Repositorio:
    '''Consulta y escribe en la BD. Clase madre de los otros repositorios'''

    def __init__(self):
        self.bd = sqlite3.connect("base_datos.sqlite")
        self.cursor = self.bd.cursor()
        
