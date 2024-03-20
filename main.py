from formcreator import mainForm, dialogFormTask, app, dialogFinanceTask
from Flags import Flags
from CheckBoxClick import CheckBoxClick
from MainForm.onClickCalendar import onCickCalendar
from PyQt6.QtCore import QDate
from MainForm.DatePeriod import SetDateIn, SetDateOut
from MainForm.changeRecords import AddRecordClick, DelRecordClick, EditRecordClick
from DialogFormTaskClose import dialogFormTaskClose
from dialogFinanceTaskClose import dialogFinanceTaskClose
flags = Flags()

mainForm.dateEditIn.setDate(QDate.currentDate())
mainForm.dateEditOut.setDate(QDate.currentDate())
mainForm.calendarWidget.clicked.connect(onCickCalendar)
mainForm.checkBoxFilterDate.clicked.connect(CheckBoxClick)
mainForm.dateEditIn.dateChanged.connect(SetDateIn)
mainForm.dateEditOut.dateChanged.connect(SetDateOut)
mainForm.ButtonAddRecord.clicked.connect(AddRecordClick)
mainForm.ButtonDeleteRecord.clicked.connect(DelRecordClick)
mainForm.ButtonEditRecord.clicked.connect(EditRecordClick)

dialogFormTask.ButtonCancel.clicked.connect(dialogFormTaskClose)
dialogFinanceTask.ButtonCancel.clicked.connect(dialogFinanceTaskClose)

app.exec()
