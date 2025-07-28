# модуль отправляет запросы в интернет и получать ответы
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO




#input/out вход/выход информации.
# Байт потому что картинки по запросу вернуться в виде байтов

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None


def set_image():
    img = load_image(url)  # функция в которую будет отправляться переменная url
    # и эта функция вернет картинку в переменную img
    if img:  # если переменная не пустая
        label.config(image=img)
        label.image = img  # команда, чтобы 'сборщик мусора' Пайтона уберет эту картинку


window = Tk()
window.title('Cats!')
window.geometry('800x600')

label = Label()
label.pack()
url = 'https://cataas.com/cat'
img = load_image(url) # функция в которую будет отправляться переменная url
# и эта функция вернет картинку в переменную img
button_change_img = Button(text='Еще одного котика!', width=30, height=5, command=set_image)
button_change_img.pack(pady=50)

if img: # если переменная не пустая
    label.config(image=img,width = 600, height=400)
    label.image = img # команда, чтобы 'сборщик мусора' Пайтона уберет эту картинку

set_image()

window.mainloop()
