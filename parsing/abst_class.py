from abc import ABC,abstractmethod
from requests_html import HTMLSession
import json



class BaseInterface(ABC):
    def __init__(self,url):
        self._url = url

    def get_text(self):
        session = HTMLSession()
        data = session.get(self._url)
        return data



    def get_data(self):
        lines = self.get_text().html.find('.Z97G4e')
        for items in lines:
            res_headers = [i.text for i in items.find('.oVnAB')]
            res_body = [j.text for j in items.find('.bewvKb')]
            res = {key: value.split('\n') for key, value in zip(res_headers, res_body) if key != 'Популярное'}
            return res
        raise NotImplementedError('Method is not implemented')


    def save_data(self,file_name):
        with open(file_name, 'w', encoding='utf8') as file:
            json.dump(self.get_data(), file, indent=4, ensure_ascii=False)

