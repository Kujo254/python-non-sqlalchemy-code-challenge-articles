from lib.article import Article
from lib.magazine import Magazine

class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name.strip()) > 0:
            self._name = name

    @property
    def name(self):
        # Immutable, no setter
        return getattr(self, "_name", None)

    def articles(self):
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        return list({a.magazine for a in self.articles()})

    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine) and isinstance(title, str):
            return Article(self, magazine, title)

    def topic_areas(self):
        areas = {m.category for m in self.magazines()}
        return list(areas) if areas else None
