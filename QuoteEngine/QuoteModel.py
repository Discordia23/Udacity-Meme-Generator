"""Class QuoteModel initialized through the IngestInterface class."""


class QuoteModel():
    """A QuoteModel class."""

    def __init__(self, body, author):
        """Create a new quote."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return 'repr(self)'."""
        return f"'{self.body}' - {self.author}"
