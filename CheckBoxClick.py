from formcreator import mainForm
from PyQt6.QtCore import QDate

def CheckBoxClick():
    if mainForm.checkBoxFilterDate.isChecked():
       # mainForm.dateEditIn.setEnabled(True)
       # mainForm.dateEditOut.setEnabled(True)
       # mainForm.ButtonFilter.setEnabled(True)
        mainForm.dateEditIn.setDate(QDate.currentDate())
        mainForm.dateEditOut.setDate(QDate.currentDate())
    else:
        # mainForm.dateEditIn.setEnabled(False)
        # mainForm.dateEditOut.setEnabled(False)
        # mainForm.ButtonFilter.setEnabled(False)
        pass

