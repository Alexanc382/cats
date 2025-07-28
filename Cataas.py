# модуль отправляет запросы в интернет и получать ответы
from cProfile import label
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


#input/out вход/выход информации.
# Байт потому что картинки по запросу вернуться в виде байтов

window = Tk()
window.title('Cats!')
window.geometry('600x480')


label = Label()
label.pack()
url = 'https://cataas.com/cat'
img = load_image(url) # функция в которую будет отправляться переменная url
# и эта функция вернет картинку в переменную img

if img: # если переменная не пустая
    label.config(image=img)
    label.image = img # команда, чтобы 'сборщик мусора' Пайтона уберет эту картинку



window.mainloop()
