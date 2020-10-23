from repositorioTrabajos import RepositorioTrabajos
from trabajo import Trabajo
import datetime


class TrabajosLista:


    def __init__(self):
        self.rt = RepositorioTrabajos()
        self.lista_trabajos = self.rt.get_all()

    def nuevo_trabajo(self, cliente, fecha_ingreso, fecha_entrega_propuesta, descripcion):
        """Crea un nuev trabajo y lo agrega a la lista y a la base de datos"""
        t = Trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, None, descripcion, False)
        t.id_trabajo = self.rt.store(t)
        if t.id_trabajo == 0:
            return None
        else:
            self.lista_trabajos.append(t)
            return t

    def borrar_trabajo(self, cliente, fecha_ingreso, fecha_entrega_propuesta, descripcion):
        """Crea un nuev trabajo y lo agrega a la lista y a la base de datos"""
        t = Trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, None, descripcion, False)
        t.id_trabajo = self.rt.store(t)
        if t.id_trabajo == 0:
            return None
        else:
            self.lista_trabajos.append(t)
            return t
