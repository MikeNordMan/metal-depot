from DB import searchElement
import marki
import PySimpleGUI as sg

text ='Привет'
listbox=['1tdn20','1real20','3tdn20']

def ost():
    a=''
    for element in range(len(marki.names)):
        if searchElement(marki.names[element]) != '0':
           # print(marki.names[element] + ' вес нетто: ' + searchElement(marki.names[element]) )
            a= a +marki.names[element] + ' вес нетто: ' + searchElement(marki.names[element])+'\n'
    return a


layout =[
        [sg.Frame('', [[sg.Text('Остатки на складе',size=(30,1))],[sg.Multiline(default_text=ost(), size=(35, 20))]]),
        sg.Frame('', [[sg.Button('Поступление', size=(10, 1))],[sg.Button('Реализация', size=(10, 1))],[sg.Button('Переработка', size=(10, 1))]]),
        sg.Frame('', [[sg.Text('Дата'),sg.InputText(size=(10,1))],[sg.Listbox(values=listbox, size=(20, 19))]])],


        [sg.Text('_'  * 90)],


        [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]
        ]

window = sg.Window('Основная страница', layout)

while True:  # Event Loop
    event, values = window.read()
    #print(event, values)

    if event in (None):
        break



window.close()