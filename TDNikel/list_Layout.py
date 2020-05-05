'''Место для хранения всех Layout'''
'''Попытка использования'''


import PySimpleGUI as sg
from marki import names

myRow = 15  # Колличество строк которые будут появляться

def new_Admission ():
    #myRow = 15  # Колличество строк которые будут появляться
    '''Часть Layout отвечающаяя за заголовок'''

    heder = [[sg.Text('Дата поступления:', pad=(15, 0)), sg.InputText(key='data', pad=(0, 0))],
             [sg.Text('Номер а/м', pad=(15, 10)), sg.InputText(key='auto', pad=(47, 10))]]

    '''Часть Layout отвечающая за формирование строки сопроводительной '''
    mol = [[[sg.InputCombo(names, size=(20, 1), key=str(i + 1)), sg.InputText(key='in' + str(i + 1), size=(20, 1)),
             sg.InputText('0', key='z' + str(i + 1), size=(3, 1)),
             sg.Text(background_color='white', key='res' + str(i + 1), size=(10, 1), enable_events=True,
                     text_color='black')]] for i in range(myRow)]

    colButton = [[sg.Button('Добавить строку', key='on', visible=True),
                  sg.Button('Удалить строку', key='off', visible=True),
                  sg.Button('Сохранить', key='save', visible=True),
                  sg.Button('Печать', key='printF')]]

    exitMesagge = [[sg.Text('', key='txt', size=(40, 2))]]

    layout = heder + [[sg.Column(mol[x], key='col' + str(x + 1), visible=False)] for x in
                      range(myRow)] + colButton + exitMesagge
    return layout