class Cliente:
    # Dar a conocer los atributos de la clase cliente (privados)
    __DniCliente = ""
    __NombresCliente = ""
    __ApellidoPaternoCliente = ""
    __ApellidoMaternoCliente = ""
    __DireccionCliente = ""
    __TelefonoCliente = ""

    # Crear constructor e inicializar variables
    def __init__(self, dniCliente, nombresCliente, apellidoPaternoCliente, apellidoMaternoCliente, direccionCliente,
                 telefonoCliente):
        self.__DniCliente = dniCliente
        self.__NombresCliente = nombresCliente
        self.__ApellidoPaternoCliente = apellidoPaternoCliente
        self.__ApellidoMaternoCliente = apellidoMaternoCliente
        self.__DireccionCliente = direccionCliente
        self.__TelefonoCliente = telefonoCliente

    # Setters & getters
    def getNombresCliente(self):
        return self.__NombresCliente

    def setNombresCliente(self, NombresCliente):
        self.__NombresCliente = NombresCliente

    def getDniCliente(self):
        return self.__DniCliente

    def setDniCliente(self, DniCliente):
        self.__DniCliente = DniCliente

    def getApellidoMaternoCliente(self):
        return self.__ApellidoMaternoCliente

    def setApellidoMaternoCliente(self, ApellidoMaternoCliente):
        self.__ApellidoMaternoCliente = ApellidoMaternoCliente

    def getTelefonoCliente(self):
        return self.__TelefonoCliente

    def setTelefonoCliente(self, TelefonoCliente):
        self.__TelefonoCliente = TelefonoCliente

    def getApellidoPaternoCliente(self):
        return self.__ApellidoPaternoCliente

    def setApellidoPaternoCliente(self, ApellidoPaternoCliente):
        self.__ApellidoPaternoCliente = ApellidoPaternoCliente

    def getDireccionCliente(self):
        return self.__DireccionCliente

    def setDireccionCliente(self, DireccionCliente):
        self.__DireccionCliente = DireccionCliente