from DB import searchElement
import marki
import PySimpleGUI as sg
from layout_AddMaterial import *
from workWithRow import *
import datetime
from workWithList import *

now = datetime.datetime.now() # Получаем текущую дату
flagAdd =True  # Переменная для проверки создания пустых строк
text = 'Привет'
listbox = ['1tdn20','1real20','3tdn20']

'''Функция формирующая Остатки на складе '''
# Прописать фнкцию и определить ей место!!!!
def ost():
    a = ''
    for element in range(len(marki.names)):
        if searchElement(marki.names[element]) != '0':
           # print(marki.names[element] + ' вес нетто: ' + searchElement(marki.names[element]) )
            a= a +marki.names[element] + ' вес нетто: ' + searchElement(marki.names[element])+'\n'
    return a

'''Основной Layout'''
layout =[
        [sg.Frame('', [[sg.Text('Остатки на складе', size=(30, 1))], [sg.Multiline(default_text=ost(), size=(35, 20))]]),
        sg.Frame('', [[sg.Button('Поступление', key='-winAdd-', size=(10, 1))], [sg.Button('Реализация', size=(10, 1))], [sg.Button('Переработка', size=(10, 1))]]),
        sg.Frame('', [[sg.Text('Дата'), sg.InputText(now.strftime('%d.%m.%Y'), key='nowDate', size=(10,1))], [sg.Listbox(values=listbox, size=(20, 19))]])],

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
            if eventAdd in (None, '-close-'): # Прописать кнопку Exit
                flagAdd = True
                windowAdmission.Close()
                windowAdmission_active = False
                windowMain.UnHide()
                windowAdmission.close()
                break
            if eventAdd == 'printF':
                print('Проверка кнопки')
                buttonPrint()

            if eventAdd == '-addStr-': # Добовление строки (Написать условия проверки недопустимости появления пустых строк)
                if flagAdd == True:
                    openStrAdd = visibleRow(openStrAdd, myRow, windowAdmission)
                    flagAdd = False
                    print(valuesAdd)
                else:
                    print(valuesAdd)
                    if valuesAdd['mar' + str(openStrAdd)] != '' and valuesAdd['ves' + str(openStrAdd)] != '':
                        openStrAdd = visibleRow(openStrAdd, myRow, windowAdmission)
                print('Пустое значение строки')

            if eventAdd =='-offStr-' : # Удалениение строки (Написать условия проверки удаления строк)
                openStrAdd = visibleRowUn(openStrAdd, windowAdmission)
                print(openStrAdd)

            if eventAdd == '-save-': # Сохранение Документа
                #print(valuesAdd)
                messageSave(windowAdmission, valuesAdd, now.strftime('%d.%m.%Y'), generatorNumDok(keyBotton))

            for i in range(myRow):
                if valuesAdd['-zasor-' + str(i + 1)] != '0':
                    print('хорошо')
                    try:
                        windowAdmission.Element('res' + str(i + 1)).Update(
                        int(sumP(int(valuesAdd['ves' + str(i + 1)]), int(valuesAdd['-zasor-' + str(i + 1)]))))
                        windowAdmission.Element('txt').Update('')
                    except ValueError:
                        windowAdmission.Element('txt').Update('Введите числовые значения!')
                        print('Получилось нах')
                else:
                        windowAdmission.Element('res' + str(i + 1)).Update((valuesAdd['ves' + str(i + 1)]))


        windowAdmission.close()
windowMain.close()