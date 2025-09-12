def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Colaborador 1: Añadir Kelvin a Celsius
def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

# Colaborador 2: Añadir Celsius a Kelvin
def celsius_a_kelvin(celsius):
    return celsius + 273.15

# Colaborador 3: Añadir Fahrenheit a Kelvin
def fahrenheit_a_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

# Colaborador 4: Añadir Kelvin a Fahrenheit
def kelvin_a_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Colaborador 5: Añadir Fahrenheit a Celsius y Kelvin en una sola salida
def fahrenheit_completo(fahrenheit):
    return (fahrenheit - 32) * 5/9, (fahrenheit - 32) * 5/9 + 273.15

# Colaborador 6: Añadir Celsius a Fahrenheit y Kelvin en una sola salida
def celsius_completo(celsius):
    return celsius * 9/5 + 32, celsius + 273.15


if __name__ == "__main__":
    # Conversación 1
    temp_c = float(input("Introduce la temperatura en Celsius: "))
    print(f"{temp_c}°C son {celsius_a_fahrenheit(temp_c)}°F")
    print(f"{temp_c}°C son {celsius_a_kelvin(temp_c)}K")

    # Conversación 2
    temp_f = float(input("\nIntroduce la temperatura en Fahrenheit: "))
    print(f"{temp_f}°F son {fahrenheit_a_celsius(temp_f)}°C")
    print(f"{temp_f}°F son {fahrenheit_a_kelvin(temp_f)}K")

    # Conversación 3
    temp_k = float(input("\nIntroduce la temperatura en Kelvin: "))
    print(f"{temp_k}K son {kelvin_a_celsius(temp_k)}°C")
    print(f"{temp_k}K son {kelvin_a_fahrenheit(temp_k)}°F")

    # Conversación 4 extra (Colaborador 5)
    temp_f2 = float(input("\nIntroduce otra temperatura en Fahrenheit: "))
    c, k = fahrenheit_completo(temp_f2)
    print(f"{temp_f2}°F equivalen a {c}°C y {k}K")

    # Conversación 5 extra (Colaborador 6)
    temp_c2 = float(input("\nIntroduce otra temperatura en Celsius: "))
    f, k = celsius_completo(temp_c2)
    print(f"{temp_c2}°C equivalen a {f}°F y {k}K")