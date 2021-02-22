"""Definition of the Abstract Base Class with two methods."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestInterface(ABC):
    """Abstract base class."""

    allowed_extensions = list()

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Return if the quote file can be ingested."""
        extension = path.split('.')[-1]
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstracmethod - Definition in made into concrete class."""
        pass
