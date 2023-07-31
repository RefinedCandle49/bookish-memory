class Proveedor():
    #Atributos
    __DniProveedor = ""
    __RazonSocial = ""
    __Telefono = ""
    __Direccion = ""
    __Categoria = ""

    #Constructor
    def __init__(self, dni, raz, tel, dir, cat):
        self.__DniProveedor = dni
        self.__RazonSocial = raz
        self.__Telefono = tel
        self.__Direccion = dir
        self.__Categoria = cat

    # Métodos de acceso público SET - GET
    def getRazonSocial(self):
        return self.__RazonSocial

    def setRazonSocial(self, RazonSocial):
        self.__RazonSocial = RazonSocial

    def getDniProveedor(self):
        return self.__DniProveedor

    def setDniProveedor(self, DniProveedor):
        self.__DniProveedor = DniProveedor

    def getCategoria(self):
        return self.__Categoria

    def setCategoria(self, Categoria):
        self.__Categoria = Categoria

    def getDireccion(self):
        return self.__Direccion

    def setDireccion(self, Direccion):
        self.__Direccion = Direccion

    def getTelefono(self):
        return self.__Telefono

    def setTelefono(self, Telefono):
        self.__Telefono = Telefono