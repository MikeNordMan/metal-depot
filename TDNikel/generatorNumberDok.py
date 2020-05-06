''' задача: Создать модуль способный генерировать номер поступления(переработки, реализации)'''
''' План: в модуль попадает команда которая является ключем для создания номера
 создается запрос к базе данных к полю содержащему ранее созданые номера, далее происходит сортировка 
 по ключю. Отсортированный массив подвергается сортировке но по наибольшему номеру ( maxZnach ), то есть 
 создаем цифровой массив в котором находим наибольшее значение и передаем его в функцию ( resalt ) которая 
 увеличивает значение на 1 и конконтенирует с ключем и возвращает новый код документа.  
 '''
'''Задача выполнена Модуль работает'''

import  sqlite3

keyN = 'tdn' # Тестовый ключ
#keyN = 'real' # Тестовый ключ
#keyN = 'trans' # Тестовый ключ
#keyN = 'tra' # Тестовый ключ

'''Функция получения массива документов из БД'''
def searchNumberdoK():
    '''Поправить передачу в функцию имя БД'''

    connect = sqlite3.connect('myDB.db')
    cursor = connect.cursor()
    query = 'SELECT numberDok FROM user '

    cursor.execute(query)
    data = cursor.fetchall()

    new_data = []
    for i in data:
        new_data.append(i[0])
    data = new_data
    del(new_data)
    #print(data)
    return data

''' Функция сортировки массива по ключу'''
def sortingArr(inArr, keyN): # Вход: Массив из базы данных , ключ
    arrSort = []
    arrNum = []
    for i in range(len(inArr)):
        if inArr[i].find(keyN)==0:
            arrSort.append(inArr[i])
   # print(arrSort)
    if arrSort==[]:
       arrNum.append('0')
      # print(arrNum)
       return arrNum
    else:
        for i in range(len(arrSort)):
            arrNum.append(int(lineBrk(arrSort[i], keyN)))
        # print(arrNum)
        return arrNum # Выход: Цифровой Массив

''' Функция разбития строки для получения номера'''

def lineBrk(lineS, keyN ): # Вход: Строка которую нужно разбить, ключ
    strBrk = lineS.split(keyN)
    number =strBrk[1]
    #print(number)
    return number   # Выход: цифровой остаток строки

'''Функция поиска максимального значения массива'''

def maxZnach(arrNum): # Вход: Цифровой Массив
    number = max(arrNum)
    #print(number)
    return int(number)  # Выход: максимальное значение в массиве

'''Функция конконтенации ключа и значения'''

def resalt(keyN, number): # Вход: ключь, последний номер документа
    resalt = keyN + str(number + 1)
    #print(resalt)
    return resalt # Выход: Новый номер документа

''' Главная Функция Модуля по ключу получаем для БД генерацию номера документа'''
def generatorNumDok(keyN):
    #arrBD =[]
    arrBD = searchNumberdoK()
    #print(arrBD)
    c = sortingArr(arrBD, keyN)
    numDok = resalt(keyN, maxZnach(c))
    print(numDok)
    return numDok


generatorNumDok(keyN) # Тест функции
