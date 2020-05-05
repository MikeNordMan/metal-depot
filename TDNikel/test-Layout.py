import PySimpleGUI as sg
from list_Layout import new_Admission

window = sg.Window('Формирование поступления материала', new_Admission(), auto_size_text=True)

while True:
    event, values = window.read()
    if event is None:
        break