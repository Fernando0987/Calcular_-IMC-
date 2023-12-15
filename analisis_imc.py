import matplotlib.pyplot as plt

# Datos de ejemplo de IMC
nombres = ['Usuario 1', 'Usuario 2', 'Usuario 3', 'Usuario 4', 'Usuario 5']
imc = [22, 25, 19, 30, 27]

# Crear el gráfico de barras
plt.bar(nombres, imc, color='skyblue')
plt.xlabel('Usuarios')
plt.ylabel('IMC')
plt.title('IMC de Usuarios')
plt.show()