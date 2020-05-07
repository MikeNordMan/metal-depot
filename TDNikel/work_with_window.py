import PySimpleGUI as sg
# Очень интересная схема работы с окнами
# Все работает, можно использовать
# Всегда необходимо создавать заново Layout второго окна,
# поэтому это необходимо делать в теле цикла (вариант  - 1),
# или в цикле вызывать функцию создающую Layout (вариант - 2)
text = 'Начальный текст'
from list_Layout import new_Admission

def changeText():
    text = window2.Element('-imput-')
    return text
def newLayout (): # Вариант - 2
    a = []
    a = [[sg.Text('Второе Окно')],
         [sg.InputText('', size=(20, 1), key='in')],
         [sg.Button('Exit in First Window', key='-in_comeback-')]]
    return a

def layout3 ():
    a = []
    a = [[sg.Text('Третье Окно')],
         [sg.Button('Exit in First Window', key='-in_comeback-')]]
    return a

layout = [[sg.Text('Второе Окно'), sg.Text('Третье Окно')],
          [sg.Text(text, key='-mainText-')],
          [sg.Button('Window 2', key='-win2-'), sg.Button('Поступление', key='-winAdd-')]]

windowAdmission_active = False # Переменная активности третьего окна
window2_active = False # Переменная активности второго окна

window1 = sg.Window('Первое Окно', layout, size=(300, 100))

while True:
    event, values = window1.Read()
    if event is None:
        break
    if event == '-win2-' and not window2_active:
        window2_active = True
        window1.Hide()
        layout2 = newLayout()
        window2 = sg.Window('Второе окно!!!').Layout(layout2)
        while True:
            event2, values2 = window2.Read()
            if event2 is None or event2 == '-in_comeback-':
                window2.Close()
                window2_active=False
                window1.Element('-mainText-').Update(values2['in'])
                window1.UnHide()
                break
    if event == '-winAdd-' and not windowAdmission_active:
        windowAdmission_active = True
        window1.Hide()
        #layoutAddmission = new_Admission()
        #       layout2 = [[sg.Text('Второе Окно')],     Вариант - 1
        #                   [sg.Button('Exit in First Window', key='-in_comeback-')]]
        #windowAdmission = sg.Window('Третье окно!!!').Layout(layout3)


        windowAdmission = sg.Window('Формирование поступления материала', new_Admission(), auto_size_text=True)
        while True:
            eventAdd, valuesAdd = windowAdmission.Read()
            if eventAdd is None:
                windowAdmission.Close()
                windowAdmission_active = False
                window1.UnHide()
                break
