from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from Controller.Mantenimiento_Proveedor import *

aProv = ArregloProveedor()

class VentanaProveedores(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super(VentanaProveedores, self).__init__(parent)
        uic.loadUi("UI/ventanaProveedores.ui", self)
        self.listar()
        self.show()

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