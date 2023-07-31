from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from Controller.Mantenimiento_Empleado import *

aEmp = ArregloEmpleados()

class VentanaEmpleados(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaEmpleados, self).__init__(parent)
        uic.loadUi("UI/ventanaEmpleados.ui", self)
        self.ListarDatos()
        self.show()

        # Procesos
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