import json
import numpy as np
from pathlib import Path

from .loader import Loader


class JSONLoader(Loader):
    """Loader for JSON files."""
    def load(self, path: str) -> np.ndarray:
        """Load data from a JSON file.

        Args:
            path (str): The file path from which JSON data should be loaded.

        Returns:
            np.ndarray: The loaded data.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If JSON contents are invalid or incorrectly formatted.
        """
        path_obj = Path(path)

        if not path_obj.exists():
            raise FileNotFoundError(f"Path does not exist: {path}")

        try:
            with path_obj.open("r") as file:
                data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON content in {path}: {e}") from e

        if "data" not in data:
            raise ValueError(f"Missing 'data' key in JSON file: {path}")

        return np.array(data["data"])