""" Module documentation """

import random
import tkinter


class X():
    """ class description """
    title = 'Main Menu'
    search_string = ''

    def __init__(self, main_window: tkinter.Tk):
        self.main_window = main_window
        self.main_window.title(self.title)
        self.add_menu()

    def add_menu(self):
        main_l1 = tkinter.Menu(self.main_window)
        self.main_window.config(menu=main_l1)
        main_l2 = tkinter.Menu(self.main_window)
        main_l1.add_cascade(label='File', menu=main_l2)
        main_l3 = tkinter.Menu(self.main_window)
        main_l2.add_cascade(label='New', menu=main_l3)
        main_l3.add_command(label='New Mail', command=self.new_mail)
        main_l3.add_command(label='New Mail in same Window', command=quit)
        main_l2.add_separator()
        main_l2.add_command(label='Close', command=quit)

    def new_mail(self):
        window_new = tkinter.Tk()
        new_window = MainMenu(window_new)
        new_title = self.title + ' Copy'
        new_window.main_window.title(new_title)

        lbl1 = tkinter.Label(self.main_window, text='To:')
        lbl1.grid(row=0, column=0, sticky=tkinter.E)
        lbl1 = tkinter.Label(self.main_window, text='From:')
        lbl1.grid(row=1, column=0, sticky=tkinter.E)
        lbl1 = tkinter.Label(self.main_window, text='Subject: ')
        lbl1.grid(row=2, column=0, sticky=tkinter.E)

        lbl1 = tkinter.Entry(self.main_window)
        lbl1.grid(row=0, column=1, sticky=tkinter.W)
        lbl1 = tkinter.Entry(self.main_window)
        lbl1.grid(row=1, column=1, sticky=tkinter.W)
        lbl1 = tkinter.Entry(self.main_window)
        lbl1.grid(row=2, column=1, sticky=tkinter.W)

        send = tkinter.Button(self.main_window, command=self.get_text, text='Send')
        send.grid(row=0, rowspan=3, column=2, sticky=tkinter.W)

        self.text = tkinter.Text(self.main_window, height=30, width=90)
        self.text.grid(row=3, columnspan=3)

        search = tkinter.Label(self.main_window, text='Search: ')
        search.grid(row=4, column=0, sticky=tkinter.E)
        self.search = tkinter.Entry(self.main_window)
        self.search.select_clear()
        self.search.bind('<KeyRelease>', self.search_text)
        self.search.grid(row=4, column=1, sticky=tkinter.W)

        self.main_window.quit()
        new_window.run()

    def run(self):
        self.main_window.mainloop()

    def get_text(self):
        print(self.text.get('0.0', tkinter.END))

    # pylint: disable=unused-argument
    def search_text(self, v: tkinter.Event):
        # self.search_string += v.char
        result = self.text.search(self.search.get(), '0.0', tkinter.END)
        try:
            row, col = result.split('.')
        except ValueError:
            pass
        self.text.tag_add('selection', result, f'{row}.{int(col) + len(self.search.get())}')
        self.text.tag_config('selection', background='yellow')

        print(result)


window = tkinter.Tk()
main_menu = X(window)
main_menu.run()
