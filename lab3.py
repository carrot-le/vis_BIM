class Book:
    """Основной класс, представляющий книгу."""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Название: '{self.name}', Автор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(Название={self.name!r}, Автор={self.author!r})"


class PaperBook(Book):
    """Класс, описывающий бумажную книгу."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Число страниц должно быть целым и больше нуля.")
        self._pages = value

    def __str__(self):
        return f"'{self.name}' ({self.author}) - {self.pages} страниц"


class AudioBook(Book):
    """Класс для аудиокниг."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Длительность должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        return f"'{self.name}' ({self.author}) - Длительность: {self.duration} ч."