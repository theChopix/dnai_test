import json
import numpy as np

from .saver import Saver


class JSONSaver(Saver):
    """Concrete implementation of Saver that saves data in JSON format."""
    def save(self, data: np.ndarray, path: str) -> None:
        """Save data to a JSON file at the specified path.

        Args:
            data: np.ndarray: The data to be saved.
            path (str): The file path where data should be saved.
        """
        data_to_save = {"labels": data.tolist()}
        with open(path, 'w') as json_file:
            json.dump(data_to_save, json_file, indent=4)