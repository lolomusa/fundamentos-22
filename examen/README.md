dolores msuacchio

La entrega del examen se hará por este medio: tendrás que confeccionar el código adecuado para realizar cada actividad, generar los archivos correspondientes en el caso deser necesario y pushearlos a este repo que se te generó automáticamente.

Las devoluciones de este examen se harán por GitHub Classroom, por medio de Issues y comentarios. Debés hacer un commit cada 5 min, de lo contrario tu entrega no será considerada válida. En todo momento debés estar conectado al zoom, con la cámara prendida.

**Consigna N°1** (RE)
Escribir funciones que, dado un String, permitan obtener

 - cuántas veces aparece el string bc9. P.ej. aparece 2 veces en xsabc9cabcb3sabc9, y ninguna en hola amigos mios.
 - la lista de los substrings delimitados entre ‘aa’ y ‘gg’, que no incluyan ninguna ‘c’. P.ej. en ‘ttaatatggttaacatgg’, debe tomar solamente ‘tat’, rechazando ‘cat’.

        1)
        import re
        texto = "xsabc9cabcb3sabc9"
        patron = "bc9"
        print(re.search(patron, texto))
        print(re.search(bc9,xsabc9cabcb3sabc9))

        <re.Match object; span=(3, 6), match='bc9'>

        import re
        texto = "xsabc9cabcb3sabc9"
        patron = "bc9"
        print(re.findall(patron, texto))
        print(re.findall(bc9,xsabc9cabcb3sabc9))

        ['bc9', 'bc9']

        o

        import re
        def cuantas_veces(string):
            resultado = re.findall("bc9", string)
            return len(resultado)

        2)
        string = "aa([^c]*?)gg"  #aa literal | grupo de todo lo que no tenga c + cualquier caracter que se repita 0 o mas veces| gg literal
            patron = "ttaatatggttaacatgg"

        def obtener_substrings(patron):
            print(re.findall(string, patron))
            #print(re.findall(r"aa([^c]*?)gg", string))

        obtener_substrings(patron)

        o 

        def sin_c(string):
            return re.findall("aa([^c]*?)gg", string)

**Consigna N°2** (POO)

Un taller de diseño de autos quiere estudiar un nuevo prototipo. Para eso, nos piden hacer un modelo concentrado en las características del motor. El prototipo de motor tiene 5 cambios (de primera a quinta), y soporta hasta 5000 rpm.
La velocidad del auto se calcula así: _**(rpm / 100) * (0.5 + (cambio / 2))**_. Por ejemplo en tercera a 2000 rpm, la velocidad es 20 * (0.5 + 1.5) = 40.
También nos interesa controlar el consumo. Se parte de una base de 0.05 litros por kilómetro. A este valor se le aplican los siguientes ajustes:

* Si el motor está a más de 3000 rpm, entonces se multiplica por (rpm - 2500) / 500. Por ejemplo, a 3500 rpm hay que multiplicar por 2, a 4000 rpm por 3, etc.
* Si el motor está en primera, entonces se multiplica por 3.
* Si el motor está en segunda, entonces se multiplica por 2.

Los efectos por revoluciones y por cambio se acumulan. Por ejemplo, si el motor está en primera y a 5000 rpm, entonces el consumo es 0.05 * 5 * 3 = 0.75 litros/km.
El modelo debe entender estos mensajes:

```
arrancar() , se pone en primera con 500 rpm.
subirCambio()
bajarCambio()
subirRPM(cuantos)
bajarRPM(cuantos)
velocidad()
consumoActualPorKm(), calcula el consumo actual y lo devuelve
```

Al ejecutar esto:

```python
auto1 = Auto()
auto1.arrancar()
auto1.subirRPM(3500)
auto1.subirCambio()
auto1.subirCambio()
auto1.subirCambio()
auto1.bajarCambio()
```

la velocidad debería ser 80 y el consumo 0.15 litros/km.

        class Auto:
     def _init_(self):
        self.cambio = 0
        self.rpm = 0
        self.consumo = 0.05 

     def arrancar(self):
         self.cambio += 1
         self.rpm += 500
   
     def subirCambio(self): 
        if self.cambio < 5:
            self.cambio += 1
    
     def bajarCambio(self):
        if self.cambio > 1:
            self.cambio -= 1
  
     def subirRPM(self, RPM):
        if self.rpm + cantidad <= 5000:
            self.rpm += cantidad
        else:
            self.rpm = 5000
    
     def bajarRPM(self, RPM):
        if self.rpm - cantidad >= 0:
            self.rpm -= cantidad

     def Velocidad(self):
         return((self.rpm / 100) * (0.5 + (self.cambio / 2)))

     def consumoActualPorKm(self):
         if self.rpm > 3000:
             if self.cambio == 1:
                 return(self.consumo*((self.rpm - 2500) / 500)*3)
             elif self.cambio == 2:
                 return(self.consumo*((self.rpm - 2500) / 500)*2)
             elif self.cambio <= 5:
                 return(self.consumo*((self.rpm - 2500) / 500))
         elif self.cambio == 1:
             return(self.consumo*3)
         elif self.cambio == 2:
             return(self.consumo*2)
         else:
             return(self.consumo)
        #si los rpm son menores a 3000 y el auto en 3ra, 4ta o 5ta el consumo es el base


    def cambioActual(self):
        return (self.consumo)

    def rmpActual(self):
        return (self.rpm)


        auto1 = Auto()
        auto1.arrancar()
        auto1.subirRPM(3500)
        auto1.subirCambio()
        auto1.subirCambio()
        auto1.subirCambio()
        auto1.bajarCambio()
        auto1.Velocidad()
        auto1.consumoActualPorKm()
                la velocidad debería es 80 y el consumo 0.15 litros/km.

**Consigna N°3** (Manejo de exepciones)
Ejecutá el script_misterioso.py y realizá resolvé:
    1. ¿Qué tipo de exepción arroja la corrida del script? 
    2. Mejorá el código para que capture dicho error específicamente y lo maneje imprimiendo una advertencia al usuario sobre las posibles causas de dicho error
    3. ¿Qué otras excepciones deberias considerar?

        1 - la corrida del script devuelve ZeroDivisionError, es decir, error por división por cero.

        2 - 
        lo que agregue:
        def obtener_media(lista):
            sumatoria = 0

            for valor in lista:

                sumatoria += valor
            longitud = len(lista)
    
            try:
                return sumatoria / longitud
            except ZeroDivisionError:
                print("no se puede obtener la media ya que la longitud es 0 y  no se puede dividir por dicho numero") #0 la lista esta vacia o algo del estilo

        3 - 
        Otra excepcion a considerar es TypeError, ya que se podria ingresar un valor a la lista que no sea de un tipo compatibe con la operacion, así como también un OverFlowError, si la división arroja un numero con muchos decimales

        Se puede verificar que la lista es una lista, ya que si el parametro es de otro tipo (no iterable) el for no va a funcionar.

**Consigna N°4** (Manejo de archivos)

Escribí un programa que, por un lado, debe crear una nueva carpeta en la posición actual llamada _Resultado_ y, por otro, que lea todos los archivos con extensión `.txt` y escriba el contenido de todos en un único archivo llamado *texto_completo.txt*, que tiene que estar dentro de la carpeta _Resultado_. **NO se pueden usar rutas absolutas**

        import os
        import glob

        def unir_txt():
            os.mkdir("Resultado")

            lista_archivos = glob.glob("*.txt")
            with open("Resultado\\texto_completo.txt", 'a') as texto_completo:
                for archivo in lista_archivos:
                    with open(archivo, 'r') as file:
                        texto_completo.write(file.read())
                

**otra alternativa:**

        def unir_txt():
            os.mkdir("Resultado")
            lista_txt = glob.glob("*.txt")
            salida = open("Resultado/texto_completo.txt", "a")
            for txt in lista_txt:
                archivo = open(txt, "r")
                salida.write(archivo.read())
                archivo.close()
            salida.close()
