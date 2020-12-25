from tkinter import *
from tkinter import ttk

import sqlite3
from datetime import date
from random import randint
'''
from reportlab.pdfgen import canvas
#from reportlab.lib import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
import pprint
'''

root = Tk()

class Works():
    def clear(self):
        self.ent_cod.delete(0, END)
        self.ent_exp.delete(0, END)
        self.ent_rev.delete(0, END)
        self.ent_name.delete(0, END)
        self.ent_time.delete(0, END)

    def connect_bd(self):
        self.conn = sqlite3.connect('freelancer_manager.db')
        self.c = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def builds_tbs(self):
        self.connect_bd()
        print('Connecting with database.')
        try:
            self.c.execute(''' CREATE TABLE IF NOT EXISTS jobs (
                        ID INT PRIMARY KEY,
                        NAME TEXT NOT NULL,
                        REVENUES FLOAT NOT NULL,
                        SPENDING FLOAT NOT NULL,
                        PROFIT TEXT ,
                        PRICE_HOUR TEXT ,
                        DATE_CADASTER TEXT NOT NULL
                        )''')
            print('Table create with successful.')
            self.conn.commit()
        except Exception as e:
            print(e)
        self.disconnect()
        print('Disconnecting database.')

    def variables(self):
        self.id = randint(1, 99)
        self.name = self.ent_name.get()
        self.rev = float(self.ent_rev.get())
        self.spend = float(self.ent_exp.get())
        self.profit = float(self.rev - self.spend)
        self.profit_str = f'{self.profit:.2f}'
        self.time = float(self.ent_time.get())
        self.price_hour = float(self.profit / self.time)
        self.price_hour_str = f'{self.price_hour:.2f}'
        self.date = date.today()

    def new_job(self):
        self.variables()
        try:
            self.connect_bd()
            self.c.execute(''' INSERT INTO jobs (ID, NAME, REVENUES, SPENDING, PROFIT, PRICE_HOUR, DATE_CADASTER) VALUES
                        (?, ?, ?, ?, ?, ?, ?)''', (self.id, self.name, self.rev, self.spend, self.profit_str,
                                                   self.price_hour_str, self.date))
            self.conn.commit()
            print('Trabalho registrado com sucesso.')
            self.select()
            self.clear()
        except Exception as e:
            print(e)
        self.disconnect()

    def select(self):
        try:
            self.job_list.delete(*self.job_list.get_children())
            self.connect_bd()
            list1 = self.c.execute(''' SELECT ID, NAME, REVENUES, SPENDING, PROFIT, PRICE_HOUR, DATE_CADASTER
             FROM jobs ORDER BY NAME ASC;           
                    ''')
            for i in list1:
                self.job_list.insert("", END, values=i)
            self.disconnect()
        except Exception as e:
            print(e)
    '''
    def double_click(self):
        self.clear()
        self.job_list.selection()

        for n in self.job_list.selection():
            col1, col2, col3, col4, col5, col6, col7 = self.job_list.item(n, 'values')
            self.id.insert(END, col1)
            self.ent_name.insert(END, col2)
            self.ent_rev.insert(END, col3)
            self.ent_exp.insert(END, col4)
            self.profit_str.insert(END, col5)
            self.price_hour_str.insert(END, col6)
            self.date.insert(END, col7)
    '''
    def delete_job(self):
        try:
            self.connect_bd()
            self.c.execute(''' DELETE FROM jobs WHERE id = ?
                           ''', (int(self.ent_cod.get()),))
            self.conn.commit()
            self.disconnect()
            self.clear()
            self.select()
        except Exception as e:
            print(e)

    def edit_job(self):
        self.variables()
        try:
            self.connect_bd()
            self.c.execute('''
                    UPDATE jobs SET NAME = ?, REVENUES = ?, SPENDING = ? WHERE ID = ?
                    ''', (self.name, self.rev, self.spend, self.id))
            self.conn.commit()
            self.disconnect()
            self.clear()
            self.select()
        except Exception as e:
            print(e)


class Aplication(Works):
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_display()
        self.widgets_frame1()
        self.list_frame_2()
        self.builds_tbs()
        self.select()
        root.mainloop()

    def tela(self):
        self.root.title('Freelancer manager 1.0')
        self.root.configure(bg='#265F84')
        self.root.geometry('700x500+340+110')
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=600)
        self.root.minsize(width=550, height=350)

    def frame_display(self):
        self.frame_1 = Frame(self.root, bg='#93B8D1', bd=2, highlightbackground='#5F8FAE', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = Frame(self.root, bg='white', bd=2, highlightbackground='#5F8FAE', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def widgets_frame1(self):
        # Builds buttons
        self.bt_clear = Button(self.frame_1, text='Clear', bg='#3D7294', fg='white',
                               font=('verdana', 8, 'bold'), command=self.clear)
        self.bt_clear.place(relx=0.15, rely=0.1, relwidth=0.1, relheight=0.12)

        #self.bt_search = Button(self.frame_1, text='Search', bg='#3D7294', fg='white',
                               #font=('verdana', 8, 'bold'))
        #self.bt_search.place(relx=0.25, rely=0.1, relwidth=0.1, relheight=0.12)

        self.bt_add = Button(self.frame_1, text='New task', bg='#3D7294', fg='white',
                               font=('verdana', 8, 'bold'), command=self.new_job)
        self.bt_add.place(relx=0.7, rely=0.1, relwidth=0.12, relheight=0.12)

        #self.bt_edit = Button(self.frame_1, text='Edit task', bg='#3D7294', fg='white',
                               #font=('verdana', 8, 'bold'), command=self.edit_job)
        #self.bt_edit.place(relx=0.72, rely=0.1, relwidth=0.12, relheight=0.12)

        self.bt_del = Button(self.frame_1, text='Delete', bg='#3D7294', fg='white',
                               font=('verdana', 8, 'bold'), command=self.delete_job)
        self.bt_del.place(relx=0.84, rely=0.1, relwidth=0.12, relheight=0.12)

        # Builds labels and entries (id).
        self.lb_cod = Label(self.frame_1, text='ID',  bg='#93B8D1',
                               font=('verdana', 8, 'bold'))
        self.lb_cod.place(relx=0.05, rely=0.025, relwidth=0.08)
        self.ent_cod = Entry(self.frame_1)
        self.ent_cod.place(relx=0.05, rely=0.125, relwidth=0.08)

        # Builds labels and entries (name task).
        self.lb_name = Label(self.frame_1, text='Name of job:', bg='#93B8D1',
                               font=('verdana', 8, 'bold'))
        self.lb_name.place(relx=0.042, rely=0.495, relwidth=0.15, relheight=0.1)
        self.ent_name = Entry(self.frame_1)
        self.ent_name.place(relx=0.2, rely=0.5, relwidth=0.75, relheight=0.1)

        # Builds labels and entries (revenues)
        self.lb_rev = Label(self.frame_1, text='Revenues', bg='#93B8D1',
                               font=('verdana', 8, 'bold'))
        self.lb_rev.place(relx=0.05, rely=0.75, relwidth=0.2)
        self.ent_rev = Entry(self.frame_1)
        self.ent_rev.place(relx=0.05, rely=0.85, relwidth=0.2)


        # Builds labels and entries (expenses)
        self.lb_exp = Label(self.frame_1, text='Expenses', bg='#93B8D1',
                               font=('verdana', 8, 'bold'))
        self.lb_exp.place(relx=0.4, rely=0.75, relwidth=0.2)
        self.ent_exp = Entry(self.frame_1)
        self.ent_exp.place(relx=0.4, rely=0.85, relwidth=0.2)

        # Builds labels and entries (expenses)
        self.lb_time = Label(self.frame_1, text='Time spend', bg='#93B8D1',
                               font=('verdana', 8, 'bold'))
        self.lb_time.place(relx=0.75, rely=0.75, relwidth=0.2)
        self.ent_time = Entry(self.frame_1)
        self.ent_time.place(relx=0.75, rely=0.85, relwidth=0.2)

    def list_frame_2(self):
        self.job_list = ttk.Treeview(self.frame_2, height=3,
                                     column=('ID', 'NAME', 'REVENUES', 'SPENDING', 'PROFIT', 'PRICE HOUR',
                                             'DATE_CADASTER'))
        self.job_list.heading('#0', text='')
        self.job_list.heading('#1', text='ID')
        self.job_list.heading('#2', text='NAME')
        self.job_list.heading('#3', text='REVENUES')
        self.job_list.heading('#4', text='SPENDING')
        self.job_list.heading('#5', text='PROFIT')
        self.job_list.heading('#6', text='PRICE HOUR')
        self.job_list.heading('#7', text='DATE')

        self.job_list.column('#0', width=1)
        self.job_list.column('#1', width=50)
        self.job_list.column('#2', width=100)
        self.job_list.column('#3', width=80)
        self.job_list.column('#4', width=80)
        self.job_list.column('#5', width=80)
        self.job_list.column('#6', width=80)
        self.job_list.column('#7', width=80)

        self.job_list.place(relx=0.02, rely=0.03, relwidth=0.95, relheight=0.85)

        self.scrool_list = Scrollbar(self.frame_2, orient='vertical')
        self.job_list.configure(yscroll=self.scrool_list.set)
        self.scrool_list.place(relx=0.97, rely=0.03, relwidth=0.03, relheight=0.85)
        self.job_list.bind('<Double-1>', self.delete_job)


Aplication()

