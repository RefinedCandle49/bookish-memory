from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from Controller.Mantenimiento_Productos import ArregloProductos
from Controller.Controller_Producto import *

aPro = ArregloProductos()

class VentanaProductos(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaProductos, self).__init__(parent)
        uic.loadUi("UI/ventanaProductos.ui", self)
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnConsultar.clicked.connect(self.modificar)
        self.btnActualizar.clicked.connect(self.grabar)
        self.listar()
        self.show()

    def obtenerCodigo(self):
        return self.txtCodigo.text()
    def obtenerNombre(self):
        return self.txtNombre.text()
    def obtenerDescripcion(self):
        return self.txtDescripcion.text()
    def obtenerStockMinimo(self):
        return self.txtStockMinimo.text()
    def obtenerStockActual(self):
        return self.txtStockActual.text()
    def obtenerPrecioCosto(self):
        return self.txtPrecioCosto.text()
    def obtenerPrecioVenta(self):
        return self.txtPrecioVenta.text()
    def obtenerProveedor(self):
        return self.cboProveedor.currentText()
    def obtenerAlmacen(self):
        return self.cboAlmacen.currentText()

        # Procesos
    def listar(self):
        self.tblProductos.setRowCount(aPro.tamañoArregloProducto())
        self.tblProductos.setColumnCount(9)
        self.tblProductos.verticalHeader().setVisible(False)
        for i in range(0, aPro.tamañoArregloProducto()):
            self.tblProductos.setItem(i, 0, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getCodigo()))
            self.tblProductos.setItem(i, 1, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getNombre()))
            self.tblProductos.setItem(i, 2, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getDescripcion()))
            self.tblProductos.setItem(i, 3, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getStockMinimo()))
            self.tblProductos.setItem(i, 4, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getStockActual()))
            self.tblProductos.setItem(i, 5, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getPrecioCosto()))
            self.tblProductos.setItem(i, 6, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getPrecioVenta()))
            self.tblProductos.setItem(i, 7, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getProveedor()))
            self.tblProductos.setItem(i, 8, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getAlmacen()))

    def grabar(self):
        try:
            pos = aPro.buscarProducto(self.obtenerCodigo())
            objPro = aPro.devolverProducto(pos)
            objPro = setCodigo(self.obtenerCodigo())
            objPro = setNombre(self.obtenerNombre())
            objPro = setDescripcion(self.obtenerDescripcion())
            objPro = setStockMinimo(self.obtenerStockMinimo())
            objPro = setStockActual(self.obtenerStockActual())
            objPro = setPrecioCosto(self.obtenerPrecioCosto())
            objPro = setPrecioVenta(self.obtenerPrecioVenta())
            objPro = setProveedor(self.obtenerProveedor())
            objPro = setAlmacen(self.obtenerAlmacen())
            aPro.grabar()
            self.listar()
        except:
            QtWidgets.QMessageBox.information(self, "Registrar Producto", "Ha ocurrido un error al registrar el producto", QtWidgets.QMessageBox.Ok)

    def registrar(self):
        objPro = Producto(self.obtenerCodigo(), self.obtenerNombre(), self.obtenerDescripcion(), self.obtenerStockMinimo(), self.obtenerStockActual(), self.obtenerPrecioCosto(), self.obtenerPrecioVenta(), self.obtenerProveedor(), self.obtenerAlmacen())
        aPro.adicionaProducto(objPro)
        aPro.grabar()
        self.listar()
        QtWidgets.QMessageBox.information(self, "Registrar Producto", "Producto registrado con con éxito", QtWidgets.QMessageBox.Ok)

    def eliminar(self):
        if aPro.tamañoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Producto", "No existen productos a eliminar",
                                              QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tblProductos.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                codigo = self.tblProductos.item(indiceFila, 0).text()
                pos = aPro.buscarProducto(codigo)
                aPro.eliminarProducto(pos)
                aPro.grabar()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Producto", "Ningún producto seleccionado", QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aPro.tamañoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Producto", "No se encontraron registros para el DNI ingresado", QtWidgets.QMessageBox.Ok)
        else:
            codigo = QtWidgets.QInputDialog.getText(self, "Buscar Productos", "Ingrese el DNI a modificiar")
            pos = aPro.buscarProducto(codigo)
            if pos != -1:
                objProducto = aPro.devolverProducto(pos)
                self.txtCodigo.setText(objProducto.getCodigo())
                self.txtNombre.setText(objProducto.getNombre())
                self.txtDescripcion.setText(objProducto.getDescripcion())
                self.txtStockMinimo.setText(objProducto.getStockMinimo())
                self.txtStockActual.setText(objProducto.getStockActual())
                self.txtPrecioCosto.setText(objProducto.getPrecioCosto())
                self.txtPrecioVenta.setText(objProducto.getPrecioVenta())
                self.cboProveedor.setCurrentText(objProducto.getProveedor())
                self.cboAlmacen.setCurrentText(objProducto.getAlmacen())