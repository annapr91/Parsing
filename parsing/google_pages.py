from .abst_class import BaseInterface

class Books(BaseInterface):
    def parse(self):
        lines = self._data_html.html.find('.Z97G4e')
        for items in lines:
            res_headers = [i.text for i in items.find('.oVnAB')]
            res_body = [j.text for j in items.find('.bewvKb')]
            self._res = {key: value.split('\n') for key, value in zip(res_headers, res_body) if key != 'Популярное'}



class ChildsGames(BaseInterface):
    def parse(self):
        lines = self._data_html.html.find('.Z97G4e')
        for items in lines:
            res_headers = [i.text for i in items.find('.oVnAB')]
            res_body = [j.text for j in items.find('.bewvKb')]
            self._res = {key: value.split('\n') for key, value in zip(res_headers, res_body) if key != 'Популярное'}



class Apps(BaseInterface):
    def parse(self):
        lines = self._data_html.html.find('.Z97G4e')
        for items in lines:
            res_headers = [i.text for i in items.find('.oVnAB')]
            res_body = [j.text for j in items.find('.bewvKb')]
            self._res = {key: value.split('\n') for key, value in zip(res_headers, res_body) if key != 'Популярное'}


class Games(BaseInterface):
    def parse(self):
        lines = self._data_html.html.find('.Z97G4e')
        for items in lines:
            res_headers = [i.text for i in items.find('.oVnAB')]
            res_body = [j.text for j in items.find('.bewvKb')]
            self._res = {key: value.split('\n') for key, value in zip(res_headers, res_body) if key != 'Популярное'}


