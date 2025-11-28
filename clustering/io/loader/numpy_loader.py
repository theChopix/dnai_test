import numpy as np
from pathlib import Path

from .loader import Loader


class NumpyLoader(Loader):
    """Conrete implementation of Loader for NumPy .npy files."""
    def load(self, path: str) -> np.ndarray:
        """Load data from a NumPy .npy file.

        Args:
            path (str): The file path from which NumPy data should be loaded.
        
        Returns:
            np.ndarray: The loaded data.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        path_obj = Path(path)

        if not path_obj.exists():
            raise FileNotFoundError(f"Path does not exist: {path}")

        data = np.load(path)
        return data