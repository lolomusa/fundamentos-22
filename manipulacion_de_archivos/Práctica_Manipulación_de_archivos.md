# **Manipulación de archivos**

##### **Ejercicio 1**
Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo **no** empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

        with open('nombreArchivo', 'r') as file: 
            fileContent = file.readlines()

        for fileline in fileContent: 
            noEmpiezaCon = 0 
            if not str.startswith(fileline, 'P'): 
                noEmpiezaCon += 1
            print(noEmpiezaCon) 

##### **Ejercicio 2**
Escribí un programa que lea un archivo e imprima las primeras n líneas.

    from itertools import islice

    with open('nombreArchivo', 'r') as file: 
    contentList = file.readlines()
    for i in range(len(contentList) + n), len(contentList):
        print(contentList[i])
        
    def imprimir_n(archivo, cantidad_de_lineas):
        with open(archivo, "r") as f:
            for linea in islice(f, cantidad_de_lineas):
                print(linea, end="")

##### **Ejercicio 3**
Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

        with open('nombreArchivo', 'r') as file: 
    contentList = file.readlines() 
    for i in range(len(contentList) - n), len(contentList): 
        print(contentList[i])

    def read_n_back_lines(n, archivo): 
    texto = open(archivo, "r").readlines()
    for i in range((len(texto) -n), len(texto)):
        print(texto[i])
    texto.close()
##### **Ejercicio 4**
Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

        with open('nombreArchivo', 'r') as file: 
            fileContent = file.readlines()
            print(len(fileContent)) 

##### **Ejercicio 5**
Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

        with open('nombreArchivo', 'r') as file: 
          fileContent = file.readlines()

        for fileline in fileContent: 
            fileline = fileline.replace('w', 'w \n')

        with open('otroArchivo', 'a') as f: 
          for i in fileContent:
             f.write(i) 

##### **Ejercicio 6**
Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

        def eliminar_saltos(entrada,salida):
            with open(entrada,"r") as f, open(salida,"w") as s:
        for line in f:
            s.write(line.strip("\n"))

##### **Ejercicio 7**
Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

        def palabra_mas_larga(archivo): 
            palabra = '' 
         max_long = 0
         with open(archivo, 'r') as f: 
                lista_palabra = f.read().split()
             for word in lista_palabra:
                  if len(word) > max_long: 
                       max_long = len(word)
            print(max_long) 

##### **Ejercicio 8**
Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

        def join_files(file1,file2,file3):
         with open(file1,"r") as f1, open (file2,"r") as f2, open(file3,"a") as f3:
             f3.write(f1.read() + f2.read())

##### **Ejercicio 9**
Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

        def word_counter(archivo): 
          frecuencias = dict() 
          with open(archivo, 'r') as miArchivo: 
                word_list = miArchivo.read().split() 
                for palabra in word_list:
                 if palabra in frecuencias: 
                      frecuencias[palabra] += 1
                    else: 
                     frecuencias[palabra] = 1 
             for word in frecuencias.keys(): 
                 frecuencias[word] = round(frecuencias[word] / len(word_list),3) #3 decimales 
            print(frecuencias) 

##### **Ejercicio 10**
Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.

        def join_files(file1, file2, file3): 
         with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'a') as f3: 
        f3.write(f1.read() + f2.read())

        join_files('documento1', 'documento2', 'documento3')
