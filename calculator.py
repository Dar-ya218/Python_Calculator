def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: No se puede dividir por cero"
    return x / y

while True:
    print("\nCalculadora Simple")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Elige una operación (1-5): ")
    
    if opcion == '5':
        print("¡Hasta luego!")
        break
        
    if opcion not in ('1', '2', '3', '4'):
        print("Opción no válida")
        continue
        
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    if opcion == '1':
        print(f"Resultado: {add(num1, num2)}")
    elif opcion == '2':
        print(f"Resultado: {subtract(num1, num2)}")
    elif opcion == '3':
        print(f"Resultado: {multiply(num1, num2)}")
    elif opcion == '4':
        print(f"Resultado: {divide(num1, num2)}")