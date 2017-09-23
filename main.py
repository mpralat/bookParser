from book import Book
from bokeh.plotting import figure, output_file, show
import glob
import os


book_dir = "agatha_project"
all_books = []

def parse_all_books():
    for file in glob.glob("{}/*.txt".format(book_dir)):
        print("Parsing... {}".format(file))
        book = Book(file)
        book.read_book()
        book.count_distinct_words()
        print(book)

        all_books.append(book)

def print_word_count_per_year():
    years = [book.get_year for book in all_books]
    word_counts = [book.get_distinct_words/book.get_words for book in all_books]

    years, word_counts = zip(*sorted(zip(years, word_counts)))

    output_file('books.html')

    # p = figure(title='test', x_axis_label='years', y_axis_label='words')
    p = figure(plot_width=400, plot_height=400)
    p.vbar(x=range(len(years)), width=0.5, bottom=0,
           top=word_counts, color="firebrick")

    # p.line(years, word_counts, line_width=2)

    show(p)

parse_all_books()
print_word_count_per_year()
