"""Strategy object that realizes the IngestInterface for docx files."""

from typing import List
import docx

from .IngestInterface import IngestInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestInterface):
    """A Docxingestor Class."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Classmethod returning QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception('File extension not allowed')

        quotes = list()
        doc = docx.Document(path)

        for line in doc.paragraphs:
            if line.text != "":
                parse = line.text.split(' - ')
                new_quote = QuoteModel(str(parse[0]), str(parse[1]))
                quotes.append(new_quote)

        return quotes
