import tkinter

main_window = tkinter.Tk()
main_window.title('MyApp')
label1 = tkinter.Label(main_window, text='RED Text', bg='red')
label1.grid(row=0, column=0)
label1.config(font=('Times New Roman', 30))
label2 = tkinter.Label(main_window, text='Green Text', bg='green')
label2.grid(row=100, column=0)
label2.config(width=50)
label3 = tkinter.Label(main_window, text='BLUE Text', bg='blue')
label3.grid(row=100, column=100)
label4 = tkinter.Label(main_window, text='Yellow Text', bg='yellow')
label4.grid(row=101, column=101)
label5 = tkinter.Label(main_window, text='Magenta Text', bg='magenta')
label5.grid(row=55, column=55)

main_window.mainloop()
print('all done')
