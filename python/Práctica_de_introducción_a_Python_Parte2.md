# **Práctica de introducción a Python - Parte 2**

### Alternativa condicional

##### **Ejercicio 1**
Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.

    str = input("Ingrese una palabra o una frase: ")
    cap = str.capitalize() #sino puedo usar str.isupper[0]
    if str == cap: 
      print("la primer letra es mayúscula.")
    else: 
      print("la primer letra es minúscula")

##### **Ejercicio 2**
Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además informe si es par o impar (el 0 es un número par).

    numero = int(input("Ingrese un número: "))
    if numero > 0: 
      print("es positivo")
    if numero%2 == 0: 
      print("es par")
    else: 
      print("es impar")
    elif numero < 0: 
      print("es negativo")
    if numero%2 == 0: 
      print("es par")
    else: 
      print("es impar")
    else: 
      print("es cero y par")

##### **Ejercicio 3**
Escribí un programa que dado un número del 1 al 6, ingresado por teclado, muestre cuál es el número que está en la cara opuesta de un dado. Si el número es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto el número ingresado.

    num = int(input("Escribí un número del 1 al 6: "))
    if  num >= 1 or num <= 6: 
      print("la cara opuesta del dado es ") + str(7 - num)
    else: 
      print("el número ingresado es incorrecto") 

##### **Ejercicio 4**
Una compañía de transporte internacional tiene servicio en algunos países de América del Sur, América Central, América del Norte, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido, tal como se muestra en la tabla:
| Zona | Ubicación | Costo/gramo |
| -- | -- | -- |
| 1 | América del Sur | 10.00 dólares |
| 2 | América Central | 15.00 dólares |
| 3 | América del Norte | 18.00 dólares |
| 4 | Europa | 24.00 dólares |
| 5 | Asia | 30.00 dólares |

Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. Realizá un programa para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

    peso_paquete = int(input("Ingrese el peso del paquete: "))
    lugar = input("Ingrese la ubicación de la entrega: ")
    costos_ubicacion = {"America del sur": "10usd", "America central": "15usd", "America del norte": "18usd", "Europa": "24usd", "Asia": "30usd"}
    if peso_paquete <= 5: 
      print("el cobro por entrega es " + costos_ubicacion[lugar])  
    else: 
      print("su entrega fue rechazada, no puede transportarse por exceso de peso")

##### **Ejercicio 5**
Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.

    num_dia = int(input("Ingrese el número del día del 1 al 7: "))
    dias_semana = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes", 6:"Sábado", 7:"Domingo"}
    if num_dia > 7 or num_dia < 1: 
      print("el número ingresado es inválido, intentelo nuevamente")
    else: 
      print(dias_semana[num_dia])

### Listas

##### **Ejercicio 6**
Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.

_Recordá que la manera de copiar una lista en otra es:_

```python
lista2 = list(lista1)
```
    lista = [input(), input(), input(), input(), input()]
    lista_invertida = [lista[4], lista[3], lista[2], lista[1], lista[0]]
    print(lista_invertida)

##### **Ejercicio 7**
Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta que se introduzca un número negativo. Una vez hecho esto se deben imprimir los elementos de la lista.

    numero = int(input("Ingrese un número: "))
    lista_num = [] 
    while numero >= 0:
      lista_num.append(numero)
    print(lista_num)

##### **Ejercicio 8**
Realizá un programa que declare tres listas _lista1_, _lista2_ y _lista3_, donde las dos primeras listas deben tener cinco enteros cada una, ingresados por teclado y asigne para cada elemento de la _lista3_ la suma de los elementos de la _lista1_ y la _lista2_ (es decir, el primer elemento de la _lista3_ tiene que ser la suma del primer elemento de la _lista1_ y el primero de la _lista2_)

    Lista1 = [int(input("ingrese 5 numeros, uno por linea: ")), int(input()), int(input()), int(input()), int(input())]
    Lista2 = [int(input("ingrese 5 numeros nuevamente: ")), int(input()), int(input()), int(input()), int(input())]
    Lista3 = [Lista1[0]+Lista2[0], Lista1[1]+Lista2[1], Lista1[2]+Lista2[2], Lista1[3]+Lista2[3], Lista1[4]+Lista2[4]]
    print(Lista3)

##### **Ejercicio 9**
Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. Se debe introducir el nombre y la edad de cada alumno por teclado. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (__*__). Al finalizar se deben mostrar los siguientes datos:

* La edad máxima de todos los alumnos.
* Los alumnos que tengan la edad máxima

      lista_nombre = []
      lista_edad = []
      nombre = input('ingrese el nombre del alumno: ')
      edad = input('ingrese la edad del alumno: ')

      while nombre != "*":
      lista_nombre.append(nombre)   
      lista_edad.append(edad)
      nombre = input('ingrese el nombre del alumno: ')
      if nombre == "*":
        continue
      edad = input('ingrese la edad del alumno: ')
      print("la edad máxima de los alumnos es: " + max(lista_edad))
      dic = {"lista_nombre" : "lista_edad"} 

### Diccionarios

##### **Ejercicio 10**
Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).

    diccionario = (1:"mercurio)
    
    for caracter in cadena: 
      contadores[caracter] += 1
    else: 
      contadores[caracter] = 1

    for clave, valor in contadores.items(): 
       print(clave, valor)

##### **Ejercicio 11**
Modificá el programa anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.

    ontadores = {} 
    aclfabeto = "abcdefghijklmnopqrstuvwxyz"

    for letra in alfabeto + alfabeto.upper(): 
      contadores[letra] = 0

    cadena = input("Escribí una cadena de caracteres: ")

    for caracter in cadena: 
      if caracter.lower() in alfabeto: 
        contadores[caracter] += 1

    for campo, valor in contadores.items(): 
      print (campo, valor)

##### **Ejercicio 12**
Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guardá la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
El programa tiene que pedir el número de alumnos que se va a introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo. Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.

    cantidad = int(input("Introducir cantidad de alumnos: "))
    alumnos = {} 

    for numero in range(cantidad): 
      alumno = input("alumno: ")
      notas = [] 
      nota = int(input("nota: "))
      while nota >= 0:
        notas.append(nota)
        nota = int(input("nota: "))
     alumnos[alumno] = notas 

    for alumno in alumnos: 
      print(alumno, sum(alumnos[alumno]) / len(alumnos[alumno])) 

### Funciones

##### **Ejercicio 13**
Creá un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro creando la función **esMultiplo**.

    n1 = int(input('Ingrese un número: '))  
    n2 = int(input('Ingrese el otro número: '))

    def esMultiplo(n1, n2): 
      if (n1%n2) == 0: 
        print(str(n1) + ' es múltiplo de ' + str(n2)) 
      if (n2%n1) == 0: 
        print(str(n2) + ' es múltipo de ' + str(n1))
      else: 
        print('Los números que ingresaste no son múltiplos entre sí')

##### **Ejercicio 14**
Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa tiene que pedir el número de días que se van a introducir.

    def temperatura_media(temperatura_max, temperatura_min):
        print((temperatura_max + temperatura_min)/ 2)

    temperatura=int(input("introducir cantidad de dias a medir: "))
    dias={}

    for temp in range(temperatura):
        dia=input("Dia: ")
        temp_media=[]
        temperatura_max=int(input("Temp Máxima del día: "))
        temperatura_min=int(input("Temp mínima del día: "))
        temp_media.append(temperatura_media(temperatura_max, temperatura_min))
        dias[dia]=temp_media  
    print(dias)

##### **Ejercicio 15**
Creá un programa para gestionar datos de los socios de un club, el cual permita:

* Cargar la información de los socios en un diccionario para acceder por número de socio. Los datos que se deben almacenar son: _número_, _nombre y apellido_, _fecha de ingreso (ddmmaaaa)_, _cuota al dia (s/n)_ (el programa tiene que dejar de cargar cuando se ingrese el _número_ **0**). El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:

  **Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día**
  
  **Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día**
  
  **Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día**

* Informar la cantidad de socios que tiene el club.

* Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.

* Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.

* Solicitar el nombre y apellido d eun socio y darlo de baja (eliminarlo del listado).

* Imprimir el listado de socios completos.

Definir las funciones que creas necesarias.

    socios_activos = {1: ["Florencia Ocampo", "14092001", True], 2: ["David Estévez", "14092001", True], 3: ["Sofía Cáceres", "14092001", True]}

    len(socios_activos) #Informar la cantidad de socios que tiene el club.
    def cargarSocios(socios):
        numero = int(input("Número de socio: "))
        while numero != 0:
            nombre = input("Nombre y apellido: ")
            fecha = input("Fecha de ingreso: ")
            cuota = input("¿Cuota al día? s/n: ")
           pago = cuota.lower() == "s"
           socios[numero] = [nombre, fecha, pago]
           numero = int(input("Número de socio: "))
       return socios
    
    def modificarFecha(socios, fechaAnterior, fechaNueva):
       for datos in socios.values():
            if datos[1] == fechaAnterior:
               datos[1] = fechaNueva
        return socios
    
    
    def numeroSocio(socios, nombre):
            for numero,datos in socios.items():
               if datos[0].lower() == nombre.lower():
                    return numero
           return 0
                
                
    def formatoFecha(fecha):
        return fecha[:2] + "/" + fecha[2:4] + "/" + fecha[4:]


    def imprimirListado(socios):
        for numero,datos in socios.items():
            print("Número: ", numero)
            print("Nombre: ", datos[0])
           print("Fecha de ingreso ", formatoFecha(datos[1]))
           if datos[2]:
               print("Cuota al día")
           else:
                print("En deuda")
            print("---------------")
       return None

    socios_activos = {1: ["Florencia Ocampo", "14092001", True], 2: ["David Estévez", "14092001", True], 3: ["Sofía Cáceres", "14092001", True]}

    print("Cargar socios")
    socios_activos = cargarSocios(socios_activos)

    print("El club tiene", len(socios_activos), "socios")

    print("Registrar pago de cuotas")
    numero = int(input("Numero de socio: "))
    socios_activos[numero][2] = True

    print("Modificando fecha de ingreso...")
    socios_activos = modificarFecha(socios_activos, "21102017", "22102017")

    print("Eliminar socio:")
    nombre = input("Nombre y apellido: ")
    numero = numeroSocio(socios_activos, nombre)
    del socios_activos[numero]

    imprimirListado(socios_activos)