import numpy as np
import pytest

from clustering.io.loader.numpy_loader import NumpyLoader


def test_numpy_loader_valid(tmp_path):
    """Loader should correctly read valid .npy files."""
    path = tmp_path / "data.npy"
    original = np.array([[1, 2], [3, 4]])

    np.save(path, original)

    loader = NumpyLoader()
    result = loader.load(str(path))

    assert isinstance(result, np.ndarray)
    assert result.shape == (2, 2)
    assert result.tolist() == original.tolist()


def test_numpy_loader_missing_file():
    """Loader should raise FileNotFoundError if file does not exist."""
    loader = NumpyLoader()

    with pytest.raises(FileNotFoundError):
        loader.load("nonexistent.npy")