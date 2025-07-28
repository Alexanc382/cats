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


def open_new_window():
    tag = tag_entry.get()

    img = load_image(url_my)  # функция в которую будет отправляться переменная url_my
    # и эта функция вернет картинку в переменную img
    if url_my:  # если переменная не пустая
        new_window = Toplevel()
        new_window.title('Картинка с котиком')
        new_window.geometry('600x480')
        label = Label(new_window, image=img)
        label.pack()
        label.image = img


def exit_file():
    window.destroy()



window = Tk()
window.title('Cats!')
window.geometry('800x600')



menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit_file)

tag_entry = Entry()
tag_entry.pack()

load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()


url_my = 'https://cataas.com/cat'



window.mainloop()
