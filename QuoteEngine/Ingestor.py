"""Realize the IngestInterface abstract base class."""

from typing import List

from .IngestInterface import IngestInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .TextIngestor import TextIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestInterface):
    """A Ingestor class."""

    ingestors = [PDFIngestor, DocxIngestor, CSVIngestor, TextIngestor] 

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Classmethod depending on the ingestor."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
