from datetime import date
import back
from random import randint


class Jobs:
    '''
    Classe voltada para registro de trabalhos freelancers.
    '''

    def __init__(self, name_job='txt', revenues=0, spending=0, time_spent=0):
        self._name_job = name_job
        self._id_job = int()
        self._date_cadaster = date.today()
        self._revenues = revenues
        self._spending = spending
        self._time_spent = time_spent
        self._profit_float = self._revenues - self._spending
        self._profit_str = f'{self._profit_float:.2f}'
        self._price_hour_float = self._profit_float / self._time_spent
        self._price_hour_str = f'{self._price_hour_float}'

        back.create_table()

    def cadaster_job(self):
        self._id_job = randint(1, 99)
        back.write(self._id_job, self._name_job, self._revenues, self._spending, self._profit_str, self._price_hour_str, self._date_cadaster)

    def delete_job(self, id):
        back.delete(id)

    def alterar_job(self, NOME, ID):
        back.alter(NOME, ID)

    def select_job(self, id):
        back.select(id)

    def show_job(self):
        back.show_all()
