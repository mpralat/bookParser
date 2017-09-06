import nltk
import re

ROMAN_NUMBERS_PATTERN = 'M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})'


class Book:
    def __init__(self, path: str, encoding: str="ISO-8859-1"):
        self._path = path
        self._chapters = []
        self._encoding = encoding
        self._word_count = 0

    def read_book(self) -> None:
        with open(self._path, 'r', encoding = self._encoding) as file:
            text = file.read()
            sentences = nltk.sent_tokenize(text)

        for sent in sentences:
            chapter_regex = re.search(r'Chapter (?:[0-9]+|{})'.format(ROMAN_NUMBERS_PATTERN), sent, re.IGNORECASE)
            if chapter_regex:
                chapter_title = chapter_regex.group(0)
                self._chapters.append({'title': chapter_title, 'sentences': [], 'words': 0, 'sentiment': 0})
                sent = sent.replace(chapter_title, '')
            else:
                if not self._chapters:
                    continue
            self._word_count += len(sent)
            self._chapters[-1].get('sentences').append(sent)
            self._chapters[-1]['words'] += len(sent.split(' '))
    @property
    def get_chapters(self):
        return self._chapters

    def count_distinct_words(self):
        sentences_in_chapter = [chapter.get('sentences') for chapter in self._chapters]
        distinct_words = set(item for sentences in sentences_in_chapter for sentence in sentences for item in sentence.split(' '))
        print(len(distinct_words))
        leng = sum(chapter.get('words') for chapter in self._chapters)
        print(leng)
        self._distinct_words_count = len(distinct_words)
