class DetalleFactura:
    __NroCom = ""
    __CodProducto = ""
    __NomProducto = ""
    __PrecioVenta = 0.0
    __Cant = 0

    def __init__(self, nroCom, codProducto, nomProducto, precioVenta, cant):
        self.__NroCom = nroCom
        self.__CodProducto = codProducto
        self.__NomProducto = nomProducto
        self.__PrecioVenta = precioVenta
        self.__Cant = cant

    def getCant(self):
        return self.__Cant

    def setCant(self, Cant):
        self.__Cant = Cant

    def getNroCom(self):
        return self.__NroCom

    def setNroCom(self, NroCom):
        self.__NroCom = NroCom

    def getNomProducto(self):
        return self.__NomProducto

    def setNomProducto(self, NomProducto):
        self.__NomProducto = NomProducto

    def getCodProducto(self):
        return self.__CodProducto

    def setCodProducto(self, CodProducto):
        self.__CodProducto = CodProducto

    def getPrecioVenta(self):
        return self.__PrecioVenta

    def setPrecioVenta(self, PrecioVenta):
        self.__PrecioVenta = PrecioVenta

