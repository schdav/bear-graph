import argparse
import errno
import os
import sys
import unicodedata
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

__version__ = '0.0.1'


def main():
    parser = argparse.ArgumentParser(
        description='graph generator for bear notes',
        epilog='further help: https://github.com/schdav/bear-graph')
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-d',
                       '--dir',
                       help='directory with notes',
                       metavar=('NAME'))
    parser.add_argument('-v',
                        '--version',
                        action='version',
                        version=__version__)

    args = parser.parse_args()

    if args.dir:
        process_directory(args.dir)


def compare_strings(string_1, string_2):
    def nfd(string):
        return unicodedata.normalize('NFD', string)

    return nfd(string_1) in nfd(string_2)


def process_directory(path):
    try:
        os.chdir(path)
    except OSError as error:
        if error.errno == errno.ENOENT:
            print('can not find directory')
            sys.exit(1)

    notes = os.listdir('.')
    graph = nx.Graph()

    for note in notes:
        if os.path.isfile(note) and not note.startswith('.'):
            note_name = Path(note).stem
            graph.add_node(note_name)

            for reference in notes:
                if os.path.isfile(reference) and not reference.startswith('.'):
                    reference_name = Path(reference).stem
                    with open(note, 'r', encoding='utf-8') as content:
                        for line in content.readlines():
                            if compare_strings('[[' + reference_name + ']]', line):
                                graph.add_edge(note_name, reference_name)

    nx.draw_random(graph, node_size=50, node_color='#00ADB5')
    plt.savefig('../graph.png')


if __name__ == '__main__':
    main()
