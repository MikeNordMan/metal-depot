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
                    ' nameMark TEXT,'
                    ' vesBrt REAL,'
                    ' zasor REAL,'
                    ' vesNet REAL,'
                    ' freeZona REAL)')
        con.commit()

        cur.execute('INSERT INTO user VALUES (?,?,?,?,?,?,?,?,?)', element)
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