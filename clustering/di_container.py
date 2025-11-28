from dependency_injector import containers, providers
from dependency_injector.providers import Selector

from clustering.io.loader.loader import Loader
from clustering.io.saver.saver import Saver

from clustering.io.loader.json_loader import JSONLoader
from clustering.io.saver.json_saver import JSONSaver

from clustering.io.loader.numpy_loader import NumpyLoader
from clustering.io.saver.numpy_saver import NumpySaver


class Container(containers.DeclarativeContainer):
    """Dependency injection container for loaders and savers."""

    # configuration
    config = providers.Configuration()

    # available loaders
    json_loader: providers.Provider[Loader] = providers.Singleton(JSONLoader)
    numpy_loader: providers.Provider[Loader] = providers.Singleton(NumpyLoader)
    # singleton is fine since no state is captured in io classes

    # selection of loader based on config
    loader: Selector[Loader] = providers.Selector(
        config.input_format,
        json=json_loader,
        numpy=numpy_loader,
    )

    # available savers
    json_saver: providers.Provider[Saver] = providers.Singleton(JSONSaver)
    numpy_saver: providers.Provider[Saver] = providers.Singleton(NumpySaver) 
    # singleton is fine since no state is captured in io classes

    # selction of saver based on config
    saver: Selector[Saver] = providers.Selector(
        config.output_format,
        json=json_saver,
        numpy=numpy_saver,
    )

