from DB import *
import marki
import PySimpleGUI as sg
from layout_AddMaterial import *
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

'''Основной Layout'''
layout =[
        [sg.Frame('', [[sg.Text('Остатки на складе', size=(30, 1))], [sg.Multiline(default_text=ost(), key='depot', size=(35, 20))]]),
        sg.Frame('', [[sg.Button('Поступление', key='-winAdd-', size=(10, 1))], [sg.Button('Реализация', size=(10, 1))], [sg.Button('Переработка', size=(10, 1))]]),
        sg.Frame('', [[sg.Text('Дата'), sg.InputText(now, key='nowDate', size=(10,1))], [sg.Listbox(values=ivetLog(now), key='eventLog', size=(20, 19))]])],

        [sg.Text('_'  * 90)],

        [sg.Submit(tooltip='Click to submit this window'), sg.Button('Exit', key='-exit-')] # Посмотреть tooltip!!!
        ]

windowMain = sg.Window('Основная страница', layout)

windowAdmission_active = False # Переменная активности окна Поступления


while True:  # Event Loop
    event, values = windowMain.read()

    if event in (None, '-exit-'):
        break
    #windowMain.FindElement('depot').Update(ost())

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

                #eventAdd =[]
                break
            if eventAdd == 'printF':
                print('Проверка кнопки')
                buttonPrint()

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

            if eventAdd =='-offStr-' : # Удалениение строки (Написать условия проверки удаления строк)
                openStrAdd = visibleRowUn(openStrAdd, windowAdmission)
                #print(openStrAdd)

            if eventAdd == '-save-': # Сохранение Документа
                #print(valuesAdd)
                messageSave(windowAdmission, valuesAdd, now, generatorNumDok(keyBotton), openStrAdd)
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
windowMain.close()