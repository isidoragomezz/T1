# Tarea 1: DCCortaRamas 🌳✂️

Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

## Consideraciones generales :octocat:

-mi main.py trata de visualizar y acomodar un bonsai de la forma que una persona externa quiera modificarlo.
-las ultimas 2 funciones de dccortarama no funcionan en nada, no alcance a llegar a ellas y en emparejar_bonsai me dan 6 test malos
-explique cda funcnion y que es lo que hacen o no en comentarios arriba de cada funcion

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Menú: 13 pts (21,7%)
##### ❌✅🟠 Consola #no se que es esto
##### ✅ Menú de Inicio
##### ✅ Menú de Acciones
##### ❌✅🟠 Modularización #no se que es esto
##### ❌✅🟠 PEP8 #no se que es esto


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  `main.py`. Además se debe crear los siguientes archivos y directorios adicionales:
1. `dccortarama.py` en `ingresados a github junto con main.py`
2. `carpeta 'data'` en `github\IIC2233\Syllabus\tareas\T1\data` (si son carpetas o archivos fuera de estos genera un buble al no ser los archivos y carpetas correspondientes)

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. `utilidades.pyc`: `visualizar_bonsai()` (lo importe en el dccortarama)
2. `dccortarama.py`: `todas las funciones` (lo importe en el main.py)
3. `sys`           : `sys.exit()` (importado en el main.py)
4. `os`            : `os.path.dirname(os.path.abspath(__file__),os.path.join(verificar_carpeta, "data"), os.path.isdir, os.path.isfile y os.path.join(carpeta, archivo)` (importado y usado en main.py)
5. `os`            : `os.path.join("data", carpeta, archivo)` (importado y usado en dccortarama)

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. `dccortarama`    : `todas las funciones` (importado y usado en main.py)

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. utilice un supuesto en linea 31 donde en `clase_bonsai= dccortaramas.Bonsai("victor", 10, 27, estructura)` y mi suespuesto es `"victor", 10, 27, []` en el main.py.

2. utilice un supuesto en linea 35 donde en `clase_bonsai.visualizar_bonsai("Vertical", True, False)` y mi supuesto es `"Vertical", True, False` en el main.py

PD: <los supuestos fueron usados para poder verificar que todo lo que estoy haciendo funcione correctamente, ya que me generaba problemas al no tener parametros>

-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. <[link de código](https://programacion.top/python/que-es-la-libreria-os-en-python/)>: ocupo lineas de codigo que me ayudaron a verificar que los archivos se encuentren en el `data` utilizando la libreria os, tiene eexplicacion detallada de como usarla y por eeso la utilice>

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/main/Tareas/Bases%20Generales%20de%20Tareas%20-%20IIC2233.pdf).