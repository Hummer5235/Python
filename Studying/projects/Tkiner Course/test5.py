from tkinter import *
from tkinter import messagebox


window = Tk()
window.title('Главное окно')
window.geometry('400x400')
messagebox.showwarning('Заголовок message','Внимание,внимание')

sub_window = Toplevel(master=window)
sub_window.title('Дочернее окно')
sub_window.geometry('300x200')
window.grab_set()


mainloop()



# mainloop()
