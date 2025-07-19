# Basic Operations Calculator
# Requests two numbers and displays addition, subtraction, multiplication, and division
def main():
    print("------------------------------------------")
    print("Inicio del programa")
    print("------------------------------------------")
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
        return
    print("------------------------------------------")
    print(f"Suma: {num1} + {num2} = {num1 + num2}")
    print(f"Resta: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplicación: {num1} * {num2} = {num1 * num2}")
    if num2 != 0:
        print(f"División: {num1} / {num2} = {num1 / num2}")
    else:
        print("División: No se puede dividir entre cero.")
    
    print("------------------------------------------")
    print("Fin del programa")
    print("------------------------------------------")

if __name__ == "__main__":
    main()
