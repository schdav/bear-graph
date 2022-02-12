# Bear Graph 🐻

![GitHub top language](https://img.shields.io/github/languages/top/schdav/bear-graph.svg)
![license](https://img.shields.io/github/license/schdav/bear-graph.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/schdav/bear-graph.svg)
![GitHub repo size in bytes](https://img.shields.io/github/repo-size/schdav/bear-graph.svg)

The missing graph generator for Bear notes

## Requirements

- [Python 3](https://www.python.org/)
- [pip](https://pip.pypa.io/)

## Development

Bear Graph uses [flake8](https://pypi.org/project/flake8/) and [pylint](https://pypi.org/project/pylint/).

## Usage

1. Run `pip install -r requirements.txt` to install all required packages.
2. Export all Bear notes (e. g. as text files) into a new directory.
3. Run `python bear_graph.py -d <directory with notes>`.
4. The graph will be created in the parent directory of the directory with notes.
