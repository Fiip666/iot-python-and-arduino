import requests
import time
from tkinter import *
global chek
global window
global chek
key = '****************'  # ключ
board = '****************'  # Название панели
variable = '**************'  # значение
def read(key, board, variable):
        """Читаем из переменной на сайте"""
        response = requests.post("http://iocontrol.ru/api/readData/"+ board + "/" + variable + "?key="+key)
        result = response.json()  # encoding dic
        return result.get('value')  # функция возвращает значение и дату

def send(key,board,send_variable):
    """Пишем в переменную на сайте"""
    requests.post("http://iocontrol.ru/api/sendData/" +board + "/" +variable+ "/"+ send_variable +"?key=" +key)



def cliced_start_send():
    """Обработка нажатия и отправка для старта на сайт"""
    send(key, board, send_variable = '2')
    chek_read()
def cliced_stop_send():
    send(key, board, send_variable = '1')
    chek_read()


def chek_read():
    """Чтение пременной с сайта и проверка состояния"""
    chek = read(key, board, variable)
    if chek == '1':
        lbl.configure(text="СОСТОЯНИЕ ПРИВОДА:\nДвигатель остановлен",height = 5, fg='green',font=(None, 15))
    if chek == '2':
        lbl.configure(text="СОСТОЯНИЕ ПРИВОДА:\nВНИМАНИЕ!\nДвигатель запущен!",height = 5, fg='red',font=(None, 15))


#Графическая оболочка

window = Tk()
window.title("Удаленное управление")
lbl = Label(window)
lbl.grid(column=1, row=3)
window.geometry('455x250')
window.resizable(width=False, height=False)

btn = Button(window, text="Запустить двигатель", height = 5,font=(None, 15),  fg ="green", command=cliced_start_send)
btn2 = Button(window, text="Остановить двигатель",height = 5,font=(None, 15),  fg = 'red',  command=cliced_stop_send)
btn2.grid(column=1, row=0)
btn.grid(column=2, row=0)
while True:
    """Переодическое обновление состояния привода"""
    if read(key, board, variable) == '1':
        lbl.configure(text="СОСТОЯНИЕ ПРИВОДА:\n Двигатель остановлен",font=(None, 15),height = 5, fg='green')
    if read(key, board, variable) == '2':
        lbl.configure(text="СОСТОЯНИЕ ПРИВОДА:\nВНИМАНИЕ!\nДвигатель запущен!",font=(None, 15),height = 5, fg='red')
    time.sleep(1)
    window.update()






