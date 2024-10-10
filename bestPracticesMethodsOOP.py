class Alumno:
    def __init__(self):
        # Crea la función constructor con atributos vacíos
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None

    # Método para asignar todos los valores de una vez
    def set_datos(self, nombre, apellido_paterno, apellido_materno, no_control, semestre):
        self.set_nombre(nombre)
        self.set_apellido_paterno(apellido_paterno)
        self.set_apellido_materno(apellido_materno)
        self.set_no_control(no_control)
        self.set_semestre(semestre)

    # Métodos para asignar valores (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener los valores (getters)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre

    # Nombre completo
    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido_paterno} {self.__apellido_materno}"


# Ejemplo de uso
#Crea la instancia de alumno
#Una instancia es la creacion de un objeto a partir de una clase
# alumno.nombre("Victor") esto es incorecto ya que lo está llamando como si fuera público
alumno = Alumno()

# Asignar valores utilizando el método set_datos
alumno.set_datos("Juan", "Pérez", "García", "12345", "3")

# Obtener valores usando los getters
print("Nombre:", alumno.get_nombre())  # Juan
print("Apellido paterno:", alumno.get_apellido_paterno())  # Pérez
print("Apellido materno:", alumno.get_apellido_materno())  # García
print("Nombre completo:", alumno.get_nombre_completo())  # Juan Pérez García
print("Número de control:", alumno.get_no_control())  # 12345
print("Semestre:", alumno.get_semestre())  # 3

# Diccionario para almacenar los alumnos
registro_alumnos = {}

for i in range(3):
    print(f"\nCapturando datos del alumno {i + 1}:")

    alumno = Alumno()  # Crear una nueva instancia de Alumno

    # Utilizar el método set_datos para capturar los datos de un alumno
    nombre = input("Ingresa el nombre: ")
    apellido_paterno = input("Ingresa el apellido paterno: ")
    apellido_materno = input("Ingresa el apellido materno: ")
    no_control = input("Ingresa el número de control: ")
    semestre = int(input("Ingresa el semestre: "))

    alumno.set_datos(nombre, apellido_paterno, apellido_materno, no_control, semestre)

    # Guardar en el diccionario de alumnos usando el número de registro como clave
    registro_alumnos[i] = {
        "nombre": alumno.get_nombre_completo(),
        "semestre": alumno.get_semestre()
    }

# Mostrar el registro de alumnos
print("\nRegistro de alumnos:")
for registro, datos in registro_alumnos.items():
    print(f"Registro: {registro} - Nombre: {datos['nombre']} (Semestre: {datos['semestre']})")