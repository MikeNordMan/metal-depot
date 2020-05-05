import PySimpleGUI as sg
sg.theme('BluePurple')
import marki
from DB import dbinsert

name = marki.names
layout = [[sg.Text('Список полей для Базы данных'), sg.Text(size=(15, 1), key='-OUTPUT-')],
              [sg.Text('Дата поступления:', size=(20, 1)), sg.Input(key='-IN1-', size=(15, 1))],
              [sg.Text('Дата создания документа:', size=(20, 1)), sg.Input(key='-IN2-', size=(15, 1))],
              [sg.Text('Номер сопроводительной:', size=(20, 1)), sg.Input(key='-IN3-', size=(15, 1))],
              [sg.Text('Поставщик:', size=(20, 1)), sg.Input(key='-IN4-', size=(15, 1))],
              [sg.Text('Ноименование марки:', size=(20, 1)), sg.InputCombo(name, key='-IN5-', size=(15, 1))],
              [sg.Text('Вес Брутто:', size=(20, 1)), sg.Input(key='-IN6-', size=(15, 1))],
              [sg.Text('Засор:', size=(20, 1)), sg.Input(key='-IN7-', size=(15, 1))],
              [sg.Text('Вес нетто:', size=(20, 1)), sg.Input(key='-IN8-', size=(15, 1))],
              [sg.Text('Свободное поле:',size=(20, 1)), sg.Input(key='-IN9-', size=(15, 1))],

              [sg.Button('Сохранить в БД', key='-Save-'), sg.Button('Exit')]]

window = sg.Window('Тестовое внесение в двнных в БД', layout)

while True:  # Event Loop
    event, values = window.read()
    #print(event, values)
    if event in (None, 'Exit'):
        break
    if event == '-Save-':
        a = []
        #print(values)
        for i in values:
            a.append(values.get(i))
        print(a)
        dbinsert(a)
        print('Сохранено')


window.close()
