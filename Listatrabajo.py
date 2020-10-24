#! /usr/bin/env python3

from repositorioTrabajos import RepositorioTrabajos
from trabajo import Trabajo
import datetime
from datetime import date

class TrabajosLista:


    def __init__(self):
        self.rt = RepositorioTrabajos()
        self.lista_trabajos = self.rt.get_all()

    def alerta_trabajos(self, dias):
        """Recibe un numero (cantidad de días) y crea una lista con las fechas de esos proximos cantidad de dias"""
        alertas = [] #Listado de fechas a comparar
        hoy = datetime.date.today()
        for c in range(dias+1):
            f = hoy + datetime.timedelta(days=c)
            f = date(f.year, f.month,f.day)
            alertas.append(f)

        return alertas

    def nuevo_trabajo(self, cliente, fecha_ingreso, fecha_entrega_propuesta, descripcion):
        """Crea un nuev trabajo y lo agrega a la lista y a la base de datos"""
        t = Trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, None, descripcion, False)
        t.id_trabajo = self.rt.store(t)
        if t.id_trabajo == 0:
            return None
        else:
            self.lista_trabajos.append(t)
            return t

    def buscar_por_id(self, id_trabajo):
        """Buscar el trabajo con el ID dado"""
        c = self.rt.get_one(id_trabajo)
        return (c)

    def establecer_entrega(self, id_trabajo, retirado):
        c = self.buscar_por_id(id_trabajo)
        if c:
            c.retirado = retirado
            return self.rt.update(c)
        return None

    def establecer_final(self, id_trabajo):
        c = self.buscar_por_id(id_trabajo)
        if c:
            c.fecha_entrega_real = datetime.date.today()
            return self.rt.update(c)
        return None

    def modificar_datos_trabajos(self, id_trabajo, fecha_ingreso, fecha_entrega_propuesta, fecha_entrega_real ,descripcion, retirado):
        """Modificar o corregir los datos de un trabajo particular"""
        c = self.buscar_por_id(id_trabajo)
        if c:
            c.fecha_ingreso = fecha_ingreso
            c.fecha_entrega_propuesta = fecha_entrega_propuesta
            c.fecha_entrega_real = fecha_entrega_real
            c.descripcion = descripcion
            c.retirado = retirado
            return self.rt.update(c)
        return None

    def  eliminar_trabajo(self, id_trabajo):
        c = self.buscar_por_id(id_trabajo)
        if c:
            return self.rt.delete(c)
        return None