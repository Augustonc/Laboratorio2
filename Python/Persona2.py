#Esto fue lo que hicimos la última clase del martes 18/10

class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los: ', {self._nombre}, {self._apellido}, {self._edad})

    @property  # decorador
    def nombre(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Método Setter
        print('Estamos utilizando el metodo set')
        self.nombre = nombre


persona1 = Persona2('Ariel', 'Betancud', 41)
print(persona1.nombre)  # Llamamos al método getter
persona1.nombre = 'Juan Pedro'  # Llamamos al método setter
print(persona1.nombre)  # Otra vez con el método getter
print(persona1.mostrar_detalles())  # Llamamos el método mostrar_detalles
