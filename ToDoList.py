
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

class ToDoList(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ToDoList.ui", self)

        self.btnagregar.clicked.connect(self.AgregarTarea)
        self.btneliminar.clicked.connect(self.EliminarTarea)
        self.btneditar.clicked.connect(self.EditarTarea)

    def AgregarTarea(self):
        tarea = self.edttarea.text()

        if tarea:
            self.lsttareas.addItem(tarea)
            self.edttarea.clear()
        else:
            QMessageBox.warning(self, "Error", "Por favor ingrese una tarea.")

    def EliminarTarea(self):
        indiceTareaBorrar = self.lsttareas.currentRow()

        if indiceTareaBorrar != -1:
            self.lsttareas.takeItem(indiceTareaBorrar)
            self.edttarea.clear()
        else:
            QMessageBox.warning(self, "Error", "Seleccione una tarea.")

    def EditarTarea(self):
        indiceTareaEditar = self.lsttareas.currentRow()
        nuevoTexto = self.edttarea.text().strip()

        if indiceTareaEditar != -1 and nuevoTexto != "":
            self.lsttareas.currentItem().setText(nuevoTexto)
            self.edttarea.clear()
        else:
            QMessageBox.warning(self, "Error", "Seleccione una tarea e ingrese el nuevo texto.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = ToDoList()
    ventana.show()
    sys.exit(app.exec_())
