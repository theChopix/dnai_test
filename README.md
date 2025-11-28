# Data Clustering CLI Tool

This project is a command-line tool for performing data clustering using **scikit-learn**. The tool supports multiple clustering algorithms, configurable hyperparameters, and flexible input/output formats. It uses **Dependency Injector** for modular component management and **pre-commit hooks** to ensure consistent code quality. Configuration is fully managed through a **config.yaml** file, allowing seamless switching between clustering strategies without modifying code.



## Development Setup

### Makefile

This project uses a simple `Makefile` utilizing `pip-tools` to manage Python dependencies in a **local virtual environment**. 

#### Makefile commands

```bash
make install_dev
```
Create the `.venv` virtual environment, install `pip-tools`, and install dependencies from `requirements.txt`.

```bash
make compile
```
Compiles dependencies from `pyproject.toml` into a pinned `requirements.txt` using `pip-tools`.

```bash
make sync
```
Synchronizes your virtual environment with the exact versions listed in `requirements.txt`.

```bash
make up
```
Runs both `compile` and `sync` - updating and installing dependencies in one step.

### Pre-commit Setup

This project uses **pre-commit** to run code quality checks such as ruff and mypy before each commit.

After installing the dependencies from `requirements.txt`, install pre-commit (only needed once per clone):

```bash
pre-commit install
```

### Testing Setup

To execute each of the tests in the `tests` folder, execute command:
```
PYTHONPATH=. pytest
```

## Usage

The tool is executed through the command line using the main.py entry point.
It accepts the following parameters:

- `--config` — Path to the configuration file (default: config.yaml)

- `--input` — Path to the input data file (JSON or NumPy - ) (required)

- `--output` — Path where the output should be saved (required)

```
python main.py --input data.json --output result.json
```

Since `--config` has a default, it may be omitted.
To specify a custom configuration file:

```
python main.py --config config.yaml --input data.json --output result.npy
```