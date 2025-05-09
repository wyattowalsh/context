"""context/processors/base.py -- base processor class

This class defines the base processor class that all other processors should inherit from.
"""

from abc import ABC, abstractmethod


class BaseProcessor(ABC):
    """Base processor class that all other processors should inherit from."""

    @abstractmethod
    def process(self, data: Any) -> Any:
        """Process the data and return the processed data."""
