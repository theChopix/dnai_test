import numpy as np

from .saver import Saver


class NumpySaver(Saver):
    """Concrete implementation of Saver that saves data in NumPy .npy format."""
    def save(self, data: np.ndarray, path: str) -> None:
        """Save data to a NumPy .npy file at the specified path.

        Args:
            data: np.ndarray: The data to be saved.
            path (str): The file path where data should be saved.
        """
        np.save(path, data)