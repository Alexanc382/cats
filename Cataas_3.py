# модуль отправляет запросы в интернет и получать ответы
from tkinter import *
from tkinter import ttk # улучшенные виджеты
from PIL import Image, ImageTk
import requests
from io import BytesIO
#input/out ввод/вывод информации.
# Байт потому что картинки по запросу вернуться в виде байтов

Allowed_tags = [
    'sleep', 'jump', 'fight', 'black', 'white', 'red', 'siamese', 'bengal', 'angry'
]


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
    tag = tag_combobox.get() # получаем из выпад.списка
    url_with_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_with_tag)
    # img = load_image(url_my)  # функция в которую будет отправляться переменная url_my
    # # и эта функция вернет картинку в переменную img
    if url_my:  # если переменная не пустая
        new_window = Toplevel()
        new_window.title('Картинка с котиком')
        new_window.geometry('600x480')
        label = Label(new_window, image=img)
        label.pack()
        label.image = img


def open_random_cat():
    tag = tag_combobox.get() # получаем из выпад.списка
    url_random = 'https://cataas.com/cat'
    img = load_image(url_random)
    if url_random:  # если переменная не пустая
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

# frame1 = Frame(window) # бокс
# frame2 = Frame(window) # метка
# frame3 = Frame(window) # кнопка "загрузить"
# frame4 = Frame(window) # кнопка "случайный котик"
# frame1.pack()
# frame2.pack()
# frame3.pack()
# frame4.pack()

frame1 = Frame(window) # бокс, метка, кнопка "загрузить"
frame2 = Frame(window) # кнопка "случайный котик"
frame1.pack()
frame2.pack()

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit_file)



tag_combobox = ttk.Combobox(frame1, values=Allowed_tags)
tag_combobox.pack()
tag_label = Label(frame2, text='Выбери тег')
tag_label.pack()
load_button = ttk.Button(frame3, text='Загрузить по тегу', command=open_new_window)
load_button.pack()
random_button = ttk.Button(frame4, text='Случайный котик', command=open_random_cat)
random_button.pack()

url_my = 'https://cataas.com/cat'




window.mainloop()
