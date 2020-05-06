''' задача: Создать модуль способный генерировать номер поступления(переработки, реализации)'''
''' План: в модуль попадает команда которая является ключем для создания номера
 создается запрос к базе данных к полю содержащему ранее созданые номера, далее происходит сортировка 
 по ключю. Отсортированный массив подвергается сортировке но по наибольшему номеру ( maxZnach ), то есть 
 создаем цифровой массив в котором находим наибольшее значение и передаем его в функцию ( resalt ) которая 
 увеличивает значение на 1 и конконтенирует с ключем и возвращает новый код документа.  
 '''
keyN = 'tdn' # Тестовый ключ
#keyN = 'real' # Тестовый ключ
#keyN = 'trans' # Тестовый ключ


a = ['tdn2', 'tdn3', 'real24', 'trans52', 'tdn4', 'trans60', 'trans2', 'tdn5', 'tdn5'] # Тестовый массив документов


'''Функция получения массива документов из БД'''




''' Функция сортировки массива по ключу'''
def sortingArr(inArr, keyN): # Вход: Массив из базы данных , ключ
    arrSort = []
    for i in range(len(inArr)):
        if inArr[i].find(keyN)==0:
            arrSort.append(a[i])
    #print(arrSort)
    arrNum = []
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


def generatorNumDok(arrBD, keyN):
    c = sortingArr(arrBD, keyN)
    numDok = resalt(keyN, maxZnach(c))
    print(numDok)


generatorNumDok(a, keyN)