# модуль отправляет запросы в интернет и получать ответы
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO




#input/out ввод/вывод информации.
# Байт потому что картинки по запросу вернуться в виде байтов

def load_image(url_my):
    try:
        response = requests.get(url_my)
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


def exit_file():
    window.destroy()



window = Tk()
window.title('Cats!')
window.geometry('800x600')

label = Label()
label.pack()

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=set_image)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit_file)


url = 'https://cataas.com/cat'




set_image()

window.mainloop()
