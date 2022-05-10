import random
import tkinter


class MainMenu():
    title = 'Main Menu'

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
        window = tkinter.Tk()
        new_window = MainMenu(window)
        new_title = self.title + ' Copy'
        new_window.main_window.title(new_title)

        l1 = tkinter.Label(self.main_window, text='To:')
        l1.grid(row=0, column=0, sticky=tkinter.E)
        l1 = tkinter.Label(self.main_window, text='From:')
        l1.grid(row=1, column=0, sticky=tkinter.E)
        l1 = tkinter.Label(self.main_window, text='Subject: ')
        l1.grid(row=2, column=0, sticky=tkinter.E)

        l1 = tkinter.Entry(self.main_window)
        l1.grid(row=0, column=1, sticky=tkinter.W)
        l1 = tkinter.Entry(self.main_window)
        l1.grid(row=1, column=1, sticky=tkinter.W)
        l1 = tkinter.Entry(self.main_window)
        l1.grid(row=2, column=1, sticky=tkinter.W)

        send = tkinter.Button(self.main_window, command=quit, text='Send')
        send.grid(row=0, rowspan=3, column=2, sticky=tkinter.W)

        text = tkinter.Text(self.main_window, height=30, width=90)
        text.grid(row=3, columnspan=3)

        self.main_window.quit()
        new_window.run()

    def run(self):
        self.main_window.mainloop()


window = tkinter.Tk()
main_menu = MainMenu(window)
main_menu.run()
