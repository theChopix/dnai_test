import click


@click.command()
@click.option("--config", default="config.yaml", help="Path to config file.")
@click.option("--input", required=True, help="Input data (JSON or NumPy).")
@click.option("--output", required=True, help="Output file path.")
def run(config, input, output):

    # for demonstration purposes, just print the parameters
    click.echo(f"Config file: {config}, Input file: {input}, Output file: {output}")


if __name__ == "__main__":
    run()