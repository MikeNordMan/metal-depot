'''Тут разположены функции работы со строками сопроводительных'''
from workWithList import *

'''Функция добовления кол-ва строк'''
def visibleRow(x,y, window): # Вход: Счетчик открытых строк, кол-во возможных строк, наименование окна
   if x<y:
       x=x+1
       nu='col'+str(x)
       window.Element(nu).Update(visible=True)
       #  window.FindElement(nu).Update(visible=True)
       return x
   return x # Выход:  счетчик строк

'''Функция сокращения кол-ва строк'''
def visibleRowUn(x, window): # Вход: Счетчик открытых строк, наименование окна
   if x>0:
        nu='col'+str(x)
        window.Element(nu).Update(visible=False)
        x = x - 1
        return x
   return x # Выход:  счетчик строк

'''Функция сохранения данных из строк кол-ва строк'''
def messageSave(window, values, time, dok, count):
    #print(dok)
    #print(time)
    y = list(dict.values(values))
    #print(y)
    readyToDB(y, time, dok, int(count))
    #a=firstPartArr(y)
    #b=[]
   # b.append(a[0])
    #b.append(time)
   # b.append(dok)
   # b.append(a[1])
   # b.append(a[2])
   # print(b)
   # a = secondPartArr(y)
    #print(a)

  #  tl.readyToDB(tl.firstPartArr(y), tl.secondPartArr(y))
   # window.Element('txt').Update(message)
    #print(message)


def sumP(a, b):  # Функция расчета засора
    c=a*(100-b)/100
    return c
