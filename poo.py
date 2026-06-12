from abc import ABC, abstractmethod
class Mascota(ABC):
    def __init__(self, nombre, edad, peso):
        self._nombre = nombre
        self._edad = edad
        self._peso = peso
        self._adoptado = False
    def get_nombre(self):
        return self._nombre
    def is_adoptado(self):
        return self._adoptado
    def set_adoptado(self, estado):
        self._adoptado = estado

    @abstractmethod
    def hacer_sonido(self):
        pass
    def obtener_datos(self):
        estado = "Adoptado" if self._adoptado else "Disponible"
        return f"Nombre: {self._nombre} | Edad: {self._edad} años | Peso: {self._peso}kg | Estado: {estado}"
    
class Perro(Mascota):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self._raza = raza 

    def hacer_sonido(self):
        return "Guau Guau"
    def obtener_datos(self):
        return super().obtener_datos() + f" | Tipo: Perro ({self._raza})"
    #El super trae el texto con los datos básicos de la Mascota.
        #El '+' une ese texto base con el nuevo texto
        #La 'f' permite incrustar la variable {self._raza} directamente dentro de las comillas.

class Gato(Mascota):
    def __init__(self, nombre, edad, peso, color):
        super().__init__(nombre, edad, peso)
        self._color = color

    def hacer_sonido(self):
        return "Miau Miau"
    def obtener_datos(self):
        return super().obtener_datos() + f" | Tipo: Gato ({self._color})"
    #Aquí se hace lo mismo que en Perro pero en vez de mostrar la raza muestra el color del pelaje del gato.

class Adoptante:
    def __init__(self, nombre, rut, telefono):
        self._nombre = nombre
        self._rut = rut
        self._telefono = telefono
    def get_nombre(self):
        return self._nombre
    def obtener_datos(self):
        return f"Adoptante: {self._nombre} | RUT: {self._rut} | Teléfono: {self._telefono}"
    #Esta clase es para representar a las personas que quieren adoptar esta tiene un método para mostrar sus datos aunque en este programa no se usa mucho, pero podría ser útil si queremos mostrar información de los adoptantes en el futuro.
    
class CentroAdopcion:
    def __init__(self):
        self.lista_mascotas = []
        self.lista_adoptantes = []
    def registrar_mascota(self, mascota):
        self.lista_mascotas.append(mascota)
        print(f"{mascota.get_nombre()} entró al registro de mascotas.")
    def registrar_adoptante(self, adoptante):
        self.lista_adoptantes.append(adoptante)
        print(f"El adoptante {adoptante.get_nombre()} fue registrado.")
    def mostrar_mascotas(self):
        if not self.lista_mascotas:
            print("No hay mascotas registradas por ahora.")
            return
        print("Lista de mascotas:")
        for i, mascota in enumerate(self.lista_mascotas, 1):
            print(f"{i}. {mascota.obtener_datos()}")
            # Aquí se muestra la lista de mascotas registradas. Si no hay ninguna, se muestra un mensaje indicando que no hay mascotas disponibles. Si hay mascotas, se enumeran con su información detallada.

    def procesar_adopcion(self, nombre_mascota):
        for mascota in self.lista_mascotas:
            if mascota.get_nombre().lower() == nombre_mascota.lower():
                if mascota.is_adoptado():
                    print("Esta mascota ya fue adoptada por otra familia.")
                    return
                mascota.set_adoptado(True)
                print(f"Felicidades, {mascota.get_nombre()} se va contigo. Escucha: {mascota.hacer_sonido()}")
                return
        print("No encontramos ninguna mascota con ese nombre.")
#El método 'procesar_adopcion' busca una mascota por su nombre. Si la encuentra y no ha sido adoptada, marca la mascota como adoptada y muestra un mensaje de felicitación junto con el sonido que hace la mascota. Si la mascota ya fue adoptada, informa al usuario. Si no se encuentra ninguna mascota con ese nombre, también se informa al usuario.
def menu():
    centro = CentroAdopcion()
    centro.registrar_mascota(Perro("Kerry", 3, 12.5, "chihuaha"))
    centro.registrar_mascota(Gato("Capija", 2, 4.2, "naranja"))
    while True:
        print("Centro de adopción:")
        print("1. Registrar un perro")
        print("2. Registrar un gato")
        print("3. Registrar un adoptante")
        print("4. Ver mascotas")
        print("5. Adoptar una mascota")
        print("6. Salir")
        opcion = input("Elige una opción (1-6): ")
        if opcion == "1":
            nombre = input("Nombre del perro: ")
            edad = int(input("Edad: "))
            peso = float(input("Peso (kg): "))
            raza = input("Raza: ")
            centro.registrar_mascota(Perro(nombre, edad, peso, raza))
        elif opcion == "2":
            nombre = input("Nombre del gato: ")
            edad = int(input("Edad: "))
            peso = float(input("Peso (kg): "))
            color = input("Color de pelaje: ")
            centro.registrar_mascota(Gato(nombre, edad, peso, color))      
        elif opcion == "3":
            nombre = input("Nombre del adoptante: ")
            rut = input("RUT: ")
            telefono = input("Teléfono: ")
            centro.registrar_adoptante(Adoptante(nombre, rut, telefono))
        elif opcion == "4":
            centro.mostrar_mascotas()
        elif opcion == "5":
            nombre_m = input("¿A quién quieres adoptar? Escribe el nombre: ")
            centro.procesar_adopcion(nombre_m)
        elif opcion == "6":
            print("Cerrando el sistema.")
            break
        else:
            print("Opción no válida. Elige un número del 1 al 6.")
            #Este menú permite al usuario interactuar con el sistema de adopción así el usuario puede registrar perros, gatos y adoptantes, ver la lista de mascotas disponibles y procesar adopciones cabe aclarar que el programa se ejecuta en un bucle hasta que el usuario decide salir
            #Cada opción del menú corresponde a una acción específica que el usuario puede realizar, y se manejan las entradas del usuario para crear objetos de las clases correspondientes y llamar a los métodos adecuados del centro de adopción.
            #