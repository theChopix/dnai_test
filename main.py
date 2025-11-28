import click

from clustering.di_container import Container

@click.command()
@click.option("--config", default="config.yaml", help="Path to config file.")
@click.option("--input", required=True, help="Input data (JSON or NumPy).")
@click.option("--output", required=True, help="Output file path.")
def run(config, input, output):

    # set up DI container
    container = Container()
    container.config.from_yaml(config)

    loader = container.loader()
    saver = container.saver()

    # load data using the loader from configured DI container
    data = loader.load(input)

    # for demonstration purposes, just save the data back
    saver.save(data, output)

    # for demonstration purposes, just print the parameters
    click.echo(f"Config file: {config}, Input file: {input}, Output file: {output}")


if __name__ == "__main__":
    run()