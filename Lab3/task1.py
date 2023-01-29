class Book:
    def __init__(self, name, author):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f"Book: {self.name}, author: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.author!r})"

class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value):
        if isinstance(value, int) and value > 0:
            self.__pages = value
        else:
            raise ValueError("Pages must be a positive integer.")

    def __str__(self):
        return f"PaperBook: {self.name}, author: {self.author}, pages: {self.pages}"

class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__duration = value
        else:
            raise ValueError("Duration must be a positive number.")

    def __str__(self):
        return f"AudioBook: {self.name}, author: {self.author}, duration: {self.duration}"
