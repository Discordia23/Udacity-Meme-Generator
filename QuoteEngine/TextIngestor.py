"""Strategy object that realizes the IngestInterface for text files."""

from typing import List

from .IngestInterface import IngestInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestInterface):
    """A TextIngestor Class."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Classmethod returning QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception('File extension not allowed')

        quotes = list()

        with open(path, 'r') as infile:
            for line in infile:
                quote, author = line.split('-')
                new_quote = QuoteModel(quote, author)
                quotes.append(new_quote)

        return quotes
