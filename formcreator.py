# from os import path
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QApplication

MainForm, Window = uic.loadUiType("mainform.ui")
DialogFormTask, dialogTaskWindow = uic.loadUiType("DialogFormTask.ui")
# DialogFormTask, dialogTaskWindow = loadUiType(path.join(path.dirname(__file__), "DialogFormTask.ui"))
DialogFinanceTask, dialogFinanceWindow = uic.loadUiType("DialogFormFinance.ui")

app = QApplication([])
mainWindow = Window()
dialogTaskWindow = dialogTaskWindow()
dialogFinanceWindow = dialogFinanceWindow()

mainForm = MainForm()
dialogFormTask = DialogFormTask()
dialogFinanceTask = DialogFinanceTask()


mainForm.setupUi(mainWindow)
dialogFormTask.setupUi(dialogTaskWindow)
dialogFinanceTask.setupUi(dialogFinanceWindow)

mainWindow.show()
