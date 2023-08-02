from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from Controller.Mantenimiento_Proveedor import *
from Controller.Controller_Empleado import *

aProv = ArregloProveedor()

class VentanaProveedores(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super(VentanaProveedores, self).__init__(parent)
        uic.loadUi("UI/ventanaProveedores.ui", self)
        self.btnRegistrar.clicked.connect(self.registrar)
        self.listar()
        self.show()

    def obtenerDni(self):
        return self.txtDni.text()
    def obtenerRazSoc(self):
        return self.txtRazonSocial.text()
    def obtenerTelefono(self):
        return self.txtTelefono.text()
    def obtenerDireccion(self):
        return self.txtDireccion.text()
    def obtenerCategoria(self):
        return self.cboCategoria.currentText()

        # Procesos
    def listar(self):
        self.tblProveedores.setRowCount(aProv.tamañoArregloProveedor())
        self.tblProveedores.setColumnCount(5)
        self.tblProveedores.verticalHeader().setVisible(False)
        for i in range(0, aProv.tamañoArregloProveedor()):
            self.tblProveedores.setItem(i, 0,QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getDniProveedor()))
            self.tblProveedores.setItem(i, 1, QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getRazonSocial()))
            self.tblProveedores.setItem(i, 2, QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getTelefono()))
            self.tblProveedores.setItem(i, 3, QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getDireccion()))
            self.tblProveedores.setItem(i, 4, QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getCategoria()))

    def grabar(self):
        try:
            pos = aProv.buscarProveedor(self.obtenerDni())
            objPro = aProv.devolverProveedor(pos)
            objPro.setRazonSocial(self.obtenerRazSoc())
            objPro.setTelefono(self.obtenerTelefono())
            objPro.setDireccion(self.obtenerDireccion())
            objPro.setCategoria(self.obtenerCategoria())
            aProv.grabar()
            self.listar()
        except:
            QtWidgets.QMessageBox.information(self, "Registrar Proveedor", "Ha ocurrido un error al registrar al proveedor", QtWidgets.QMessageBox.Ok)

    def registrar(self):
        objPro = Proveedor(self.obtenerDni(), self.obtenerRazSoc(), self.obtenerTelefono(), self.obtenerDireccion(), self.obtenerCategoria())
        aProv.adicionaProveedor(objPro)
        aProv.grabar()
        self.listar()
        QtWidgets.QMessageBox.information(self, "Registrar Proveedor", "Proveedor registrado con con éxito", QtWidgets.QMessageBox.Ok)