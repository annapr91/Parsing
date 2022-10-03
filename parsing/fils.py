from .abst_class import BaseInterface

class Books(BaseInterface):
    def get_data(self):
        lines = self.get_text().html.find('.T4LgNb')


if __name__ == "__main__":
    main()