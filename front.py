from tkinter import *
from tkinter import ttk
from functools import partial
import classes


class GUI:
    def __init__(self):

        # Windows main
        self.window = Tk()
        # largura x altura + deslocamento da esquerda + deslocamento do topo
        self.window.geometry('400x300+500+100')


        def windows_delete():
            # Windows what delete jobs
            self.window.destroy()
            window_delete = Tk()
            window_delete.geometry('400x300+500+100')
            lb6 = Label(window_delete, text='FREELANCER MANAGER')
            lb6.place(x=140, y=20)
            window_delete.mainloop()

        def window_list_job():
            # Window for show jobs

            window_list_jobs = Tk()
            window_list_jobs.geometry('850x600+500+100')
            lb7 = Label(window_list_jobs, text='list')
            lb7.place(x=140, y=20)
            bt5 = Button(window_list_jobs, text='Exit', width=10)
            bt5.place(x=160, y=250)
            lstTree = ttk.Treeview(window_list_jobs, column=('col1', 'col2', 'col3', 'col4'))
            lstTree.place(x=5, y=8)
            lst = classes.Jobs().show_job()
            lb7['text'] = lst


        def bt_loading():
                name = str(et1.get())
                revenues = float(et2.get())
                expenses = float(et3.get())
                time_spend = float(et4.get())
                print(name, revenues, expenses, time_spend)
                job = classes.Jobs(name, revenues, expenses, time_spend)
                job.cadaster_job()

        def bt_list_jobs():
                window_list_job()


        def bt_delete():
                windows_delete()


        def bt_exit():
            self.window.destroy()


        # Widgets of window_main:
        # Labels
        lb1 = Label(self.window, text='FREELANCER MANAGER')
        lb1.place(x=140, y=20)

        lb2 = Label(self.window, text='Name: ')
        lb2.place(x=40, y=70)

        lb3 = Label(self.window, text='Revenues: ')
        lb3.place(x=40, y=110)

        lb4 = Label(self.window, text='Expenses: ')
        lb4.place(x=40, y=150)

        lb5 = Label(self.window, text='Time spend: ')
        lb5.place(x=40, y=190)

        # Button
        bt1 = Button(self.window, text='Add', width=10, command=bt_loading)
        #bt1['command'] = partial(bt_loading, bt1)
        bt1.place(x=25, y=250)

        bt2 = Button(self.window, text='List Jobs', width=10, command=bt_list_jobs)
        bt2.place(x=115, y=250)

        bt3 = Button(self.window, text='Delete', width=10, command=bt_delete)
        bt3.place(x=205, y=250)

        bt4 = Button(self.window, text='Exit', width=10, command=bt_exit)
        bt4.place(x=295, y=250)

        # Input Text
        et1 = Entry(self.window, width=30)
        et1.place(x=130, y=70)

        et2 = Entry(self.window, width=30)
        et2.place(x=130, y=110)

        et3 = Entry(self.window, width=30)
        et3.place(x=130, y=150)

        et4 = Entry(self.window, width=30)
        et4.place(x=130, y=190)

        self.window.mainloop()

