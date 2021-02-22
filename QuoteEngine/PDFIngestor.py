"""Strategy object that realizes the IngestInterface for pdf files."""

from typing import List
import subprocess
import os
import random

from .IngestInterface import IngestInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestInterface):
    """A PDFIngestor Class."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Classmethod returning QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception('File extension not allowed')

        tmp = f'{random.randint(0, 10000000)}.txt'
        call = subprocess.call(
                'pdftotext ' + '-layout ' + str(path) + ' ' + str(tmp),
                shell=True)

        quotes = list()
        quotes_ref = open(tmp, 'r')

        for line in quotes_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                quote, author = line.split(' - ')
                new_quote = QuoteModel(quote, author)
                quotes.append(new_quote)

        quotes_ref.close()

        os.remove(tmp)

        return quotes
