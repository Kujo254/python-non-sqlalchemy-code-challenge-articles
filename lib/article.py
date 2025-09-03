from lib.author import Author
from lib.magazine import Magazine

class Article:
    all = []

    def __init__(self, author, magazine, title):
        if isinstance(author, Author) and isinstance(magazine, Magazine) and isinstance(title, str):
            if 5 <= len(title) <= 50:
                self._author = author
                self._magazine = magazine
                self._title = title
                Article.all.append(self)

    @property
    def title(self):
        # Immutable, no setter
        return getattr(self, "_title", None)

    @property
    def author(self):
        return getattr(self, "_author", None)

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return getattr(self, "_magazine", None)

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
