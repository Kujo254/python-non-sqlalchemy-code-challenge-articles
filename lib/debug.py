from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

if __name__ == "__main__":
    author1 = Author("Carry Bradshaw")
    mag1 = Magazine("Vogue", "Fashion")
    mag2 = Magazine("AD", "Architecture")

    article1 = author1.add_article(mag1, "How to wear a tutu with style")
    article2 = author1.add_article(mag2, "Dating life in NYC")

    print("Author:", author1.name)
    print("Magazines:", [m.name for m in author1.magazines()])
    print("Articles:", [a.title for a in author1.articles()])
    print("Topic areas:", author1.topic_areas())
