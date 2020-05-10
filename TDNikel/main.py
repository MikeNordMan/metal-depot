from DB import *
import marki
import PySimpleGUI as sg
from layout_AddMaterial import *
from layout_RealMaterial import *
from workWithRow import *
import datetime
from workWithList import *

now = datetime.datetime.now() # Получаем текущую дату
now = now.strftime('%d.%m.%Y')
flagAdd =True  # Переменная для проверки создания пустых строк
text = 'Привет'
listbox = ['1tdn20', '1real20', '3tdn20']

'''Функция Формирования Журнала Событий'''
def ivetLog(nowDate): # Вход сегодняшняя дата
    a =[]
    istboxData =[]
    a = searchElementInBD('numberDok', 'dataDok', str(nowDate))
    #print('Промежуточный массив :')
    #print(a)
    listboxData = findRepitData(a)
    #print('Это listBox : ')
    #print(listboxData)
    return listboxData # Выход: массив для листбокса



'''Функция формирующая Остатки на складе '''
def ost():
    a = ''
    for element in range(len(marki.names)):
        if searchElement(marki.names[element]) != '0':
           # print(marki.names[element] + ' вес нетто: ' + searchElement(marki.names[element]) )
            a= a +marki.names[element] + ' вес нетто: ' + searchElement(marki.names[element])+'\n'
    return a
'''Цвет темы'''

sg.theme('LightPurple')

'''Основной Layout'''
layout =[
        [sg.Frame('', [[sg.Text('Остатки на складе', size=(30, 1))], [sg.Multiline(default_text=ost(), key='depot', size=(35, 20))]]),
        sg.Frame('', [[sg.Button('Поступление', key='-winAdd-', size=(10, 1))],
                      [sg.Button('Реализация', key='-winSale-', size=(10, 1))], [sg.Button('Переработка', size=(10, 1))]]),
        sg.Frame('', [[sg.Text('Дата'), sg.InputText(now, key='nowDate', size=(10,1))], [sg.Listbox(values=ivetLog(now), key='eventLog', size=(20, 19))]])],

        [sg.Text('_'  * 90)],

        [sg.Submit(tooltip='Click to submit this window'), sg.Button('Exit', key='-exit-')] # Посмотреть tooltip!!!
        ]

windowMain = sg.Window('Основная страница', layout)

windowAdmission_active = False # Переменная активности окна Поступления
windowSale_active = False # Переменная активности окна Реализация

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
            ''' Действия при нажатии кнопки Закрыть layout - AddMaterial'''
            if eventAdd in (None, '-close-'): # Прописать кнопку Exit
                flagAdd = True
                windowAdmission.Close()
                windowAdmission_active = False
                windowMain.UnHide()
                windowAdmission.close()
                break
            ''' Действия при нажатии кнопки Печать layout - AddMaterial'''
            if eventAdd == 'printF':
                print('Проверка кнопки')
                buttonPrint()
            ''' Действия при нажатии кнопки Добавить строку layout - AddMaterial'''
            if eventAdd == '-addStr-': # Добовление строки (Написать условия проверки недопустимости появления пустых строк)
                #print(eventAdd)
                if flagAdd == True:
                    openStrAdd = visibleRow(openStrAdd, myRow, windowAdmission)
                    flagAdd = False
                    #print(valuesAdd)
                else:
                    #print(valuesAdd)
                    if valuesAdd['mar' + str(openStrAdd)] != '' and valuesAdd['ves' + str(openStrAdd)] != '':
                        openStrAdd = visibleRow(openStrAdd, myRow, windowAdmission)
               # print('Пустое значение строки')
            ''' Действия при нажатии кнопки Удалить строку layout - AddMaterial'''
            if eventAdd =='-offStr-' : # Удалениение строки (Написать условия проверки удаления строк)
                openStrAdd = visibleRowUn(openStrAdd, windowAdmission)
                #print(openStrAdd)
            ''' Действия при нажатии кнопки Сохранить layout - AddMaterial'''
            if eventAdd == '-save-': # Сохранение Документа
                #print(valuesAdd)
                messageSave(windowAdmission, valuesAdd, now, generatorNumDok(keyBotton), openStrAdd, keyBotton)
                openStrAdd = 0
                windowMain.FindElement('depot').Update(ost())
                windowMain.FindElement('eventLog').Update(ivetLog(now))

            for i in range(myRow):
               if valuesAdd['-zasor-' + str(i + 1)] != '0':
                  # print('хорошо')
                   try:
                        windowAdmission.Element('res' + str(i + 1)).Update(
                        int(sumP(int(valuesAdd['ves' + str(i + 1)]), int(valuesAdd['-zasor-' + str(i + 1)]))))
                        windowAdmission.Element('txt').Update('')
                   except ValueError:
                        windowAdmission.Element('txt').Update('Введите числовые значения!')
                   #     print('Получилось нах')
               else:
                    windowAdmission.Element('res' + str(i + 1)).Update((valuesAdd['ves' + str(i + 1)]))
        windowAdmission.close()

    '''Открытие окна Реализация'''
    if event == '-winSale-' and not windowSale_active:
        windowSale_active = True
        windowMain.Hide() # Глушим основное окно
        windowSale = sg.Window('Формирование Реализации Материала', new_Sale(), auto_size_text=True)
        while True:
            eventSale, valuesSale = windowSale.Read()
            ''' Действия при нажатии кнопки Закрыть layout - RealMaterial'''
            if eventSale in (None, '-close-'):
                flagAdd = True
                windowSale.Close()
                windowSale_active =False
                windowMain.UnHide()
                windowSale.close()
                break
            ''' Действия при нажатии кнопки Печать layout - RealMaterial'''
            if eventSale == 'printF':
                print('Проверка кнопки Печать для Реализации')
                buttonPrint()
            ''' Действия при нажатии кнопки Добавить строку layout - RealMaterial'''
            if eventSale == '-addStr-':
                if flagAdd == True:
                    openStrSale = visibleRow(openStrSale, myRow, windowSale)
                    flagAdd = False
                    # print(valuesAdd)
                else:
                    # print(valuesAdd)
                    if valuesSale['mar' + str(openStrSale)] != '' and valuesSale['ves' + str(openStrSale)] != '':
                        openStrSale = visibleRow(openStrSale, myRow, windowSale)
            ''' Действия при нажатии кнопки Удалить строку layout - RealMaterial'''
            if eventSale =='-offStr-' : # Удалениение строки (Написать условия проверки удаления строк)
                openStrSale = visibleRowUn(openStrSale, windowSale)
                #print(openStrAdd)
            ''' Действия при нажатии кнопки Сохранить layout - RealMaterial'''
            if eventSale == '-save-':  # Сохранение Документа
                messageSave(windowSale, valuesSale, now, generatorNumDok(keyBotton), openStrSale, keyBotton)
                openStrSale = 0
                windowMain.FindElement('depot').Update(ost())
                windowMain.FindElement('eventLog').Update(ivetLog(now))

            for i in range(myRow):
               if valuesSale['-zasor-' + str(i + 1)] != '0':
                  # print('хорошо')
                   try:
                        windowSale.Element('res' + str(i + 1)).Update(
                        int(sumP(int(valuesSale['ves' + str(i + 1)]), int(valuesSale['-zasor-' + str(i + 1)]))))
                        windowSale.Element('txt').Update('')
                   except ValueError:
                        windowSale.Element('txt').Update('Введите числовые значения!')
                   #     print('Получилось нах')
               else:
                    windowSale.Element('res' + str(i + 1)).Update((valuesSale['ves' + str(i + 1)]))

        windowSale.close()
windowMain.close()