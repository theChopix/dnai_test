import pytest
from dependency_injector.errors import Error as DIError

from clustering.di_container import Container
from clustering.io.loader.json_loader import JSONLoader
from clustering.io.loader.numpy_loader import NumpyLoader
from clustering.io.saver.json_saver import JSONSaver
from clustering.io.saver.numpy_saver import NumpySaver


def test_container_selects_json_loader_and_saver():
    """Container should return JSON loader and saver when config is json."""
    container = Container()
    container.config.from_dict({
        "input_format": "json",
        "output_format": "json"
    })

    loader = container.loader()
    saver = container.saver()

    assert isinstance(loader, JSONLoader)
    assert isinstance(saver, JSONSaver)


def test_container_selects_numpy_loader_and_saver():
    """Container should return NumPy loader and saver when config is numpy."""
    container = Container()
    container.config.from_dict({
        "input_format": "numpy",
        "output_format": "numpy"
    })

    loader = container.loader()
    saver = container.saver()

    assert isinstance(loader, NumpyLoader)
    assert isinstance(saver, NumpySaver)


def test_container_invalid_input_format_raises_error():
    """Invalid input_format should raise dependency injector OptionNotFoundError."""
    container = Container()
    container.config.from_dict({
        "input_format": "invalid_value",
        "output_format": "json"
    })

    with pytest.raises(DIError):
        container.loader()


def test_container_invalid_output_format_raises_error():
    """Invalid output_format should raise dependency injector OptionNotFoundError."""
    container = Container()
    container.config.from_dict({
        "input_format": "json",
        "output_format": "invalid_value"
    })

    with pytest.raises(DIError):
        container.saver()