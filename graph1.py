import matplotlib.pyplot as plt

# Datos proporcionados
data = """
0:00:01.807844	22.937	23.562
0:00:03.567879	22.875	23.625
0:00:05.327835	22.937	23.687
0:00:07.087802	22.937	23.625
0:00:08.847816	22.937	23.625
0:00:10.607776	22.937	23.562
0:00:12.367813	22.937	23.625
0:00:14.127751	22.937	23.562
0:00:15.887751	22.937	23.562
0:00:17.647865	22.875	23.625
0:00:19.407747	22.875	23.562
0:00:21.167732	22.937	23.562
0:00:22.927749	22.937	23.562
0:00:24.687752	22.812	23.562
0:00:26.447825	22.937	23.625
0:00:28.207781	22.937	23.5
0:00:29.967750	22.937	23.625
0:00:31.727750	22.937	23.5
0:00:33.487746	22.937	23.5
"""

# Dividir las líneas y extraer las columnas relevantes
lines = data.strip().split('\n')
times = [float(line.split('\t')[0].split(':')[-1]) for line in lines]
values1 = [float(line.split('\t')[1]) for line in lines]
values2 = [float(line.split('\t')[2]) for line in lines]

# Crear el gráfico
plt.figure(figsize=(10, 6))

# Graficar las columnas relevantes
plt.plot(times, values1, label='Columna 2')
plt.plot(times, values2, label='Columna 3')

# Configurar el gráfico
plt.title('Gráfico de Datos')
plt.xlabel('Tiempo (s)')
plt.ylabel('Valores')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()

