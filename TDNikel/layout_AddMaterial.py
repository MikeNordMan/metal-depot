'''Место для хранения Layout Поступление'''



import PySimpleGUI as sg
from marki import names
from generatorNumberDok import generatorNumDok
keyBotton = 'tdn' # Ключ layout
myRow = 15  # Возможное колличество строк для появления
lStrText = 12  # длинна текстового поля
lenRasdelLine = 75  # Длинна разделительной линии
openStrAdd = 0  # Колличество открытых строк

def new_Admission ():
    '''Цвет темы'''

    sg.theme('LightBrown7')

    '''Часть Layout отвечающаяя за заголовок'''

    heder = [
             [sg.Text('Номер Сопроводительной:', pad=(5, 5)), sg.Text(generatorNumDok(keyBotton), key='dok', pad=(50, 0))],
             [sg.Text('Дата поступления:', pad=(5, 5)), sg.InputText(key='data', pad=(60, 0), size=(15, 1))],
             [sg.Text('Поставщик:', pad=(5, 5)), sg.InputText(key='post', pad=(100, 0), size=(15, 1))],
             [sg.Text('Транспорт (Марка, номер)', pad=(5, 5)), sg.InputText(key='auto', pad=(15, 5), size=(15, 1))],
             [sg.Text('_' * lenRasdelLine)],  # Разделительная линия
             [sg.Text('Наименование', pad=(20, 5), size=(lStrText, 1)), sg.Text('Вес Нетто (кг)', pad=(45, 5), size=(10, 1)),
              sg.Text('Засор ( % )', pad=(1, 5), size=(lStrText, 1)) , sg.Text('Вес Брутто (кг)', pad=(1, 5), size=(lStrText, 1))]
            ]

    '''Часть Layout отвечающая за формирование строки сопроводительной '''
    mol = [[[sg.InputCombo(names, size=(20, 1), key='mar' + str(i + 1), pad=(0, 1)),
             sg.InputText(key='ves' + str(i + 1), size=(12, 1), pad=(20, 1)),
             sg.InputText('0', key='-zasor-' + str(i + 1), size=(3, 1), pad=(45, 1)),
             sg.Text(background_color='#4B8E8D', key='res' + str(i + 1), size=(10, 1), pad=(10, 1), enable_events=True,
                     text_color='white')]] for i in range(myRow)]

    colButton = [
                 [sg.Text('_' * lenRasdelLine)],   # Разделительная линия
                 [sg.Button('Добавить строку', key='-addStr-', visible=True),
                  sg.Button('Удалить строку', key='-offStr-', visible=True),
                  sg.Button('Сохранить', key='-save-', visible=True),
                  sg.Button('Печать', key='printF')],
                 [sg.Text('Иформационная строка', text_color='red', pad=(0, 10))]
                ]

    exitMesagge = [
                   [sg.Text('', key='txt', size=(40, 2))],
                   [sg.Button('Закрыть Окно', key='-close-')]
                  ]

    layout = heder + [[sg.Column(mol[x], key='col' + str(x + 1), visible=False)] for x in
                      range(myRow)] + colButton + exitMesagge

   # window = sg.Window('Формирование поступления материала', layout, auto_size_text=True, finalize=True)

    #return window
    return  layout
'''-----------------------------------------Функции----------------------------------------------------'''
def buttonPrint():
    print('Проверка кнопи из Функции')
