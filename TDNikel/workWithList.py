#test = ['data post', 'post', 'a/m', 'mar', '150', '5']
#test = ['01.01.2020', 'post1', 'a/m258', 'ЖС6У', '158', '1', 'ЭП718', '205', '2', '', '', '0']
#element1 = 'dataDok'
#element2 = 'nDok'
from DB import dbinsert

def firstPartArr(a, n):
    mas=[]
    for i in range(n):
        mas.append(a[i])
    return mas

def secondPartArr(a, n):
    for i in range(n):
        a.remove(a[0])
    while ('' in a):
        a.remove('')
    #print(a)
    return a

def readyToDB(arr, element1, element2, count): # Описать Функцию пока не забыл
    '''Функция родготовки и отправки мфссива в БД'''
    #print(arr)
    a=firstPartArr(arr, 3)
    a=insertElement(a, 1, element1)
    a=insertElement(a, 2, element2)
    b=secondPartArr(arr,3)
    #x = int(len(b)/3)
    path2 = []
    for i in range(count):
        for z in range(3):
            path2.append(b[z])
        res = a + path2
        res =vesNetto(res)
        #print(res)  # Тут отправляем в БД
        addBD(res)
        path2 = []
        for s in range(3):
            b.remove(b[0])

'''Функция помещения значения в массив в нужное место'''
def insertElement (arr, nomberAfter, Element): # Вход: Массив, место помещения элемента, елемент
    a = firstPartArr(arr, nomberAfter) # Делим массив на две части по заданному элементу
    a.append(Element)
    #print(a)
    b = secondPartArr(arr, nomberAfter)
    #print(b)
    res = a+b
    return res #Выход: готовый массив

'''Функция расчета веса нетто'''
def vesNetto(arr):
    arr.reverse()
    a = arr[0]
    b = arr[1]
    #print(a)
    #print(b)
    if a == '0':
        arr.reverse()
        arr.append(b)
        return arr
    else:
        res = int(b)*(100-int(a))/100
       # print(int(res))
        arr.reverse()
        arr.append(int(res))
        return arr

def addBD(readyArr): # Неработает
    a = []
    # print(values)
    for i in readyArr:
        a.append(readyArr.get(i))
    print(a)
    dbinsert(a)
    print('Сохранено')

'''Тест'''

#testP = insertElement(test, 1, element1)
#testP = insertElement(insertElement(test, 1, element1), 2, element2)
#print(testP)
#print(vesNetto(testP))
#print(testP)
#readyToDB(test, element1, element2)

