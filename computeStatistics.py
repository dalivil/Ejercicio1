

import time

# Guarda el tiempo de inicio
inicio_tiempo = time.time()


TC1	= '/Users/dalinaaideevillaocelotl/Desktop/EjercicioProgramacion1/P1/TC1.txt'

try:
	contador_registrosTC1 = 0
	with open(TC1, 'r') as file:
	    for linea in file:
	        contador_registrosTC1 += 1

except Exception as e:
	print(f"Se ha producido un error en el proceso de conteo de registros: {e}")

### MEDIA TC1
try:
	suma = 0
	contador = 0

	with open(TC1, 'r') as file:
	    
	    for linea in file:
	        numero = float(linea)
	       
	        suma += numero
	        
	        contador += 1

	    mediaTC1 = suma / contador
	    

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la media: {e}")


# MEDIANA

try:
	numeros = []
	with open(TC1, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	numeros.sort()

	# Calcular la mediana
	n = len(numeros)
	if n % 2 == 0:
	    # Si la cantidad de números es par, calcular la mediana como el promedio de los dos valores centrales
	    medianaTC1 = (numeros[n // 2 - 1] + numeros[n // 2]) / 2
	else:
	    # Si la cantidad de números es impar, la mediana es el valor central
	    medianaTC1 = numeros[n // 2]

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la mediana: {e}")
	medianaTC1 = 0

# MODA
try:
	numeros = []
	with open(TC1, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	frecuencias = {}
	for numero in numeros:
	    if numero in frecuencias:
	        frecuencias[numero] += 1
	    else:
	        frecuencias[numero] = 1

	# Encontrar el número con la mayor frecuencia (moda)
	modaTC1 = max(frecuencias, key=frecuencias.get)

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la moda: {e}")

### VARIANZA

try:
	numeros = []
	with open(TC1, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	# Calcular la media
	media = sum(numeros) / len(numeros)

	# Calcular la suma de los cuadrados de las diferencias entre cada número y la media
	sum_cuadrados_diferencias = sum((numero - media)**2 for numero in numeros)

	# Calcular la varianza
	varianzaTC1 = sum_cuadrados_diferencias / len(numeros)
except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la moda: {e}")


### DESVIACION ESTANDAR
try:

	numeros = []
	with open(TC1, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	# Calcular la media
	media = sum(numeros) / len(numeros)

	# Calcular la suma de los cuadrados de las diferencias entre cada número y la media
	sum_cuadrados_diferencias = sum((numero - media)**2 for numero in numeros)

	# Calcular la varianza
	varianza = sum_cuadrados_diferencias / len(numeros)

	# Calcular la desviación estándar (raíz cuadrada de la varianza)
	desvEstandarTC1 = varianza**0.5

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la desviacionEstandar: {e}")

#####################################################


TC2	= '/Users/dalinaaideevillaocelotl/Desktop/EjercicioProgramacion1/P1/TC2.txt'

try:
	contador_registrosTC2 = 0

	with open(TC2, 'r') as file:
	    for linea in file:
	        contador_registrosTC2 += 1

except Exception as e:
	print(f"Se ha producido un error en el proceso de conteo de registros: {e}")

### MEDIA
try:
	suma = 0
	contador = 0

	with open(TC2, 'r') as file:
	    
	    for linea in file:
	        numero = float(linea)
	       
	        suma += numero
	        
	        contador += 1

	    mediaTC2 = suma / contador
	    
except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la media: {e}")

# MEDIANA
try:
	numeros = []
	with open(TC2, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	numeros.sort()

	# Calcular la mediana
	n = len(numeros)
	if n % 2 == 0:
	    # Si la cantidad de números es par, calcular la mediana como el promedio de los dos valores centrales
	    medianaTC2 = (numeros[n // 2 - 1] + numeros[n // 2]) / 2
	else:
	    # Si la cantidad de números es impar, la mediana es el valor central
	    medianaTC2 = numeros[n // 2]

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la mediana: {e}")

# MODA
try:
	numeros = []
	with open(TC2, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	frecuencias = {}
	for numero in numeros:
	    if numero in frecuencias:
	        frecuencias[numero] += 1
	    else:
	        frecuencias[numero] = 1

	# Encontrar el número con la mayor frecuencia (moda)
	modaTC2 = max(frecuencias, key=frecuencias.get)

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la moda: {e}")


### VARIANZA

try:
	numeros = []
	with open(TC2, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	# Calcular la media
	media = sum(numeros) / len(numeros)

	# Calcular la suma de los cuadrados de las diferencias entre cada número y la media
	sum_cuadrados_diferencias = sum((numero - media)**2 for numero in numeros)

	# Calcular la varianza
	varianzaTC2 = sum_cuadrados_diferencias / len(numeros)
except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la moda: {e}")


### DESVIACION ESTANDAR
try:

	numeros = []
	with open(TC2, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	# Calcular la media
	media = sum(numeros) / len(numeros)

	# Calcular la suma de los cuadrados de las diferencias entre cada número y la media
	sum_cuadrados_diferencias = sum((numero - media)**2 for numero in numeros)

	# Calcular la varianza
	varianza = sum_cuadrados_diferencias / len(numeros)

	# Calcular la desviación estándar (raíz cuadrada de la varianza)
	desvEstandarTC2 = varianza**0.5

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la desviacionEstandar: {e}")

############################# TC3


TC3	= '/Users/dalinaaideevillaocelotl/Desktop/EjercicioProgramacion1/P1/TC3.txt'

try:
	contador_registrosTC3 = 0

	# Leer los números del archivo y contar registros
	with open(TC3, 'r') as file:
	    for linea in file:
	        # Incrementar el contador de registros por cada línea
	        contador_registrosTC3 += 1

except Exception as e:
	print(f"Se ha producido un error en el proceso de conteo de registros: {e}")


### MEDIA
try:
	suma = 0
	contador = 0

	with open(TC3, 'r') as file:
	    
	    for linea in file:
	        numero = float(linea)
	       
	        suma += numero
	        
	        contador += 1

	    mediaTC3 = suma / contador
	    

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la media: {e}")
	mediaTC3 = "NA"

# MEDIANA
try:
	numeros = []
	with open(TC3, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	numeros.sort()

	# Calcular la mediana
	n = len(numeros)
	if n % 2 == 0:
	    # Si la cantidad de números es par, calcular la mediana como el promedio de los dos valores centrales
	    medianaTC3 = (numeros[n // 2 - 1] + numeros[n // 2]) / 2
	else:
	    # Si la cantidad de números es impar, la mediana es el valor central
	    medianaTC3 = numeros[n // 2]

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la mediana: {e}")

# MODA
try:
	numeros = []
	with open(TC3, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	frecuencias = {}
	for numero in numeros:
	    if numero in frecuencias:
	        frecuencias[numero] += 1
	    else:
	        frecuencias[numero] = 1

	# Encontrar el número con la mayor frecuencia (moda)
	modaTC3 = max(frecuencias, key=frecuencias.get)

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la moda: {e}")


### VARIANZA
try:
	numeros = []
	with open(TC3, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	# Calcular la media
	media = sum(numeros) / len(numeros)

	# Calcular la suma de los cuadrados de las diferencias entre cada número y la media
	sum_cuadrados_diferencias = sum((numero - media)**2 for numero in numeros)

	# Calcular la varianza
	varianzaTC3 = sum_cuadrados_diferencias / len(numeros)
except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la moda: {e}")


### DESVIACION ESTANDAR
try:

	numeros = []
	with open(TC3, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	# Calcular la media
	media = sum(numeros) / len(numeros)

	# Calcular la suma de los cuadrados de las diferencias entre cada número y la media
	sum_cuadrados_diferencias = sum((numero - media)**2 for numero in numeros)

	# Calcular la varianza
	varianza = sum_cuadrados_diferencias / len(numeros)

	# Calcular la desviación estándar (raíz cuadrada de la varianza)
	desvEstandarTC3 = varianza**0.5

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la desviacionEstandar: {e}")

#######################################


TC4	= '/Users/dalinaaideevillaocelotl/Desktop/EjercicioProgramacion1/P1/TC4.txt'

try:
	contador_registrosTC4 = 0

	# Leer los números del archivo y contar registros
	with open(TC4, 'r') as file:
	    for linea in file:
	        # Incrementar el contador de registros por cada línea
	        contador_registrosTC4 += 1

except Exception as e:
	print(f"Se ha producido un error en el proceso de conteo de registros: {e}")

### MEDIA
try:
	suma = 0
	contador = 0

	with open(TC4, 'r') as file:
	    
	    for linea in file:
	        numero = float(linea)
	       
	        suma += numero
	        
	        contador += 1

	    mediaTC4 = suma / contador
	    
except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la media: {e}")
	mediaTC4 = "NA"

# MEDIANA
try:
	numeros = []
	with open(TC4, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	numeros.sort()

	# Calcular la mediana
	n = len(numeros)
	if n % 2 == 0:
	    # Si la cantidad de números es par, calcular la mediana como el promedio de los dos valores centrales
	    medianaTC4 = (numeros[n // 2 - 1] + numeros[n // 2]) / 2
	else:
	    # Si la cantidad de números es impar, la mediana es el valor central
	    medianaTC4 = numeros[n // 2]

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la mediana: {e}")

# MODA
try:
	numeros = []
	with open(TC4, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	frecuencias = {}
	for numero in numeros:
	    if numero in frecuencias:
	        frecuencias[numero] += 1
	    else:
	        frecuencias[numero] = 1

	# Encontrar el número con la mayor frecuencia (moda)
	modaTC4 = max(frecuencias, key=frecuencias.get)

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la moda: {e}")


### VARIANZA
try:
	numeros = []
	with open(TC4, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	# Calcular la media
	media = sum(numeros) / len(numeros)

	# Calcular la suma de los cuadrados de las diferencias entre cada número y la media
	sum_cuadrados_diferencias = sum((numero - media)**2 for numero in numeros)

	# Calcular la varianza
	varianzaTC4 = sum_cuadrados_diferencias / len(numeros)
except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la moda: {e}")


### DESVIACION ESTANDAR
try:

	numeros = []
	with open(TC4, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	# Calcular la media
	media = sum(numeros) / len(numeros)

	# Calcular la suma de los cuadrados de las diferencias entre cada número y la media
	sum_cuadrados_diferencias = sum((numero - media)**2 for numero in numeros)

	# Calcular la varianza
	varianza = sum_cuadrados_diferencias / len(numeros)

	# Calcular la desviación estándar (raíz cuadrada de la varianza)
	desvEstandarTC4 = varianza**0.5

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la desviacionEstandar: {e}")

######################################################################


TC5	= '/Users/dalinaaideevillaocelotl/Desktop/EjercicioProgramacion1/P1/TC5.txt'

try:
	contador_registrosTC5 = 0

	with open(TC5, 'r') as file:
	    for linea in file:
	        contador_registrosTC5 += 1

except Exception as e:
	print(f"Se ha producido un error en el proceso de conteo de registros: {e}")

mediaTC5 = None
### MEDIA
try:
	suma = 0
	contador = 0

	with open(TC5, 'r') as file:
	    
	    for linea in file:
	        numero = float(linea)
	       
	        suma += numero
	        
	        contador += 1

	    mediaTC5 = suma / contador
	    
except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la media: {e}")
	mediaTC5 = "NA"

# MEDIANA
medianaTC5 = None
try:
	numeros = []
	with open(TC5, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	numeros.sort()

	# Calcular la mediana
	n = len(numeros)
	if n % 2 == 0:
	    # Si la cantidad de números es par, calcular la mediana como el promedio de los dos valores centrales
	    medianaTC5= (numeros[n // 2 - 1] + numeros[n // 2]) / 2
	else:
	    # Si la cantidad de números es impar, la mediana es el valor central
	    medianaTC5 = numeros[n // 2]

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la mediana: {e}")

# MODA
modaTC5 = None
try:
	numeros = []
	with open(TC5, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	frecuencias = {}
	for numero in numeros:
	    if numero in frecuencias:
	        frecuencias[numero] += 1
	    else:
	        frecuencias[numero] = 1

	# Encontrar el número con la mayor frecuencia (moda)
	modaTC5= max(frecuencias, key=frecuencias.get)

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la moda: {e}")


### VARIANZA
varianzaTC5 = None
try:
	numeros = []
	with open(TC5, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	# Calcular la media
	media = sum(numeros) / len(numeros)

	# Calcular la suma de los cuadrados de las diferencias entre cada número y la media
	sum_cuadrados_diferencias = sum((numero - media)**2 for numero in numeros)

	# Calcular la varianza
	varianzaTC5 = sum_cuadrados_diferencias / len(numeros)
except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la moda: {e}")


### DESVIACION ESTANDAR
desvEstandarTC5 = None
try:

	numeros = []
	with open(TC5, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	# Calcular la media
	media = sum(numeros) / len(numeros)

	# Calcular la suma de los cuadrados de las diferencias entre cada número y la media
	sum_cuadrados_diferencias = sum((numero - media)**2 for numero in numeros)

	# Calcular la varianza
	varianza = sum_cuadrados_diferencias / len(numeros)

	# Calcular la desviación estándar (raíz cuadrada de la varianza)
	desvEstandarTC5 = varianza**0.5

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la desviacionEstandar: {e}")


##########################################################################

TC6	= '/Users/dalinaaideevillaocelotl/Desktop/EjercicioProgramacion1/P1/TC6.txt'

try:
	contador_registrosTC6 = 0

	# Leer los números del archivo y contar registros
	with open(TC6, 'r') as file:
	    for linea in file:
	        # Incrementar el contador de registros por cada línea
	        contador_registrosTC6 += 1

except Exception as e:
	print(f"Se ha producido un error en el proceso de conteo de registros: {e}")


### MEDIA
try:
	suma = 0
	contador = 0

	with open(TC6, 'r') as file:
	    
	    for linea in file:
	        numero = float(linea)
	       
	        suma += numero
	        
	        contador += 1

	    mediaTC6 = suma / contador
	    
except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la media: {e}")
	mediaTC6 = "NA"

# MEDIANA
try:
	numeros = []
	with open(TC6, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	numeros.sort()

	# Calcular la mediana
	n = len(numeros)
	if n % 2 == 0:
	    # Si la cantidad de números es par, calcular la mediana como el promedio de los dos valores centrales
	    medianaTC6= (numeros[n // 2 - 1] + numeros[n // 2]) / 2
	else:
	    # Si la cantidad de números es impar, la mediana es el valor central
	    medianaTC6 = numeros[n // 2]

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la mediana: {e}")

# MODA
try:
	numeros = []
	with open(TC6, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	frecuencias = {}
	for numero in numeros:
	    if numero in frecuencias:
	        frecuencias[numero] += 1
	    else:
	        frecuencias[numero] = 1

	# Encontrar el número con la mayor frecuencia (moda)
	modaTC6= max(frecuencias, key=frecuencias.get)

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la moda: {e}")


### VARIANZA
try:
	numeros = []
	with open(TC6, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	# Calcular la media
	media = sum(numeros) / len(numeros)

	# Calcular la suma de los cuadrados de las diferencias entre cada número y la media
	sum_cuadrados_diferencias = sum((numero - media)**2 for numero in numeros)

	# Calcular la varianza
	varianzaTC6 = sum_cuadrados_diferencias / len(numeros)
except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la moda: {e}")


### DESVIACION ESTANDAR
try:

	numeros = []
	with open(TC6, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	# Calcular la media
	media = sum(numeros) / len(numeros)

	# Calcular la suma de los cuadrados de las diferencias entre cada número y la media
	sum_cuadrados_diferencias = sum((numero - media)**2 for numero in numeros)

	# Calcular la varianza
	varianza = sum_cuadrados_diferencias / len(numeros)

	# Calcular la desviación estándar (raíz cuadrada de la varianza)
	desvEstandarTC6 = varianza**0.5

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la desviacionEstandar: {e}")


#####################################################


TC7	= '/Users/dalinaaideevillaocelotl/Desktop/EjercicioProgramacion1/P1/TC7.txt'

try:
	contador_registrosTC7 = 0

	with open(TC7, 'r') as file:
	    for linea in file:
	       
	        contador_registrosTC7 += 1
except Exception as e:
	print(f"Se ha producido un error en el proceso de conteo de registros: {e}")



### MEDIA
mediaTC7 = None
try:
	suma = 0
	contador = 0

	with open(TC7, 'r') as file:
	    
	    for linea in file:
	        numero = float(linea)
	       
	        suma += numero
	        
	        contador += 1

	    mediaTC7 = suma / contador
	    

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la media: {e}")
	mediaTC7 = "NA"


# MEDIANA
medianaTC7 = None
try:
	numeros = []
	with open(TC7, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	numeros.sort()

	# Calcular la mediana
	n = len(numeros)
	if n % 2 == 0:
	    # Si la cantidad de números es par, calcular la mediana como el promedio de los dos valores centrales
	    medianaTC7= (numeros[n // 2 - 1] + numeros[n // 2]) / 2
	else:
	    # Si la cantidad de números es impar, la mediana es el valor central
	    medianaTC7= numeros[n // 2]

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la mediana: {e}")

# MODA
modaTC7 = None
try:
	numeros = []
	with open(TC7, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	frecuencias = {}
	for numero in numeros:
	    if numero in frecuencias:
	        frecuencias[numero] += 1
	    else:
	        frecuencias[numero] = 1

	# Encontrar el número con la mayor frecuencia (moda)
	modaTC7= max(frecuencias, key=frecuencias.get)

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la moda: {e}")


### VARIANZA
varianzaTC7 = None
try:
	numeros = []
	with open(TC7, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	# Calcular la media
	media = sum(numeros) / len(numeros)

	# Calcular la suma de los cuadrados de las diferencias entre cada número y la media
	sum_cuadrados_diferencias = sum((numero - media)**2 for numero in numeros)

	# Calcular la varianza
	varianzaTC7 = sum_cuadrados_diferencias / len(numeros)
except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la moda: {e}")


### DESVIACION ESTANDAR
desvEstandarTC7 = None
try:

	numeros = []
	with open(TC7, 'r') as file:
	    for linea in file:
	        numero = float(linea)
	        numeros.append(numero)

	# Calcular la media
	media = sum(numeros) / len(numeros)

	# Calcular la suma de los cuadrados de las diferencias entre cada número y la media
	sum_cuadrados_diferencias = sum((numero - media)**2 for numero in numeros)

	# Calcular la varianza
	varianza = sum_cuadrados_diferencias / len(numeros)

	# Calcular la desviación estándar (raíz cuadrada de la varianza)
	desvEstandarTC7 = varianza**0.5

except Exception as e:
	print(f"Se ha producido un error en el proceso de obtencion de la desviacionEstandar: {e}")
################################################################################

archivo_resultados = '/Users/dalinaaideevillaocelotl/Desktop/EjercicioProgramacion1/P1/StatisticsResults.txt'

# Guarda el tiempo de finalización
fin_tiempo = time.time()

# Calcula la diferencia para obtener el tiempo total de ejecución
tiempo_total = fin_tiempo - inicio_tiempo

# Imprime el tiempo de ejecución
print(f"Tiempo de ejecución: {tiempo_total} segundos")

# Escribir los resultados en el nuevo archivo
with open(archivo_resultados, 'w') as resultado_file:
	resultado_file.write(f"TC\tTC1\tTC2\tTC3\tTC4\tTC5\tTC6\tTC7\n")
	resultado_file.write(f"COUNT\t{contador_registrosTC1}\t{contador_registrosTC2}\t{contador_registrosTC3}\t{contador_registrosTC4}\t{contador_registrosTC5}\t{contador_registrosTC6}\t{contador_registrosTC7}\n")
	resultado_file.write(f"MEAN\t{mediaTC1}\t{mediaTC2}\t{mediaTC3}\t{mediaTC4}\t{mediaTC5}\t{mediaTC6}\t{mediaTC7}\n")
	resultado_file.write(f"MEDIAN\t{medianaTC1}\t{medianaTC2}\t{medianaTC3}\t{medianaTC4}\t{medianaTC5}\t{medianaTC6}\t{medianaTC7}\n")
	resultado_file.write(f"MODE\t{modaTC1}\t{modaTC2}\t{modaTC3}\t{modaTC4}\t{modaTC5}\t{modaTC6}\t{modaTC7}\n")
	resultado_file.write(f"SD\t{desvEstandarTC1}\t{desvEstandarTC2}\t{desvEstandarTC3}\t{desvEstandarTC4}\t{desvEstandarTC5}\t{desvEstandarTC6}\t{desvEstandarTC7}\n")
	resultado_file.write(f"VARIANCE\t{varianzaTC1}\t{varianzaTC2}\t{varianzaTC3}\t{varianzaTC4}\t{varianzaTC5}\t{varianzaTC6}\t{varianzaTC7}\n")
	resultado_file.write(f"Total time\t{tiempo_total}\n")
	
print(f"Los resultados se han guardado en el archivo '{archivo_resultados}'.")


