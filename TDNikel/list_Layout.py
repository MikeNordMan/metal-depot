'''Место для хранения всех Layout'''
'''Попытка использования'''


import PySimpleGUI as sg
from marki import names

myRow = 15  # Колличество строк которые будут появляться
lStrText = 12 # длинна текстового поля
lenRasdelLine = 75 # Длинна разделительной линии

def new_Admission ():
    #myRow = 15  # Колличество строк которые будут появляться
    '''Часть Layout отвечающаяя за заголовок'''

    heder = [
             [sg.Text('Дата поступления:', pad=(5, 0)), sg.InputText(key='data', pad=(60, 0), size=(15, 1))],
             [sg.Text('Транспорт (Марка, номер)', pad=(5, 0)), sg.InputText(key='auto', pad=(15, 10), size=(15, 1))],
             [sg.Text('_' * lenRasdelLine)],  # Разделительная линия
             [sg.Text('Наименование', size=(lStrText, 1)), sg.Text('Вес Нетто (кг)', size=(lStrText, 1)),
              sg.Text('Засор ( % )', size=(lStrText, 1)) , sg.Text('Вес Брутто (кг)', size=(lStrText, 1))]
            ]

    '''Часть Layout отвечающая за формирование строки сопроводительной '''
    mol = [[[sg.InputCombo(names, size=(20, 1), key=str(i + 1)), sg.InputText(key='in' + str(i + 1), size=(20, 1)),
             sg.InputText('0', key='z' + str(i + 1), size=(3, 1)),
             sg.Text(background_color='white', key='res' + str(i + 1), size=(10, 1), enable_events=True,
                     text_color='black')]] for i in range(myRow)]

    colButton = [
                 [sg.Text('_' * lenRasdelLine)],   # Разделительная линия
                 [sg.Button('Добавить строку', key='on', visible=True),
                  sg.Button('Удалить строку', key='off', visible=True),
                  sg.Button('Сохранить', key='save', visible=True),
                  sg.Button('Печать', key='printF')],
                 [sg.Text('Иформационная строка', text_color='red', pad=(0, 10))]
                ]

    exitMesagge = [[sg.Text('', key='txt', size=(40, 2))]]

    layout = heder + [[sg.Column(mol[x], key='col' + str(x + 1), visible=False)] for x in
                      range(myRow)] + colButton + exitMesagge
    return layout