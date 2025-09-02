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

