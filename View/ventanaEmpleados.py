from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from Controller.Mantenimiento_Empleado import *
from Controller.Controller_Empleado import *

aEmp = ArregloEmpleados()

class VentanaEmpleados(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaEmpleados, self).__init__(parent)
        uic.loadUi("UI/ventanaEmpleados.ui", self)
        self.btnRegistrar.clicked.connect(self.registrar)
        self.ListarDatos()
        self.show()

        # Procesos

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

    def ListarDatos(self):
         self.tblEmpleados.setRowCount(aEmp.tamañoArregloEmpleado())
         self.tblEmpleados.setColumnCount(6)
         self.tblEmpleados.verticalHeader().setVisible(False)
         for i in range(0, aEmp.tamañoArregloEmpleado()):
             self.tblEmpleados.setItem(i, 0, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getDniEmpleado()))
             self.tblEmpleados.setItem(i, 1, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getNombresEmpleado()))
             self.tblEmpleados.setItem(i, 2, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getApellidoPaternoEmpleado()))
             self.tblEmpleados.setItem(i, 3, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getApellidoMaternoEmpleado()))
             self.tblEmpleados.setItem(i, 4, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getDireccionEmpleado()))
             self.tblEmpleados.setItem(i, 5, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getTelefonoEmpleado()))

    def grabar(self):
        try:
            pos = aEmp.buscarEmpleado(self.obtenerDni())
            objEmp = aEmp.devolverEmpleado(pos)
            objEmp.setNombresEmpleado(self.obtenerNombres())
            objEmp.setApellidoPaternoEmpleado(self.obtenerApellidoPaterno())
            objEmp.setApellidoMaternoEmpleado(self.obtenerApellidoMaterno())
            objEmp.setDireccionEmpleado(self.obtenerDireccion())
            objEmp.setTelefonoEmpleado(self.obtenerTelefono())
            aEmp.grabar()
            self.ListarDatos()
        except:
            QtWidgets.QMessageBox.information(self, "Registrar Empleado", "Ha ocurrido un error al registrar el cliente", QtWidgets.QMessageBox.Ok)

    def registrar(self):
        objEmp = Empleado(self.obtenerDni(), self.obtenerNombres(),self.obtenerApellidoPaterno(), self.obtenerApellidoMaterno(), self.obtenerDireccion(), self.obtenerTelefono())
        aEmp.adicionaEmpleado(objEmp)
        aEmp.grabar()
        self.ListarDatos()
        QtWidgets.QMessageBox.information(self, "Registrar Empleado", "Empleado registrado con con éxito", QtWidgets.QMessageBox.Ok)