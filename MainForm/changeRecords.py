from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import QDate
from formcreator import mainForm, dialogFormTask, dialogTaskWindow, dialogFinanceTask, dialogFinanceWindow


def ZadachiClick():
    dialogFormTask.dateEditTask.setDate(QDate.currentDate())
    dialogFormTask.timeEditStart.setTime(QtCore.QTime.currentTime())
    dialogFormTask.textEdit.setText("")
    dialogFormTask.comboBoxTaskStatus.setCurrentIndex(0)
    dialogTaskWindow.show()

def FinanceClick():
    dialogFinanceTask.dateEditTask.setDate(QDate.currentDate())
    dialogFinanceTask.textEdit.setText("")
    dialogFinanceTask.Amount.setValue(1)
    dialogFinanceTask.Sum.setValue(0)
    if mainForm.all.isChecked() or mainForm.incoming.isChecked():
        dialogFinanceTask.comboBox.setCurrentIndex(0)
    else:
        dialogFinanceTask.comboBox.setCurrentIndex(1)
    dialogFinanceWindow.show()
def AddRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.Captionlabel.setText(_translate("DialogFormTask", "Добавление записи"))
        dialogFormTask.ButtonSave.setText("Добавить")
        dialogFormTask.ButtonSave.setIcon(QtGui.QIcon("icons/add64.png"))
        ZadachiClick()
    else:
        dialogFinanceTask.Captionlabel.setText(_translate("DialogFinanceTask", "Добавление записи"))
        dialogFinanceTask.ButtonSave.setText("Добавить")
        dialogFinanceTask.ButtonSave.setIcon(QtGui.QIcon("icons/add64.png"))
        FinanceClick()


def DelRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.Captionlabel.setText(_translate("DialogFormTask", "Удаление записи"))
        dialogFormTask.ButtonSave.setText("Удалить")
        dialogFormTask.ButtonSave.setIcon(QtGui.QIcon("icons/delete64.png"))
        ZadachiClick()
    else:
        dialogFinanceTask.Captionlabel.setText(_translate("DialogFinanceTask", "Удаление записи"))
        dialogFinanceTask.ButtonSave.setText("Удалить")
        dialogFinanceTask.ButtonSave.setIcon(QtGui.QIcon("icons/delete64.png"))
        FinanceClick()


def EditRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.Captionlabel.setText(_translate("DialogFormTask", "Изменение записи"))
        dialogFormTask.ButtonSave.setText("Изменить")
        dialogFormTask.ButtonSave.setIcon(QtGui.QIcon("icons/edit64.png"))
        ZadachiClick()
    else:
        dialogFinanceTask.Captionlabel.setText(_translate("DialogFinanceTask", "Изменение записи"))
        dialogFinanceTask.ButtonSave.setText("Изменить")
        dialogFinanceTask.ButtonSave.setIcon(QtGui.QIcon("icons/edit64.png"))
        FinanceClick()

