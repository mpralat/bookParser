from book import Book

def test_read_book():
    book = Book('test/test_text_file.txt')
    book.read_book()
    chapters = book.get_chapters
    assert len(chapters) == 2
    assert chapters[0].get('title') == 'Chapter 1'
    sentences = chapters[0].get('sentences')
    assert len(sentences) == 4