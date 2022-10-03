from abc import ABC,abstractmethod
from requests_html import HTMLSession
import json



class BaseInterface(ABC):
    _res = None

    def __init__(self,url):
        self._url = url

    def get_data(self):
        session = HTMLSession()
        self._data_html = session.get(self._url)

    @abstractmethod
    def parse(self):
        ...

    def save_data(self,file_name):
        with open(file_name, 'w', encoding='utf8') as file:
            json.dump(self._res, file, indent=4, ensure_ascii=False)

