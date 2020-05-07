from DB import searchElement
import marki
import PySimpleGUI as sg
from list_Layout import new_Admission, buttonPrint

text ='Привет'
listbox=['1tdn20','1real20','3tdn20']


'''Функция формирующая Остатки на складе '''
# Прописать фнкцию и определить ей место!!!!
def ost():
    a=''
    for element in range(len(marki.names)):
        if searchElement(marki.names[element]) != '0':
           # print(marki.names[element] + ' вес нетто: ' + searchElement(marki.names[element]) )
            a= a +marki.names[element] + ' вес нетто: ' + searchElement(marki.names[element])+'\n'
    return a

'''Основной Layout'''
layout =[
        [sg.Frame('', [[sg.Text('Остатки на складе',size=(30,1))],[sg.Multiline(default_text=ost(), size=(35, 20))]]),
        sg.Frame('', [[sg.Button('Поступление', key='-winAdd-', size=(10, 1))],[sg.Button('Реализация', size=(10, 1))],[sg.Button('Переработка', size=(10, 1))]]),
        sg.Frame('', [[sg.Text('Дата'),sg.InputText(size=(10,1))],[sg.Listbox(values=listbox, size=(20, 19))]])],

        [sg.Text('_'  * 90)],

        [sg.Submit(tooltip='Click to submit this window'), sg.Button('Exit', key='-exit-')] # Посмотреть tooltip!!!
        ]

windowMain = sg.Window('Основная страница', layout)

windowAdmission_active = False # Переменная активности окна Поступления


while True:  # Event Loop
    event, values = windowMain.read()

    if event in (None, '-exit-'):
        break

    '''Открытие окна Поступление'''

    if event == '-winAdd-' and not windowAdmission_active:
        windowAdmission_active = True
        windowMain.Hide()  # Глушим основное окно

        windowAdmission = sg.Window('Формирование поступления материала', new_Admission(), auto_size_text=True)
        while True:
            eventAdd, valuesAdd = windowAdmission.Read()
            if eventAdd is None: # Прописать кнопку Exit
                windowAdmission.Close()
                windowAdmission_active = False
                windowMain.UnHide()
                break
            if eventAdd == 'printF':
                print('Проверка кнопки')
                buttonPrint()

windowMain.close()