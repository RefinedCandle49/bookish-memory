class Empleado:
    # Dar a conocer los atributos de la clase cliente (privados)
    __DniEmpleado = ""
    __NombresEmpleado = ""
    __ApellidoPaternoEmpleado = ""
    __ApellidoMaternoEmpleado = ""
    __DireccionEmpleado = ""
    __TelefonoEmpleado = ""

    # Crear constructor e inicializar variables
    def __init__(self, dniEmpleado, nombresEmpleado, apellidoPaternoEmpleado, apellidoMaternoEmpleado, direccionEmpleado,
                 telefonoEmpleado):
        self.__DniEmpleado = dniEmpleado
        self.__NombresEmpleado = nombresEmpleado
        self.__ApellidoPaternoEmpleado = apellidoPaternoEmpleado
        self.__ApellidoMaternoEmpleado = apellidoMaternoEmpleado
        self.__DireccionEmpleado = direccionEmpleado
        self.__TelefonoEmpleado = telefonoEmpleado

    # Setters & getters
    def getDireccionEmpleado(self):
        return self.__DireccionEmpleado

    def setDireccionEmpleado(self, DireccionEmpleado):
        self.__DireccionEmpleado = DireccionEmpleado

    def getNombresEmpleado(self):
        return self.__NombresEmpleado

    def setNombresEmpleado(self, NombresEmpleado):
        self.__NombresEmpleado = NombresEmpleado

    def getDniEmpleado(self):
        return self.__DniEmpleado

    def setDniEmpleado(self, DniEmpleado):
        self.__DniEmpleado = DniEmpleado

    def getApellidoMaternoEmpleado(self):
        return self.__ApellidoMaternoEmpleado

    def setApellidoMaternoEmpleado(self, ApellidoMaternoEmpleado):
        self.__ApellidoMaternoEmpleado = ApellidoMaternoEmpleado

    def getApellidoPaternoEmpleado(self):
        return self.__ApellidoPaternoEmpleado

    def setApellidoPaternoEmpleado(self, ApellidoPaternoEmpleado):
        self.__ApellidoPaternoEmpleado = ApellidoPaternoEmpleado

    def getTelefonoEmpleado(self):
        return self.__TelefonoEmpleado

    def setTelefonoEmpleado(self, TelefonoEmpleado):
        self.__TelefonoEmpleado = TelefonoEmpleado