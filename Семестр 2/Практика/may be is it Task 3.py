import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mb
import os
import tempfile
from PIL import Image, ImageTk


storage_path = os.path.join(tempfile.gettempdir(), 'historyComputing.txt')


class Window(tk.TK):
    def __init__(self):
        super(Window, self).__init__()

        # Настройка окна
        self.title("Рассчёт цен на CorgiShop")
        self.iconbitmap(default=r"Images\icon.ico")
        self.geometry('320x450+600+200')
        self.resizable(False, False)

        # Выход из программы
        self.protocol("WM_DELETE_WINDOW", self.close_window)

        # Настройка главного меню
        mainmenu = tk.Menu(self)
        self.config(menu=mainmenu)

        # Создание выпадающих списков команд
        filemenu = tk.Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Открыть...", command=self.read_file_history)
        filemenu.add_separator()
        filemenu.add_command(label="Выход", command=self.close_window)
        helpmenu = tk.Menu(mainmenu, tearoff=0)
        helpmenu.add_command(label="О программе", command=self.program_description)
        helpmenu.add_command(label="Об авторе", command=self.about_show)

        # Подвязыванием экземпляры меню к главному меню
        mainmenu.add_cascade(label="Файл", menu=filemenu)
        mainmenu.add_cascade(label="Справка", menu=helpmenu)

        # Создание вкладок
        nb = ttk.Notebook(self)
        nb.pack(fill='both', expand=True)
        frame1 = tk.Frame(self)
        frame2 = tk.Frame(self)
        nb.add(frame1, text="Рассчёт цены")
        nb.add(frame2, text="Просмотр истории рассчётов")

        # Размещение виджетов на вкладке "Рассчёт цены"
        frame_prodType = tk.LabelFrame(frame1, text="Выберите товар")
        frame_prodType.place(x=15, y=10)

        frame_type = tk.LabelFrame(frame1, text="Тип одежды")
        frame_type.place(x=190, y=10)

        frame_result = tk.Frame(frame1)
        frame_result.place(x=15, y=320)

        frame_button = tk.Frame(frame1)
        frame_button.place(x=185, y=320)

        label_xs = tk.Label(frame_prodType, text="XS", font=("Times New Roman", 11), fg="blue")
        label_s = tk.Label(frame_prodType, text="S", font=("Times New Roman", 11), fg="blue")
        label_m = tk.Label(frame_prodType, text="M", font=("Times New Roman", 11), fg="blue")
        label_l = tk.Label(frame_prodType, text="L", font=("Times New Roman", 11), fg="blue")
        label_xl = tk.Label(frame_prodType, text="XL", font=("Times New Roman", 11), fg="blue")
        label_xxl = tk.Label(frame_prodType, text="XXL", font=("Times New Roman", 11), fg="blue")
        label_xxxl = tk.Label(frame_prodType, text="XXXL", font=("Times New Roman", 11), fg="blue")
        label_xs.grid(row=0, column=0, padx=5, pady=5)
        label_s.grid(row=1, column=0, padx=5, pady=5)
        label_m.grid(row=2, column=0, padx=5, pady=5)
        label_l.grid(row=3, column=0, padx=5, pady=5)
        label_xl.grid(row=4, column=0, padx=5, pady=5)
        label_xxl.grid(row=5, column=0, padx=5, pady=5)
        label_xxxl.grid(row=6, column=0, padx=5, pady=5)

        label_hat = tk.Label(frame_prodType, text="Count", font=("Times New Roman", 11), fg="blue")
        label_hat.grid(row=7, column=0, padx=5, pady=5)
        label_hat.grid_remove()

        entry_xs = tk.Entry(frame_prodType, width=10)
        entry_xs.grid(row=0, column=1, padx=5, pady=10)
        entry_s = tk.Entry(frame_prodType, width=10)
        entry_s.grid(row=1, column=1, padx=5, pady=10)
        entry_m = tk.Entry(frame_prodType, width=10)
        entry_m.grid(row=2, column=1, padx=5, pady=10)
        entry_l = tk.Entry(frame_prodType, width=10)
        entry_l.grid(row=3, column=1, padx=5, pady=10)
        entry_xl = tk.Entry(frame_prodType, width=10)
        entry_xl.grid(row=4, column=1, padx=5, pady=10)
        entry_xxl = tk.Entry(frame_prodType, width=10)
        entry_xxl.grid(row=5, column=1, padx=5, pady=10)
        entry_xxxl = tk.Entry(frame_prodType, width=10)
        entry_xxxl.grid(row=6, column=1, padx=5, pady=10)

        entry_hat = tk.Entry(frame_prodType, width=10)
        entry_hat.grid(row=7, column=1, padx=5, pady=10)
        entry_hat.grid_remove()

        rb_var = tk.IntVar()
        rb_var.set(0)

        rb_tshirt = tk.Radiobutton(frame_type, variable=rb_var, text="Футболка", value=0, command=self.radiobutton_change)
        rb_tshirt.grid(row=0, column=0, padx=5, pady=5)
        rb_sw = tk.Radiobutton(frame_type, variable=rb_var, text="Свитшот", value=1, command=self.radiobutton_change)
        rb_sw.grid(row=1, column=0, padx=5, pady=5)
        rb_hud = tk.Radiobutton(frame_type, variable=rb_var, text="Худи", value=2, command=self.radiobutton_change)
        rb_hud.grid(row=2, column=0, padx=5, pady=5)
        rb_pan = tk.Radiobutton(frame_type, variable=rb_var, text="Панамка", value=3, command=self.radiobutton_change)
        rb_pan.grid(row=3, column=0, padx=5, pady=5)
        rb_cap = tk.Radiobutton(frame_type, variable=rb_var, text="Кепка", value=4, command=self.radiobutton_change)
        rb_cap.grid(row=4, column=0, padx=5, pady=5)

        label_text = tk.Label(frame_result)
        label_text.grid(row=0, column=0)
        label_root = tk.Label(frame_result)
        label_root.grid(row=1, column=0)

        button_res = tk.Button(frame_button, width=12, text="Узнать цену", command=self.un_solution)
        button_res.grid(row=0, column=0, padx=5, pady=2)
        button_clear = tk.Button(frame_button, state='disabled', width=12, text="Очистить", command=self.data_clear)
        button_clear.grid(row=1, column=0, padx=5, pady=2)
        button_save = tk.Button(frame_button, state='disabled', width=12, text="Сохранить", command=self.save_file_history)
        button_save.grid(row=2, column=0, padx=5, pady=2)

        # Размещение виджетов на вкладке "Просмотр истории"
        # Многострочное текстовое поле с полосой прокрутки
        text = tk.Text(frame2, wrap=tk.WORD)
        scroll = tk.Scrollbar(frame2, command=text.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        text.config(yscrollcommand=scroll.set)
        text.pack(side=tk.LEFT)

        # Контекстное меню
        popupmenu = tk.Menu(tearoff=0)
        popupmenu.add_command(label="Очистить", command=self.history_clear)
        popupmenu.add_command(label="Показать историю", command=self.read_file_history)
        text.bind('<Button-3>', self.popup)

        # self.mainloop()

    def is_file_empty(self, file_path):
        with open(file_path, 'r') as file:
            if file.read().strip() == '':
                return True
            else:
                return False

    def close_window(self):
        """ Выход из приложения """
        if mb.askyesno("Выход", "Завершить работу?"):
            self.destroy()

    def program_description(self):
        """ Отображение окна О программе """
        mb.showinfo("О программе", "Программа позволяет вам рассчитать стоимость партий товаров в магазине CorgiShop")

    def about_show(self):
        """ Окно с информацией об авторе"""
        about = tk.Toplevel()
        about.title("Информация об авторе")
        about.geometry("500x500")
        about.resizable(False, False)
        myimage = ImageTk.PhotoImage(Image.open(r"Images\author.jpg"))
        label_image = tk.Label(about, image=myimage)
        label_image.pack()

        about.grab_set()
        about.focus_set()
        about.wait_window()

    def read_file_history(self):
        """ Отображение истории рассчётов цен """
        if not os.path.exists(storage_path) or self.is_file_empty(storage_path):
            mb.showinfo(title="Информация", message="Нет истории рассчётов")
        else:
            self.text.delete(1.0, tk.END)
            with open(storage_path, 'r') as f:
                self.text.insert(1.0, f.read())
            self.text.focus_set()

    def save_file_history(self):
        """ Запись результата в файл с историей рассчётов """
        if not os.path.exists(storage_path):
            f = open(storage_path, "w")
            f.close()
        with open(storage_path, 'a') as f:
            letter = self.label_text['text'] + '\n ' + self.label_root['text'] + '\n'
            f.writelines(letter)

    def radiobutton_change(self):
        """ Различные параметры в зависимости от выбора вида товара"""
        if self.rb_var.get() == 0 or self.rb_var.get() == 1 or self.rb_var.get() == 2:
            """ Скрытие элементов """
            self.entry_hat.grid_remove()
            self.label_hat.grid_remove()
            """ Отображение элементов """
            self.entry_xs.grid()
            self.entry_s.grid()
            self.entry_m.grid()
            self.entry_l.grid()
            self.entry_xl.grid()
            self.entry_xxl.grid()
            self.entry_xxxl.grid()
            self.label_xs.grid()
            self.label_s.grid()
            self.label_m.grid()
            self.label_l.grid()
            self.label_xl.grid()
            self.label_xxl.grid()
            self.label_xxxl.grid()
        elif self.rb_var.get() == 3 or self.rb_var.get() == 4:
            """ Скрытие элементов """
            self.entry_xs.grid_remove()
            self.label_xs.grid_remove()
            self.entry_s.grid_remove()
            self.label_s.grid_remove()
            self.entry_m.grid_remove()
            self.label_m.grid_remove()
            self.entry_l.grid_remove()
            self.label_l.grid_remove()
            self.entry_xl.grid_remove()
            self.label_xl.grid_remove()
            self.entry_xxl.grid_remove()
            self.label_xxl.grid_remove()
            self.entry_xxxl.grid_remove()
            self.label_xxxl.grid_remove()
            """ Отображение элементов """
            self.entry_hat.grid()
            self.label_hat.grid()
        self.data_clear()

    def popup(self, event):
        """ Определение выбора пункта контекстного меню """
        self.popupmenu.post(event.x_root, event.y_root)

    def history_clear(self):
        """ Очистка многострочного текстового поля """
        answer = mb.askyesno(title="Подтверждение действия", message="Очистить историю расчётов?")
        if answer:
            self.text.delete(1.0, tk.END)
            f = open(storage_path, "w")
            f.close()

    def data_clear(self):
        """ Очистка полей для ввода и поля с ценой """
        self.entry_xs.delete(0, tk.END)
        self.entry_s.delete(0, tk.END)
        self.entry_m.delete(0, tk.END)
        self.entry_l.delete(0, tk.END)
        self.entry_xl.delete(0, tk.END)
        self.entry_xxl.delete(0, tk.END)
        self.entry_xxxl.delete(0, tk.END)
        self.entry_hat.delete(0, tk.END)
        self.label_root['text'] = ''
        self.label_text['text'] = ''
        self.button_save['state'] = 'disable'
        self.button_clear['state'] = 'disable'

    def run_solution(self):
        """ Считывание параметров """
        global xs, s, m, l, xl, xxl, xxxl, hat
        name = ""
        try:
            if self.rb_var.get() == 0 or self.rb_var.get() == 1 or self.rb_var.get() == 2:
                xs = int(self.entry_xs.get()) if self.entry_xs.get() != "" else 0
                s = int(self.entry_s.get()) if self.entry_s.get() != "" else 0
                m = int(self.entry_m.get()) if self.entry_m.get() != "" else 0
                l = int(self.entry_l.get()) if self.entry_l.get() != "" else 0
                xl = int(self.entry_xl.get()) if self.entry_xl.get() != "" else 0
                xxl = int(self.entry_xxl.get()) if self.entry_xxl.get() != "" else 0
                xxxl = int(self.entry_xxxl.get()) if self.entry_xxxl.get() != "" else 0

            if self.rb_var.get() == 3 or self.rb_var.get() == 4:
                hat = int(self.entry_hat.get()) if self.entry_hat.get() != "" else 0
        except ValueError:
            mb.showerror('Ошибка!', 'Проверьте ввод!')
        except Exception:
            mb.showerror('Ошибка!', 'Непонятная ошибка.')
        else:
            if self.rb_var.get() == 0 or self.rb_var.get() == 1 or self.rb_var.get() == 2:
                cnt = xs + s + m + l + xl + xxl + xxxl
                type_prod = self.rb_var.get()
                self.cost(cnt, type_prod)
                match type_prod:
                    case 0:
                        name = "футболок"
                    case 1:
                        name = "свитшов"
                    case 2:
                        name = "худи"
                self.label_text['text'] = f"Цена для {cnt} {name}"
            else:
                cnt = hat
                type_prod = self.rb_var.get()
                self.cost(cnt, type_prod)
                match type_prod:
                    case 3:
                        name = "панамок"
                    case 4:
                        name = "кепок"
                self.label_text['text'] = f"Цена для {cnt} {name}"
            self.button_save['state'] = 'active'
            self.button_clear['state'] = 'active'

    def cost(self, cnt, type_pr):
        """ Поиск корней линейного и квадратного уравнения """
        cst = 0
        match type_pr:
            case 0:  # футболка
                if cnt >= 500:
                    cst = 600
                elif cnt >= 300:
                    cst = 800
                elif cnt >= 150:
                    cst = 1000
                elif cnt >= 50:
                    cst = 1100
                else:
                    cst = 1300
                self.label_root['text'] = f"{cst * cnt} рублей"
            case 1:  # свитшот
                if cnt >= 500:
                    cst = 1600
                elif cnt >= 300:
                    cst = 1800
                elif cnt >= 150:
                    cst = 2100
                elif cnt >= 50:
                    cst = 2300
                else:
                    cst = 2500
                self.label_root['text'] = f"{cst * cnt} рублей"
            case 2:  # худи
                if cnt >= 500:
                    cst = 1600
                elif cnt >= 300:
                    cst = 1800
                elif cnt >= 150:
                    cst = 2100
                elif cnt >= 50:
                    cst = 2300
                else:
                    cst = 2500
                self.label_root['text'] = f"{cst * cnt} рублей"
            case 3:  # панамка
                if cnt >= 500:
                    cst = 250
                elif cnt >= 300:
                    cst = 280
                elif cnt >= 150:
                    cst = 320
                elif cnt >= 50:
                    cst = 370
                else:
                    cst = 400
                self.label_root['text'] = f"{cst * cnt} рублей"
            case 4:  # кепка
                if cnt >= 500:
                    cst = 250
                elif cnt >= 300:
                    cst = 280
                elif cnt >= 150:
                    cst = 320
                elif cnt >= 50:
                    cst = 370
                else:
                    cst = 400
                self.label_root['text'] = f"{cst * cnt} рублей"


def application():
    window = Window()

    window.mainloop()


if __name__ == "__main__":
    application()
