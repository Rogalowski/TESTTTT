import exam_lib

class Book:
    """Represent the book.

    :param str title: book title
    :param str author: author name
    :param int pages: number of pages
    """
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def print_book_info(self):
        """
        Returns info about book.

        :rtype: str
        :return: info about book.
        """
        return (f"Book title: {self.title}\n"
                f"Book author: {self.author}\n"
                f"Number of pages: {self.pages}")


class Ebook(Book):
    def __init__(self, title, author, pages, size, registration_code): #czy tutaj nie powinna być _registration_code?
        super().__init__(title=title, author=author, pages=pages)

        self.size = size
        self._registration_code = registration_code if len(registration_code) == 16 and str(registration_code) else None #self.registration_code = _registration_code?? Ale czy też ostatecznie ukrycie nie powinno być z podwójną podłogą '__' zeby nie byla dostepna poza klasą ('na zewnątrz')?

    @staticmethod
    def check_code(registration_code):
        return registration_code if len(registration_code) == 16 and str(registration_code) else None #nie rozumiem dlaczego podwójnie sprawdzamy kod rejestracyjny jeśli mamy już go w __init__?

    @property
    def registration_code_getter(registration_code):    #zauwazylem ze nazwy definicji dla geetera i settera sa takie same u innych: def registration_code. Czy musi tak być, czy tak ja zrobiłem? Te same nazwy definicji zlewają się w kodzie i gdy ich używamy włąściwie nie ogarniam któ©ej aktualnie używam i po co.
        return registration_code

    # @registration_code.setter  #jak komentarz powyżej
    # def registration_code_setter(self, registration_code): #niektórzy używają innej  nazwy zmiennej po self, dlaczego w takim razie powinna być inna a nie tak jak w statycznej metodzie?
    #     return registration_code if len(registration_code) == 16 and str(registration_code) else None #nie rozumiem dlaczego potrójnie sprawdzamy kod rejestracyjny jeśli mamy już go w __init__ lub/i statycznej metodzie?

    @registration_code.setter  #name 'registration_code' is not defined nie wiem co tutaj zrobic zeby bylo dobrze. Proszę też odnieś sie do powyzszego zakomentowango settera. DLaczego nie moze byc tak
    def registration_code(self, registration_code_setter):
        if self.check_code(registration_code_setter):
            self._registration_code = registration_code_setter
        else:
            self._registration_code = None

if __name__ == "__main__":

    ebook1 = Ebook("Przygody", "Jan B", "12", "22MB", "2222222222222222")
    ebook2 = Ebook("Basnie", "Julian T", 55, "1MB", "12131")

    print(ebook1)
    print(ebook2)



