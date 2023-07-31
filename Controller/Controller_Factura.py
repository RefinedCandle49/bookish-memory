class Factura:
    __NumeroDocumento = ""
    __DniCliente = ""
    __DniEmpleado = ""
    __Fecha = ""
    __Estado = ""

    def __init__(self, nroDoc, dniCliente, dniEmpleado, fecha):
        self.__NumeroDocumento = nroDoc
        self.__DniCliente = dniCliente
        self.__DniEmpleado = dniEmpleado
        self.__Fecha = fecha

    def getDniCliente(self):
        return self.__DniCliente

    def setDniCliente(self, DniCliente):
        self.__DniCliente = DniCliente

    def getNumeroDocumento(self):
        return self.__NumeroDocumento

    def setNumeroDocumento(self, NumeroDocumento):
        self.__NumeroDocumento = NumeroDocumento

    def getDniEmpleado(self):
        return self.__DniEmpleado

    def setDniEmpleado(self, DniEmpleado):
        self.__DniEmpleado = DniEmpleado

    def getFecha(self):
        return self.__Fecha

    def setFecha(self, Fecha):
        self.__Fecha = Fecha

    def getEstado(self):
        return self.__Estado

    def setEstado(self, Estado):
        self.__Estado = Estado