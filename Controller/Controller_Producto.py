class Producto:
    #Atributos
    __Codigo = ""
    __Nombre = ""
    __Descripcion = ""
    __StockMinimo = 0
    __StockActual = 0
    __PrecioCosto = 0.0
    __PrecioVenta = 0.0
    __Proveedor = ""
    __Almacen = ""

    def __init__(self, codigo, nombre, descripcion, stockMinimo, stockActual, precioCosto, precioVenta, proveedor, almacen):
        self.__Codigo = codigo
        self.__Nombre = nombre
        self.__Descripcion = descripcion
        self.__StockMinimo = stockMinimo
        self.__StockActual = stockActual
        self.__PrecioCosto = precioCosto
        self.__PrecioVenta = precioVenta
        self.__Proveedor = proveedor
        self.__Almacen = almacen

    def getNombre(self):
        return self.__Nombre

    def setNombre(self, Nombre):
        self.__Nombre = Nombre

    def getPrecioCosto(self):
        return self.__PrecioCosto

    def setPrecioCosto(self, PrecioCosto):
        self.__PrecioCosto = PrecioCosto

    def getCodigo(self):
        return self.__Codigo

    def setCodigo(self, Codigo):
        self.__Codigo = Codigo

    def getProveedor(self):
        return self.__Proveedor

    def setProveedor(self, Proveedor):
        self.__Proveedor = Proveedor

    def getPrecioVenta(self):
        return self.__PrecioVenta

    def setPrecioVenta(self, PrecioVenta):
        self.__PrecioVenta = PrecioVenta

    def getStockMinimo(self):
        return self.__StockMinimo

    def setStockMinimo(self, StockMinimo):
        self.__StockMinimo = StockMinimo

    def getStockActual(self):
        return self.__StockActual

    def setStockActual(self, StockActual):
        self.__StockActual = StockActual

    def getDescripcion(self):
        return self.__Descripcion

    def setDescripcion(self, Descripcion):
        self.__Descripcion = Descripcion

    def getAlmacen(self):
        return self.__Almacen

    def setAlmacen(self, Almacen):
        self.__Almacen = Almacen