class Automovil:
    """Clase que representa un Automóvil con atributos básicos."""
    
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    # Getters
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_anio(self):
        return self.__año

    # Setters
    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_anio(self, año):
        self.__año = año

    def __str__(self):
        return f"{self.__marca} {self.__modelo} ({self.__año})"


# ADT Estático: Lista con tamaño fijo
class AutomovilEstatico:
    """Clase con una estructura estática para almacenar automóviles."""
    
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.autos = [None] * capacidad  # Lista con tamaño fijo
        self.contador = 0

    def agregar_auto(self, auto):
        """Agrega un automóvil a la estructura si hay espacio disponible."""
        if self.contador < self.capacidad:
            self.autos[self.contador] = auto
            self.contador += 1
        else:
            print("No se pueden agregar más autos (capacidad llena).")

    def mostrar_autos(self):
        """Muestra los automóviles almacenados."""
        for auto in self.autos:
            if auto:
                print(auto)

class AutomovilDinamico:
    """Clase con una estructura dinámica para almacenar automóviles."""
    
    def __init__(self):
        self.autos = []  # Lista dinámica

    def agregar_auto(self, auto):
        """Agrega un automóvil a la estructura sin restricciones de tamaño."""
        self.autos.append(auto)

    def mostrar_autos(self):
        """Muestra los automóviles almacenados."""
        for auto in self.autos:
            print(auto)


if __name__ == "__main__":
    print("---- Estructura Estática ----")
    autos_estaticos = AutomovilEstatico(3)
    autos_estaticos.agregar_auto(Automovil("Toyota", "Corolla", 2022))
    autos_estaticos.agregar_auto(Automovil("Ford", "Focus", 2021))
    autos_estaticos.agregar_auto(Automovil("Honda", "Civic", 2023))
    autos_estaticos.mostrar_autos()

    print("\n---- Estructura Dinámica ----")
    autos_dinamicos = AutomovilDinamico()
    autos_dinamicos.agregar_auto(Automovil("Nissan", "Versa", 2020))
    autos_dinamicos.agregar_auto(Automovil("Chevrolet", "Onix", 2021))
    autos_dinamicos.agregar_auto(Automovil("Mazda", "3", 2022))
    autos_dinamicos.mostrar_autos()
