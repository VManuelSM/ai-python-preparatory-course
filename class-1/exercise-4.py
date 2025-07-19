# Example of if statement
def main():
    print("------------------------------------------")
    print("Inicio del programa")
    print("------------------------------------------")
    try:
        age = float(input("Ingrese la edad en años: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
    if(age >= 18):
        print("Eres mayor de edad (:")
    else: 
        print("No eres mayor de edad ):")
    
    print("------------------------------------------")
    print("Fin del programa")
    print("------------------------------------------")

if __name__ == "__main__":
    main()
