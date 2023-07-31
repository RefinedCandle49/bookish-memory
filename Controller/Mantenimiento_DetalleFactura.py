from Controller.Controller_DetalleFactura import *

class ArregloDetalleFactura:

    def __init__(self):
        self.dataDetalleFactura = []

    def adicionaFactura(self, objDetFact):
        self.dataDetalleFactura.append(objDetFact)

    def devolverDetalleFactura(self, pos):
        return self.dataDetalleFactura[pos]

    def tamañoDetalleFactura(self):
        return len(self.dataDetalleFactura)

    def buscarDetalleFactura(self, nDocumentoFactura):
        for i in range(self.tamañoDetalleFactura()):
            if nDocumentoFactura == self.dataDetalleFactura[i].getNroCom():
                return i
        return -1

    def eliminarDetalleFactura(self, indice):
        del(self.dataDetalleFactura[indice])
