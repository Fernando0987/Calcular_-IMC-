# Programa para calcular el índice de masa corporal (IMC)

# Solicitar al usuario que ingrese su peso en kilogramos
peso = float(input("Ingresa tu peso en kilogramos: "))

# Solicitar al usuario que ingrese su altura en metros
altura = float(input("Ingresa tu altura en metros: "))

# Solicitar al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# Solicitar al usuario que ingrese su género (M o F)
genero = input("Ingresa tu género (M o F): ")

# Solicitar al usuario que ingrese su nivel de actividad física (sedentario, moderado, activo)
nivel_actividad = input("Ingresa tu nivel de actividad física (sedentario, moderado, activo): ")

# Calcular el IMC
imc = peso / (altura ** 2)

# Mostrar el resultado
print("Tu índice de masa corporal es:", imc)

# Proporcionar recomendaciones personalizadas según el IMC y otros factores
if imc < 18.5:
    print("Tu IMC indica que estás en la categoría de bajo peso.")
    print("Recomendaciones: Aumenta tu ingesta calórica y haz ejercicio para ganar peso de manera saludable.")
elif 18.5 <= imc < 25:
    print("¡Tu IMC está en el rango de peso saludable!")
    print("Recomendaciones: Mantén una dieta equilibrada y haz ejercicio regularmente para mantener tu peso saludable.")
elif 25 <= imc < 30:
    print("Tu IMC indica que estás en la categoría de sobrepeso.")
    print("Recomendaciones: Reduce tu ingesta calórica y haz ejercicio regularmente para perder peso de manera saludable.")
else:
    print("Tu IMC indica que estás en la categoría de obesidad.")
    print("Recomendaciones: Reduce tu ingesta calórica y haz ejercicio regularmente para perder peso de manera saludable.")

# Proporcionar recomendaciones adicionales según la edad, género y nivel de actividad física
if edad >= 18:
    if genero == 'M':
        if nivel_actividad == 'sedentario':
            print("Recomendaciones adicionales: Consume al menos 2,500 calorías al día y haz ejercicio moderado durante al menos 30 minutos al día.")
        elif nivel_actividad == 'moderado':
            print("Recomendaciones adicionales: Consume al menos 2,500 calorías al día y haz ejercicio moderado durante al menos 60 minutos al día.")
        elif nivel_actividad == 'activo':
            print("Recomendaciones adicionales: Consume al menos 2,500 calorías al día y haz ejercicio vigoroso durante al menos 60 minutos al día.")
    elif genero == 'F':
        if nivel_actividad == 'sedentario':
            print("Recomendaciones adicionales: Consume al menos 2,000 calorías al día y haz ejercicio moderado durante al menos 30 minutos al día.")
        elif nivel_actividad == 'moderado':
            print("Recomendaciones adicionales: Consume al menos 2,000 calorías al día y haz ejercicio moderado durante al menos 60 minutos al día.")
        elif nivel_actividad == 'activo':
            print("Recomendaciones adicionales: Consume al menos 2,000 calorías al día y haz ejercicio vigoroso durante al menos 60 minutos al día.")
else:
    print("Recomendaciones adicionales: Consulta a un médico o nutricionista para obtener recomendaciones personalizadas según tu edad.")
    
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

# Datos de ejemplo de IMC
nombres = ['Usuario', 'Promedio']
imc_usuarios = [imc, 24]  # El 24 es un valor de IMC promedio inventado

# Crear el gráfico de barras
plt.bar(nombres, imc_usuarios, color=['blue', 'red'])
plt.xlabel('IMC')
plt.ylabel('Valor')
plt.title('Comparación de IMC')
plt.show()