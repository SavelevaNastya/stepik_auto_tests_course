class MainPage(BasePage): # наследник класса BasePage. Класс-предок в Python указывается в скобках
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs) # Конструктор с ключевым словом super только вызывает конструктор класса предка 
                                                        # и передает ему все те аргументы, которые мы передали в конструктор MainPage. 