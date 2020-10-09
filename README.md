# Trabajo práctico final
# Gestión de Software II - 2º 2ª

## Contexto
Se trata de realizar un sistema para un pequeño comercio que realiza
reparaciones eventuales. Es decir: se trata de trabajos que se realizan "por
única vez", no tienen ninguna periodicidad fija.

El sistema se utilizará en una única computadora, a nivel interno. Por lo tanto,
no se requiere login de usuario, ni permisos de ingreso, ni ningún tipo de
 previsión de seguridad fija. El sistema será utilizado únicamente por el área
de taller, por lo que no se ocupa de fijar presupuestos ni de registrar pagos:
no involucra dinero en ningún punto.

El comercio trabaja con dos tipos de clientes: particulares y corporativos. De
los clientes **corporativos** se tienen los siguientes datos:

- id de cliente
- nombre de la empresa
- telefono
- mail
- nombre del contacto
- telefono particular del contacto

De los clientes **particulares** se tienen los siguientes datos:

- id de cliente
- nombre
- apellido
- telefono
- mail

De cada uno de los **trabajos** se tienen los siguientes datos:

- id
- cliente al que pertenece el trabajo
- fecha de ingreso al taller
- fecha de entrega propuesta (la fecha en que el comercio se comprometió con
el cliente que el trabajo estaría listo).
- fecha de entrega real (la fecha en que realmente se finalizó el trabajo
finalizado; podría coincidir con la fecha comprometida, o bien adelantarse o
demorarse).
- descripcion: Un texto que describe el trabajo a realizar.
- retirado: Un valor booleano que indica si el trabajo ya fue retirado por el
cliente (`True`) o si aún está en el taller (`False`).

Se proveen dos **repositorios**: `RepositorioClientes` y `RepositorioTrabajos`, que
son clases Python que se encargan de *persisitir* (es decir: almacenar de forma
permanente) y gestionar estos datos en una base de datos sqlite. Dicha base de
datos está en el archivo base_datos.sqlite.

Para que funcione sqlite en sistemas **GNU/Linux**, debemos instalar el gestor de
bases de datos con el comando `sudo apt install sqlite3` (Debian, Ubuntu, Mint,
etc); o bien `sudo dnf install sqlite3` (Fedora).

En sistemas **Windows**, debemos descargar el archivo `.dll` correspondiente a
nuestra versión (32 o 64 bits, lo más probable es que sea de 64b), desde [esta
página](https://sqlite.org/download.html#win32). Dicho archivo debe estar en
la misma carpeta en donde tenemos el resto de nuestro código. 

También puede ser útil [instalar](https://sqlitebrowser.org/) el programa **DB
Browser**, para constatar qué datos se están guardando en nuestra Base de
Datos.

## Consigna
1. *Forkear* este repositorio, y realizar el código en Python, utilizando
adecuadamente Git para control de versiones y GitHub para alojar el repositorio.
Es importante realizar *commits* frecuentes, para que se vaya guardando el 
progreso de nuestro trabajo. (*1 punto*)
2. Realizar un *CRUD* (Create, Read, Update, Delete) de clientes. El sistema
debe permitir a cualquiera de los trabajadores del comercio cargar nuevos
 clientes, buscar información sobre uno o más clientes, actualizar los datos de
clientes existentes, y eliminar clientes. Al cargar un nuevo cliente, el id
del mismo es asignado por la base de datos. El método `store()` del 
RepositorioClientes retorna este valor. (*2&frac12; puntos*)
3. Cargar nuevos trabajos: Al cargar un trabajo nuevo, se debe indicar el
cliente al que pertenece, la fecha de ingreso (por defecto se toma la fecha del
día), la fecha de entrega propuesta, y la descripción. El valor de la fecha de
entrega real debe ser `None`, y el de `retirado` debe ser `False`. El id del
trabajo es asignado automáticamente por la base de datos, y es retornado por
el método `store()` del repositorio. (*1 punto*)
4. Registrar que un trabajo ha sido finalizado. Se debe modificar la fecha de
entrega real, definiéndola como la fecha del día. (*&frac12; punto*)
5. Registrar que un trabajo ha sido entregado. Se debe modificar el valor de la
propiedad `retirado` como `True`. (*&frac12; punto*)
6. Modificar un trabajo: Modificar o corregir cualquiera de los datos de un
trabajo, como por ejemplo su descripción, o su fecha de ingreso. **No** se puede
cambiar el cliente al que pertenece el trabajo, ni su número de id. (*1 punto*)
7. Eliminar un trabajo: Cuando un trabajo se cancela, directamente se lo elimina
de la Base de Datos. (*&frac12; punto*)
8. Generar un *informe* que consideren útil (*1 punto*). Por ejemplo:
    - listado de trabajos no finalizados cuya fecha de entrega propuesta es el
día de hoy o días anteriores.
    - listado de trabajos finalizados hace más de 3 días pero que aún no han
sido retirados
    - dado un cliente, historial de trabajos encargados por ese cliente
    - algún otro informe que les parezca útil
    - **Estos item son *opciones*, de los cuales deben elegir solamente uno**
8. Para la interfaz de usuario se puede optar por una de las siguientes
 opciones:
    - Interfaz gráfica de usuario, con la librería tkinter (*2 puntos*)
    - Interfaz de línea de comandos (*1 punto*)

## Modalidad de trabajo
- Este trabajo puede ser realizado de manera individual, o de a pares. En este
último caso, se debe enviar un mail al docente antes del día **viernes 16/10**. 
Los alumnos que el día 17/10 no hayan informado con quién van a trabajar, se 
considera que harán el trabajo individualmente.
- En el repositorio, debe quedar claro qué parte del código aporta cada
integrante del grupo, para poder establecer la calificación de cada estudiante.
Procuren repartir equitativamente las colaboraciones.
- Los estudiantes que adeuden *trabajos anteriores*, deberán entregarlos, como
máximo el día **viernes 23/10**. Los estudiantes que el día 24/10 no hayan
 entregado alguno de los primeros 5 trabajos del año, deberán recuperarlos en
instancias de examen final.
- **Fecha de entrega del Trabajo Final: viernes 30/10.** (Esta es la fecha
definida para parcial por la institución, pero **no** se tomará examen en el
sentido tradicional; la materia se aprueba por trabajos prácticos). *No se
 aceptarán entregas de quienes adeuden trabajos anteriores.*
- **Modalidad de entrega:** Por correo electrónico, con un link al repositorio
en donde está el código terminado.
- Devolución del trabajo práctico: viernes 06/11.
- **Fecha de reentrega de quienes deban realizar correcciones: viernes 13/11**
(este es el día fijado por la institución para el recuperatorio). Quienes no
hayan entregado el trabajo el 30/10, pueden entregarlo directamente el 13/11,
pero si es necesario hacer correcciones, pasarán directamente a instancia de
examen final.
- La semana del 16/11 se entregarán las calificaciones de la materia.

## Agenda
- **Viernes 9 de octubre:** Publicación de las consignas del trabajo final.
- **Lunes 12 de octubre:** Feriado nacional.
- **Viernes 16 y lunes 19 de octubre:** Clase de consulta.
- **Viernes 23 de octubre:** Clase de consulta. Último plazo para entregar los
TP 1 a 5 (atrasados). 
- **Lunes 26 de octubre:** Clase de consulta.
- **Viernes 30 de octubre:** Entrega del TP Final.
- **Lunes 2 y viernes 6 de noviembre:** Devolución de los trabajos corregidos.
- **Lunes 9 de noviembre:** Clase de consulta para quienes deban reentregar el
TP.
- **Viernes 13 de noviembre:** Último plazo de entrega del TP Final. Esta fecha
es estricta, porque es el día en que finaliza el 2º cuatrimestre.
- **Semana del 16 de noviembre:** Entrega de calificaciones finales.

