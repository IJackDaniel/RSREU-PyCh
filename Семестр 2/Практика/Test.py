import tkinter as tk


window = tk.Tk()  # Создать окно
window.geometry("800x600")  # Задать размеры окна
window.resizable(False, False)  # Неизменность окна

###### КНОПКИ
btn1 = tk.Button(text="Выход")  # Создаём кнопку
btn1.place(x=200, y=300)  # Помещаем кнопку (левый верхний угол) в координаты
btn2 = tk.Button(text="Вход")  # Создаём кнопку
btn2.place(relx=0.5, rely=0.5)  # Помещаем кнопку (левый верхний угол) в
# место на экране в отношении
btn3 = tk.Button(window, text="Портал")  # Создаём кнопку
btn3.pack()  # Помещаем кнопку куда-то))))

##### Текст
lbl1 = tk.Label(window, width=20, text="Скуфы следят за тобой")
lbl1.pack()

##### Ввод текста
ent = tk.Entry(window, width=20)
ent.pack()

window.mainloop()  # Вывод окна приложения
