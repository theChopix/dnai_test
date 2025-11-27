from abc import ABC, abstractmethod
import numpy as np


class Loader(ABC):
    """Abstract base class for loading data."""
    @abstractmethod
    def load(self, path: str) -> np.ndarray:
        """Load data from the specified path.

        Args:
            path (str): The file path from which data should be loaded.

        Returns:
            np.ndarray: The loaded data.
        """
        ...