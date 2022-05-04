**RESUMEN**

Comando para entrar a otra carpeta dentro del directorio: cd (nombre)
Comando para listar los archivos de la carpeta: ls 
Comando para saber en qué carpeta estoy: pwd 
Comando para volver al directorio anterior: cd ..
Comando para cambiar directorio: cd




**División exacta**
Por ejemplo: 

def termos_por_ronda(personas): 
  return (personas * 30) // 1000 
Esto devuelve el primer número sin la coma, es decir el entero. 
En el caso de hacer termos_por_ronda(40) = 1.2 pero con // te devuelve 1

**While** 
Para generar un bucle, es decir que se repite n° cantidad de  veces hasta que la condición se cumple. 
Junto al while se debe de incluir la condición que se quiere cumplir antes de devolver algo.
 
ej)
cantidad = int(input("Introducir cantidad de alumnos: "))
alumnos = {} 
 
for num in range(0, cantidad): 
      alumno = input("Alumno: ")
      notas = [] 
      nota = input("Nota: ")
      while nota >= 0:
            notas.append(nota)
            nota = int(input("Nota: "))
      alumnos[alumno] = notas 

**Expresiones regulares**
Metacaracteres o caracteres especiales son aquellos caracteres que determinan algún formato de texto. 

Una expresión regular es una forma en la que puedo representar un conjunto de caracteres/ string. Las expresiones regulares sirven para buscar patrones de texto o caracteres en general. 
Permite encontrar caracteres específicos.
 
La shell es la terminal que me permite interactuar con la máquina y es donde se ejecuta el intérprete. El intérprete me deja elegir el lenguaje. Cuando la shell está activa tiene de prompt un ‘>’.
 
Un script es una pequeña porción de código que está en un archivo ejecutable (extensión adecuada) que se ejecuta contra el intérprete. 
Para abrir un archivo (ya que cd sólo abre carpetas): python3 nombre_arch.py

# r que se lea literalmente lo que está entre comillas
    .cualquier caracter
    *0 o mas veces
    ? ve todos los patrones dentro de string, no solo el primero y el ultimo
    ^ no contar un caracter/rango que venga despues de ^
    \. que aparezca literalmente un punto, no el metacaracter
    + 0 o más veces

# Por ejemplo: 
\n(salto de línea)
\s(espacios)
\t(tab o cambio de pestaña)
\d(todo lo que sea número)
\D(lo que no sea número)
\w(letras o alfanumérico) 
\w caracter alfanumerico
\S cualquier caracter que no sea espacio

# Metacaracteres delimitadores: 
	^ : inicio de línea 
	$ : fin de línea 
	\A : inicio de texto
	\Z : fin de texto
	. (punto) : coincide con cualquier carácter en una línea dada

# Metacaracteres cuantificadores: 
	* : cero o más, todas las ocurrencias de un dado substring
	+ : una o más ocurrencias del patrón 
	? : cero o una
	{n} : exactamente n veces 
	{n,m} : por lo menos n y menos de m

read ´r´
write ´w´ → sobreescribe 
apper ´a´ → agregar


Importar la biblioteca = import os 
Hacer pwd en biblioteca os = cwd
Cambiar de directorio = chdir()
Hacer ls en biblioteca = list.dir()
Crea una carpeta = os.mkdir() 

path = string

**Librería re**
Match o re.match sirve para buscar en la primera palabra pero en re.search te busca cualquier aparición en todo el texto y si quiero encontrar todas las apariciones, usamos re.findall(). Con findall() te devuelve una lista y con group() te devuelve un string. El re.sub te reemplaza a todo el patrón por lo que quieras en todas las ocurrencias del texto. 

**CONTROL DE VERSIONES**
El control de versiones registra las diferentes versiones del archivo, el historial del código. 
Cada registro de estos cambios se denomina commit y se hace git.commit. 

Commit funciona como un “paquete” de cambios realizados, que se pueden ir agregando al stage (estado intermedio con cambios) mediante el comando git add. 

El espacio intermedio entre haber hecho commit (checkpoint) y no hacer nada se lo invoca como git.add en donde se le agregan los cambios o como historial de cambios. Si haces commit sin hacer add no funciona. 
 
¿Qué son los repositorios? Es un almacenamiento al que se accede de manera en línea. 
¿Qué es internet? Es una conexión física y cableada entre máquinas.  
¿Qué es la nube? Todo lo que puedo acceder a través de internet. 

Luego de commit, con git.push (subo cambios) empujo todos los cambios a la nube de GitHub y para volver para atrás se hace git.pull, en donde descargo todos (bajo cambios). 

¿Cómo clonar un repositorio? Haciendo git clone + url del enlace 
Otra opción es ir a GitHub Desktop -> ir a file -> ir a clone repository -> copiar el url de la web. 
El clone es equivalente a hacer un pull, con la diferencia que pull es solo lo nuevo y clone es todo. 

Permite rastrear datos. Estado o cambio que se realiza en un archivo. (Github)
editar {archivo}
git add {archivo} → agrega nuevas líneas.
git commit {archivo} → guarda el proceso para la próxima vez que abras el archivo.
git push → empujar el archivo a la nube. subir cambios.
git pull → descarga cambios más recientes del archivo. bajar cambios.

**OBJETOS POO**
¿Qué es programar orientado a objetos? Es una forma de programar. En Python todos son objetos. Creamos entidades computacionales orientadas a objetos. Las características de objetos: 
Cuando los objetos hacen o pueden hacer algo en principio no tienen porqué responder nada. Pero cuando el objeto hace o conoce la operación que le pedimos no tira error. 
Los objetos tienen o entienden ciertos atributos. Un atributo para un objeto es todo aquello que un objeto puede hacer. Los objetos pueden tener un estado, osea de qué cosas es inherente el objeto.  

En el caso de pepita es el estado, pero puede fluctuar y se conoce como el comportamiento de los objetos. 
Los objetos: entes que entienden mensajes, tienen un estado,  tienen identidad y son distintas instancias comparando (obj1 == obj2). 
Al ser ambos de una clase, podemos esperar que hagan lo mismo las dos. 
El comportamiento de ambos objetos puede ser diferente, aunque sean de la misma clase. 
Para importar varios ‘elementos’ de un diccionario se puede hacer todo junto separado por una coma. Por ejemplo podemos hacer lo siguiente: >>> from aves import pepita, anastacia, roberta  

La interfaz de un objeto es el conjunto de mensajes que entiende. El ambiente es el contexto en el que vive un objeto. Dentro del mismo ambiente pueden convivir varios objetos. 
Polimorfismo. → tiene que haber un tercer objeto (observador).

**Clases de objetos**
Para crear una clase se inicia con la palabra class y por consiguiente se escribe el nombre de la clase en mayúscula. Los métodos son los mensajes que puede hacer un objeto. 
La diferencia entre un método y una función, es que la última está por fuera de la clase. 
En el método, siempre tienen como primer argumento el self, quien  representa un objeto dado
El __init__ es el constructor de pepita por ejemplo. Veámos un ejemplo:

__init__ viene de la palabra en inglés initialize que en castellano es inicializar. Es lo que se conoce como el constructor de una clase y nos permite darle valores iniciales a los atributos de sus instancias a la hora de crearlas. 

Por su parte, self(que en castellano sería algo así como yo) es un primer parámetro obligatorio que nos permite acceder a los atributos del objeto que estamos instanciando. Si bien ese parámetro no debe llamarse selfobligatoriamente, es la convención que se utiliza para nombrarlo y la respetaremos a lo largo de todo el recorrido. 