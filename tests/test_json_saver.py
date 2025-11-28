import json
import numpy as np

from clustering.io.saver.json_saver import JSONSaver


def test_json_saver_valid(tmp_path):
    """Saver should correctly write labels to JSON file."""
    path = tmp_path / "output.json"

    data = np.array([0, 1, 2])

    saver = JSONSaver()
    saver.save(data, str(path))

    # read file back
    with path.open("r") as f:
        saved_content = json.load(f)

    assert "labels" in saved_content
    assert saved_content["labels"] == [0, 1, 2]


def test_json_saver_overwrites_file(tmp_path):
    """Saver should overwrite an existing file without errors."""
    path = tmp_path / "output.json"

    # write some garbage first
    path.write_text("gibberish")

    data = np.array([5, 6])

    saver = JSONSaver()
    saver.save(data, str(path))

    with path.open("r") as f:
        saved_content = json.load(f)

    assert saved_content["labels"] == [5, 6]
