from formcreator import mainForm

def onCickCalendar():
    print(mainForm.calendarWidget.selectedDate().toString('dd.MM.yyyy'))
