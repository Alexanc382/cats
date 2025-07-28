# модуль отправляет запросы в интернет и получать ответы
from cProfile import label
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

from bottle import response


#input/out вход/выход информации.
# Байт потому что картинки по запросу вернуться в виде байтов

def load_image(url):
    try:
        response = requests.get
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None


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
