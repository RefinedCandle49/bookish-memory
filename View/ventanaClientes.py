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
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnConsultar.clicked.connect(self.modificar)
        self.btnActualizar.clicked.connect(self.grabar)
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
            pos = aCli.buscarCliente(self.obtenerDni())
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

    def eliminar(self):
        if aCli.tamañoArregloCliente() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "No existen clientes a eliminar", QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tblClientes.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                dni = self.tblClientes.item(indiceFila, 0).text()
                pos = aCli.buscarCliente(dni)
                aCli.eliminarCliente(pos)
                aCli.grabar()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "Ningún cliente seleccionado", QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aCli.tamañoArregloCliente() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Cliente", "No se encontraron registros para el DNI ingresado", QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Buscar Clientes", "Ingrese el DNI a modificiar")
            pos = aCli.buscarCliente(dni)
            if pos != -1:
                objCliente = aCli.devolverCliente(pos)
                self.txtDni.setText(objCliente.getDniCliente())
                self.txtNombres.setText(objCliente.getNombresCliente())
                self.txtApellidoPaterno.setText(objCliente.getApellidoPaternoCliente())
                self.txtApellidoMaterno.setText(objCliente.getApellidoMaternoCliente())
                self.txtDireccion.setText(objCliente.getDireccionCliente())
                self.txtTelefono.setText(objCliente.getTelefonoCliente())