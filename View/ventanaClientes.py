from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from Controller.Mantenimiento_Cliente import ArregloClientes
from Controller.Controller_Cliente import *

aCli = ArregloClientes()

class VentanaClientes(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super(VentanaClientes, self).__init__(parent)
        uic.loadUi("UI/ventanaClientes.ui", self)
        # self.btnListar.clicked.connect(self.ListarDatos)
        self.btnRegistrar.clicked.connect(self.registrar)
        self.listar()
        self.show()

    def obtenerDni(self):
        return self.txtDni.text()
    def obtenerNombres(self):
        return self.txtNombres.text()
    def obtenerApellidoPaterno(self):
        return self.txtApellidoPaterno.text()
    def obtenerApellidoMaterno(self):
        return self.txtApellidoMaterno.text()
    def obtenerDireccion(self):
        return self.txtDireccion.text()
    def obtenerTelefono(self):
        return self.txtTelefono.text()

        # Procesos
    def listar(self):
        self.tblClientes.setRowCount(aCli.tamañoArregloCliente())
        self.tblClientes.setColumnCount(6)
        self.tblClientes.verticalHeader().setVisible(False)

        for i in range(0, aCli.tamañoArregloCliente()):
            self.tblClientes.setItem(i, 0, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getDniCliente()))
            self.tblClientes.setItem(i, 1, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getNombresCliente()))
            self.tblClientes.setItem(i, 2, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getApellidoPaternoCliente()))
            self.tblClientes.setItem(i, 3, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getApellidoMaternoCliente()))
            self.tblClientes.setItem(i, 4, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getDireccionCliente()))
            self.tblClientes.setItem(i, 5, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getTelefonoCliente()))

    def grabar(self):
        try:
            pos = aCli.buscarCliente(self.obtenerDNI())
            objCli = aCli.devolverCliente(pos)
            objCli.setNombresCliente(self.obtenerNombres())
            objCli.setApellidoPaternoCliente(self.obtenerApellidoPaterno())
            objCli.setApellidoMaternoCliente(self.obtenerApellidoMaterno())
            objCli.setDireccionCliente(self.obtenerDireccion())
            objCli.setTelefonoCliente(self.obtenerTelefono())
            aCli.grabar()
            self.listar()
        except:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Ha ocurrido un error al registrar el cliente", QtWidgets.QMessageBox.Ok)

    def registrar(self):
        objCli = Cliente(self.obtenerDni(), self.obtenerNombres(),self.obtenerApellidoPaterno(), self.obtenerApellidoMaterno(), self.obtenerDireccion(), self.obtenerTelefono())
        aCli.adicionaCliente(objCli)
        aCli.grabar()
        self.listar()
        QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Cliente registracon con éxito", QtWidgets.QMessageBox.Ok)