from abc import ABC, abstractmethod
import numpy as np


class Saver(ABC):
    """Abstract base class for saving data."""
    @abstractmethod
    def save(self, data: np.ndarray, path: str) -> None:
        """Save data to the specified path.

        Args:
            data: np.ndarray: The data to be saved.
            path (str): The file path where data should be saved.
        """
        ...