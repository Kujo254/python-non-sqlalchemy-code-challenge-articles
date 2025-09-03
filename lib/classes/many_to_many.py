class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name.strip()) > 0:
            self._name = name
        else:
            raise Exception("Name must be a non-empty string")

    @property
    def name(self):
        return getattr(self, "_name", None)

    @name.setter
    def name(self, value):
        # Immutable → ignore reassignment
        pass

    def articles(self):
        from classes.many_to_many import Article
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        from classes.many_to_many import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        return list({magazine.category for magazine in self.magazines()})


class Magazine:
    all = []

    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise Exception("Name must be a string between 2 and 16 chars")

        if isinstance(category, str) and len(category.strip()) > 0:
            self._category = category
        else:
            raise Exception("Category must be a non-empty string")

        Magazine.all.append(self)

    @property
    def name(self):
        return getattr(self, "_name", None)

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return getattr(self, "_category", None)

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._category = value

    def articles(self):
        from classes.many_to_many import Article
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [
            author for author in self.contributors()
            if len([article for article in self.articles() if article.author == author]) > 2
        ]
        return authors if authors else None

    @classmethod
    def top_publisher(cls):
        if not any(mag.articles() for mag in cls.all):
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))


class Article:
    all = []

    def __init__(self, author, magazine, title):
        from classes.many_to_many import Author, Magazine
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        if not (isinstance(title, str) and 5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 chars")

        self._author = author
        self._magazine = magazine
        self._title = title

        Article.all.append(self)

    @property
    def title(self):
        return getattr(self, "_title", None)

    @title.setter
    def title(self, value):
        # Immutable → ignore reassignment
        pass

    @property
    def author(self):
        return getattr(self, "_author", None)

    @author.setter
    def author(self, value):
        from classes.many_to_many import Author
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return getattr(self, "_magazine", None)

    @magazine.setter
    def magazine(self, value):
        from classes.many_to_many import Magazine
        if isinstance(value, Magazine):
            self._magazine = value
