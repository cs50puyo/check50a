import click
import subprocess
import sys

from clint.textui import colored, puts
from os import listdir
from os.path import isfile, join


def generate_results(input, output, py_file):
    with open(input) as infile:
        with open(output, 'w') as outfile:
            subprocess.call(['python', py_file],
                            stdin=infile,
                            stdout=outfile)


def compare_results(expected, actual):
    correct = True
    with open(expected) as expected, open(actual) as actual:
        expected_str = ''
        actual_str = ''
        for e, a in zip(expected.read(), actual.read()):
            expected_str += e
            actual_str += a
            if e != a:
                correct = False
                break

    return correct, expected_str, actual_str


def report_results(correct, expected_str, actual_str):
    if correct:
        puts(colored.green('Solution is correct!'))
    else:
        puts(colored.red('Incorrect!'))

        print(f'Expected output:\n{expected_str}\n\n'\
              f'Actual output:\n{actual_str}')


def get_files_from_path(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    files.sort()
    return files


@click.command()
@click.argument('assignment')
@click.argument('exercise')
def main(assignment, exercise):
    path = join('inputs', assignment, exercise[:-3])
    inputs = get_files_from_path(path)

    for input in inputs:
        solution = join('solutions', assignment, exercise)
        expected = 'expected.txt'
        actual = 'actual.txt'
        input = join(path, input)

        generate_results(input, expected, solution)
        generate_results(input, actual, exercise)
        report_results(*compare_results(expected, actual))


if __name__ == "__main__":
    main()
