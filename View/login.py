from PyQt5 import QtWidgets, uic
from View.ventanaPrincipal import VentanaPrincipal

class Login(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        uic.loadUi("UI/login.ui", self)
        self.show()

        #Eventos...
        self.btnIniciar.clicked.connect(self.iniciarSesion)

    # Aquí van las nuevas funciones
    def iniciarSesion(self):
        usuario = self.txtName.text().lower()
        contrasena = self.txtPassword.text()
        if usuario == "admin" and contrasena == "123":
            self.close()
            vprincipal = VentanaPrincipal(self)
            vprincipal.show()
        else:
            mensaje = QtWidgets.QMessageBox()
            mensaje.setWindowTitle("Sistema de Ventas")
            mensaje.setText("Los datos ingresados son incorrectos")
            mensaje.setIcon(QtWidgets.QMessageBox.Information)