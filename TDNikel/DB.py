import  sqlite3

def dbinsert(element):
    def sqlite3_create_db(con=None):
        print(1)
        con = sqlite3.connect('myDB.db')
        cur = con.cursor()
        cur.execute('CREATE  TABLE IF NOT EXISTS user(dataPost DATA,'
                    ' dataDok DATA,'
                    ' numberDok TEXT,'
                    ' partner TEXT,'
                    ' numberAM TEXT,'
                    ' nameMark TEXT,'
                    ' vesBrt REAL,'
                    ' zasor REAL,'
                    ' vesNet REAL,'
                    ' freeZona REAL)')
        con.commit()

        cur.execute('INSERT INTO user VALUES (?,?,?,?,?,?,?,?,?,?)', element)
        con.commit()

        cur.close()
        con.close()

    sqlite3_create_db()

def searchElement(element):
    '''Поправить передачу в функцию имя БД'''

    connect = sqlite3.connect('myDB.db')
    cursor = connect.cursor()
    query = 'SELECT vesNet FROM user WHERE  nameMark= ' + '"' + element + '"'

    cursor.execute(query)
    data = cursor.fetchall()

    new_data = []
    for i in data:
        new_data.append(i[0])
    data = new_data
    del(new_data)
    #print(len(data))
    #print('Всего записей марки: ' + element +' -' + str(len(data)) +' шт')

    #for i in range(len(data)):
    #    print(data[i])
    sumVes=sum(data)
    #print('Общий вес марки: '+ element + ' = ' + str(sumVes))
    cursor.close()
    connect.close()
    #print('БД - закрыта')
    return (str(sumVes))

'''Функция поиска значений из заданного столбца в БД по заданным данным из определенного столбца'''
def searchElementInBD(elementBD, elementFind, data ): # Вход: название столбца (str) из которого нужно получить данные
                                                      #       название стодбца (str) в котором происходит поиск
                                                      #       данные для столбца поиска

    connect = sqlite3.connect('myDB.db') # Подключение к БД
    cursor = connect.cursor() # Назначение курсора

    '''Формирование строки запроса  '''
    query = 'SELECT '+ elementBD +' FROM user WHERE ' + elementFind + '= ' + '"' + data + '"'
    #print((query))
    cursor.execute(query) # Отправляем сформированный запрос курсору
    data = cursor.fetchall() # На основании запроса получаем данные
    #print(data)
    ''' Приводим данные к типу с которым можем работать (Массив)'''
    new_data = []
    for i in data:
        new_data.append(i[0])
    data = new_data
    del (new_data)
    #print(data)
    cursor.close() # Оключение курсора
    connect.close() # Отключение от БД
    return data # Выход: Возвращаем масив нужных нам данных

'''Функция сортировки массива на предмет повторяющихся данных'''

def findRepitData(arrIn): # Вход массив для сортировки
    arrOut = []
    for i in arrIn:       # Перебираем значения во входящем массиве
           if i not in arrOut: #  Если в выходном массиве нет значения из входного
                arrOut.append(i) # Наполняем выходной массив
    #print(arrOut)
    return arrOut # Выход отсортированный массив



#test = searchElementInBD('numberDok', 'dataDok', '10.05.2020')
#print(test)
#findRepitData(test)

