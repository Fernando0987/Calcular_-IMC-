import matplotlib.pyplot as plt

# Definir los rangos de peso saludable
rangos = ['Bajo peso', 'Peso saludable', 'Sobrepeso', 'Obesidad']
limites = [18.5, 24.9, 29.9, 40]  # Estos son valores de IMC inventados para el ejemplo

# Crear el gráfico de barras para mostrar los rangos de peso
plt.bar(rangos, limites, color=['green', 'blue', 'yellow', 'red'])
plt.xlabel('Rangos de peso')
plt.ylabel('IMC')
plt.title('Rangos de peso saludable')
plt.axhline(y=18.5, color='r', linestyle='-')  # Línea roja para el límite de bajo peso
plt.axhline(y=24.9, color='r', linestyle='-')  # Línea roja para el límite de peso saludable
plt.axhline(y=29.9, color='r', linestyle='-')  # Línea roja para el límite de sobrepeso
plt.show()