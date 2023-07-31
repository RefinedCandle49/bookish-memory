from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from View.ventanaClientes import VentanaClientes
from View.ventanaEmpleados import VentanaEmpleados
from View.ventanaComprobante import VentanaComprobante
from View.ventanaProductos import VentanaProductos
from View.ventanaProveedores import VentanaProveedores


class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaPrincipal, self).__init__(parent)
        uic.loadUi("UI/ventanaPrincipal.ui", self)
        self.show()
    # Procesos
        self.actionClientes.triggered.connect(self.abrirVentanaClientes)
        self.actionEmpleados.triggered.connect(self.abrirVentanaEmpleados)
        self.actionVista_previa.triggered.connect(self.abrirVentanaComprobante)
        self.actionProductos.triggered.connect(self.abrirVentanaProductos)
        self.actionProveedor.triggered.connect(self.abrirVentanaProveedores)

    def abrirVentanaClientes(self):
        vcliente = VentanaClientes(self)
        vcliente.show()

    def abrirVentanaEmpleados(self):
        vempleado = VentanaEmpleados(self)
        vempleado.show()

    def abrirVentanaComprobante(self):
        vcomprobante = VentanaComprobante(self)
        vcomprobante.show()

    def abrirVentanaProductos(self):
        vproductos = VentanaProductos(self)
        vproductos.show()

    def abrirVentanaProveedores(self):
        vproveedor = VentanaProveedores(self)
        vproveedor.show()

    def cerrar(self):
        self.close()