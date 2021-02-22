"""Strategy object that realizes the IngestInterface for csv files."""

from typing import List
import pandas as pd

from .IngestInterface import IngestInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestInterface):
    """A CSVingestor Class."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Classmethod returning QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception('File extension not allowed')

        quotes = list()
        df = pd.read_csv(path)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
