# Programa para calcular la cantidad de personas necesarias para que 
# la probabilidad de que dos personas tengan el mismo cumpleaños de 0.5

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Función para calcular arreglos sin repetición
def arreglos_sin_repeticion(n, m):
    if m > n:
        return 0
    return factorial(n) // factorial(n - m)

# Función para calcular arreglos con repetición
def arreglos_con_repeticion(n, m):
    return n ** m

# Función para calcular combinaciones sin repetición
def combinaciones_sin_repeticion(n, m):
    if m > n:
        return 0
    return factorial(n) // (factorial(m) * factorial(n - m))

def mismo_cumple(num_personas):
    total_days = 365  # Número de días en un año
    total_posibilidades = arreglos_con_repeticion(total_days, num_personas)
    posibilidades_sin_repeticion = arreglos_sin_repeticion(total_days, num_personas)
    
    probabilidad_sin_repeticion = posibilidades_sin_repeticion / total_posibilidades
    probabilidad_mismo_cumple = 1 - probabilidad_sin_repeticion
    
    return probabilidad_mismo_cumple

# Funcion para hallar la cantidad minima de personas para que la probabilidad sea mayor a 0.5
def cantidad_minima_personas(probabilidad_objetivo):
    num_personas = 1
    while mismo_cumple(num_personas) < probabilidad_objetivo:
        num_personas += 1
    return num_personas

print("Cantidad mínima de personas para que la probabilidad de que dos tengan el mismo cumpleaños sea mayor a 0.5:", cantidad_minima_personas(0.5))