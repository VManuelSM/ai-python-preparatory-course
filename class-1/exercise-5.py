#Ask for a number from 1 to 7 and print the corresponding day.
# Example of if statement
def main():
    print("------------------------------------------")
    print("Inicio del programa")
    print("------------------------------------------")
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    num = int(input("Introduce un número del 1 al 7: "))
    if 1 <= num <= 7:
        print(f"El día correspondiente es: {days[num-1]}")
    else:
        print("Número fuera de rango. Debe ser entre 1 y 7.")
    print("------------------------------------------")
    print("Fin del programa")
    print("------------------------------------------")

if __name__ == "__main__":
    main()