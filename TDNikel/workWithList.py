def firstPartArr(a):
    mas=[]
    for i in range(3):
        mas.append(a[i])
    return mas

def secondPartArr(a):
    for i in range(3):
        a.remove(a[0])
    while ('' in a):
        a.remove('')
    #print(a)
    return a

def readyToDB(b, a):

    x = int(len(a) / 3)
    for t in range(x):
        for i in range(3):
            b.append(a[i])
        for s in range(3):
            a.remove(a[0])
        b.append('t') # Работает нужно допилить функцию
        print(b) # тут отправляем в базу
        b.reverse()
        for z in range(3):
            b.remove(b[0])
        b.reverse()