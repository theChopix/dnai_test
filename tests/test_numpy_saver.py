import numpy as np

from clustering.io.saver.numpy_saver import NumpySaver


def test_numpy_saver_valid(tmp_path):
    """Saver should correctly write numpy array to .npy file."""
    path = tmp_path / "output.npy"
    data = np.array([1, 2, 3])

    saver = NumpySaver()
    saver.save(data, str(path))

    # load back to verify
    loaded = np.load(path)

    assert isinstance(loaded, np.ndarray)
    assert loaded.tolist() == [1, 2, 3]


def test_numpy_saver_overwrites_file(tmp_path):
    """Saver should overwrite an existing file without errors."""
    path = tmp_path / "output.npy"

    # write something first
    np.save(path, np.array([99]))

    data = np.array([5, 6, 7])

    saver = NumpySaver()
    saver.save(data, str(path))

    loaded = np.load(path)
    assert loaded.tolist() == [5, 6, 7]