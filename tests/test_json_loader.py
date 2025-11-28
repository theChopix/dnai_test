import json
import numpy as np
import pytest

from clustering.io.loader.json_loader import JSONLoader


def test_json_loader_valid(tmp_path):
    """Loader should correctly read valid JSON containing 'data'."""
    path = tmp_path / "input.json"

    content = {"data": [[1, 2], [3, 4]]}
    path.write_text(json.dumps(content))

    loader = JSONLoader()
    result = loader.load(str(path))

    assert isinstance(result, np.ndarray)
    assert result.shape == (2, 2)
    assert result.tolist() == [[1, 2], [3, 4]]


def test_json_loader_missing_file():
    """Loader should raise FileNotFoundError if file does not exist."""
    loader = JSONLoader()
    with pytest.raises(FileNotFoundError):
        loader.load("non_existent_file.json")


def test_json_loader_invalid_json(tmp_path):
    """Loader should raise ValueError on invalid JSON content."""
    path = tmp_path / "bad.json"
    path.write_text("{invalid_json: }")  # intentionally invalid JSON

    loader = JSONLoader()
    with pytest.raises(ValueError):
        loader.load(str(path))


def test_json_loader_missing_data_key(tmp_path):
    """Loader should raise ValueError if 'data' key is missing."""
    path = tmp_path / "missing.json"
    path.write_text(json.dumps({"foo": [1, 2]}))

    loader = JSONLoader()
    with pytest.raises(ValueError):
        loader.load(str(path))
