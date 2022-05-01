La entrega del examen se hará por este medio: tendrás que confeccionar el código adecuado para realizar cada actividad, generar los archivos correspondientes en el caso deser necesario y pushearlos a este repo que se te generó automáticamente.

Las devoluciones de este examen se harán por GitHub Classroom, por medio de Issues y comentarios. Debés hacer un commit cada 5 min, de lo contrario tu entrega no será considerada válida. En todo momento debés estar conectado al zoom, con la cámara prendida.

**Consigna N°1**

Escribir funciones que, dado un String, permitan obtener

a) cuántas veces aparece el string abc. P.ej. aparece 2 veces en xcabcb3sabc9, y ninguna en hola amigos mios.

b) la lista de los substrings delimitados entre ‘aa’ y ‘gg’, que no incluyan ninguna ‘c’. P.ej. en ‘ttaatatggttaacatgg’, debe tomar solamente ‘tat’, rechazando ‘cat’.

        a)
        import re
        texto = "xcabcb3sabc9"
        patron = "abc"
        print(re.search(patron, texto))
        print(re.search(abc,xcabcb3sabc9))

        <re.Match object; span=(3, 6), match='abc'>

        import re
        texto = "xcabcb3sabc9"
        patron = "abc"
        print(re.findall(patron, texto))
        print(re.findall(abc,xcabcb3sabc9))

        ['abc', 'abc']

        import re
        texto = "hola amigos mios"
        patron = "abc"
        print(re.search(patron, texto))
        print(re.search(abc,hola amigos mios))

        None

        import re
        texto = "hola amigos mios"
        patron = "abc"
        print(re.findall(patron, texto))
        print(re.findall(abc,hola amigos mios))

        []

        b)
        string = "aa([^c].*?)gg"
        patron = "ttaatatggttaacatgg"

        def obtener_substrings(patron):
            print(re.findall(string, patron))

        obtener_substrings(patron)

        ['tat']

**Consigna N°2**

Se está pensando en el diseño de un juego que incluye la nave espacial Enterprise. En el juego, esta nave tiene un nivel de potencia de 0 a 100, y un nivel de coraza de 0 a 20. La Enterprise puede:

encontrarse con una pila atómica, en cuyo caso su potencia aumenta en 25.
encontrarse con un escudo, en cuyo caso su nivel de coraza aumenta en 10.
recibir un ataque, en este caso se especifican los puntos de fuerza del ataque recibido. La Enterprise "detiene" el ataque con la coraza, y si la coraza no alcanza, el resto se descuenta de la potencia. Por ejemplo si la Enterprise con 80 de potencia y 12 de coraza recibe un ataque de 20 puntos de fuerza, puede parar solamente 12 con la coraza, los otros 8 se descuentan de la potencia. La nave debe quedar con 72 de potencia y 0 de coraza. Si la Enterprise no tiene nada de coraza al momento de recibir el ataque, entonces todos los puntos de fuerza del ataque se descuentan de la potencia.
La potencia y la coraza tienen que mantenerse en los rangos indicados, por ejemplo, si la Enterprise tien 16 puntos de coraza y se encuentra con un escudo, entonces queda en 20 puntos de coraza, no en 26. Tampoco puede quedar negativa la potencia, a lo sumo queda en 0. La Enterprise nace con 50 de potencia y 5 de coraza. Implementar este modelo de la Enterprise, que tiene que entender los siguientes mensajes:

potencia()
coraza()
encontrarPilaAtomica()
encontrarEscudo()
recibirAtaque(puntos)

Al ejecutar esto:

enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()

la potencia de la Enterprise debe ser 66, y su coraza debe ser 10.

Agregar al modelo de la Enterprise, la capacidad de entender estos mensajes.

fortalezaDefensiva(), que es el máximo nivel de ataque que puede resistir, o sea, coraza más potencia.
necesitaFortalecerse(), tiene que ser true si su coraza es 0 y su potencia es menos de 20.
fortalezaOfensiva(), que corresponde a cuántos puntos de fuerza tendría un ataque de la Enterprise. Se calcula así: si tiene menos de 20 puntos de potencia entonces es 0, si no es (puntos de potencia - 20) / 2.

        class Enterprise:
    def __init__(self):
        self.potencia = 50
        self.coraza = 5

    def potencia(self):

    def coraza(self):
        12 detiene ataque 
        si no alcanza -= 8 self.potencia

    def encontrarPilaAtomica(self):
        self.potencia += 25

    def encontrarEscudo(self):
        self.coraza += 10

    def recibirAtaque(self, puntos):
        return puntos 

    def fortalezaDefensiva(self):
        return self.coraza + self.potencia

    def necesitaFortalecerse(self):
        if coraza = 0 amd potencia < 20:
            return True
        elif:
            false

    def fortalezaOfensiva(self):
        if self.potencia < 20:
            return 0
        elif:
            self.potencia - 20 / 2
        
    

**Consigna N°3**

Dado el siguiente enlace "https://ponyweb.ml/v1/character/all", realizar las siguientes actividades adjuntando los archivos resultantes y el código utilizado para la realización de cada paso:

a) ¿Cuál es el dominio al que estamos consultando?

b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué content_type?

c) Averigüá cuántos Ponies almacena la API

d) ¿Cómo esperás que sea la URL para obtener la información del Pony 37? ¿y cómo será la url para obtener todas las canciones (song)? Probalas y comentá que otras URL se te ocurrirían para reemplazar las que existen

e) Guardar los datos correspondientes al Pony 37 en un archivo cuyo nombre sea el nombre del poni correspondiente y extensión ".txt"