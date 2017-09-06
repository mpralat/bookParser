from book import Book
import glob
import os

book_dir = "agatha_project"
all_books = []

def parse_all_books():
    for file in glob.glob("{}/*.txt".format(book_dir)):
        print("Parsing...{}".format(file))
        book = Book(file)
        all_books.append(book)
        book.read_book()
        book.count_distinct_words()

parse_all_books()
