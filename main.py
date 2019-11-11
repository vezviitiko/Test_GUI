print('start GUI')
import tkinter as tk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        #toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_settings = tk.PhotoImage(file="settings.gif")
        #btn_open_dialog = tk.Button(toolbar, text='Настройки', command=self.open_dialog, bg='#d7d8e0', bd=0,
        btn_open_dialog = tk.Button(toolbar, command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_settings)
        btn_open_dialog.pack(padx = 5, pady = 5, side=tk.LEFT)

        self.add_start = tk.PhotoImage(file="start.gif")
        btn_open_dialog_start = tk.Button(toolbar, bg='#d7d8e0', bd=0, compound=tk.TOP, image=self.add_start)
        btn_open_dialog_start.pack(padx = 5, pady = 5, side=tk.LEFT)

        self.add_stop = tk.PhotoImage(file="stop.gif")
        btn_open_dialog_stop = tk.Button(toolbar, bg='#d7d8e0', bd=0, compound=tk.TOP, image=self.add_stop)
        btn_open_dialog_stop.pack(padx = 5, pady = 5, side=tk.LEFT)

    def open_dialog(self):
        Child()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Настройки')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        self.grab_set()# невзаимодействие с главным окном
        self.focus_set()# захват и удержание фокуса

def insert():
    e1.insert(0, "Tkinter - GUI ")

def cbc(id, tex):
    return lambda : callback(id, tex)

def callback(id, tex):
    s = 'At {} f is {}\n'.format(id, id**id/0.987)
    tex.insert(tk.END, s)
    tex.see(tk.END)             # Scroll if necessary

# python imagery library - работа с изображениями
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Главное меню")
    root.geometry("1000x800+300+200")
    root.resizable(False, False)

    img = tk.PhotoImage(file="foto.gif")
    button = tk.Button(root, image=img)
    button.pack()

    #tk.Button(text="Вставить", command=insert).pack()
    #e1 = tk.Entry(width=50)
    #l1 = tk.Label(text="Машинное обучение", font="Arial 32")

    l2 = tk.Label(text="Отчет работы:\n", font="Arial 32" )
    l2.pack(expand=1, anchor=tk.SE)
    #l1.config(bd=20, bg='#ffaaaa')
    #l1.pack()
    #e1.pack(expand=1, anchor=tk.E)

    tex = tk.Text()
    tex.pack(side=tk.RIGHT)
    bop = tk.Frame()
    bop.pack(side=tk.LEFT)
    for k in range(1, 10):
        tv = 'Say {}'.format(k)
        b = tk.Button(bop, text=tv, command=cbc(k, tex))
        b.pack()

    #tk.Button(bop, text='Exit', command=tk.Tk().destroy).pack()


    root.mainloop()
