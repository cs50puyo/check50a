import click
import os
import subprocess
import sys

from clint.textui import colored, puts


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
        print('Expected output:')
        print(expected_str)
        print()
        print('Actual output:')
        print(actual_str)


@click.command()
@click.argument('assignment')
@click.argument('exercise')
def main(assignment, exercise):
    input = os.path.join('inputs', assignment, exercise[:-2] + 'txt')
    solution = os.path.join('solutions', assignment, exercise)
    expected = 'expected.txt'
    actual = 'actual.txt'

    generate_results(input, expected, solution)
    generate_results(input, actual, exercise)
    report_results(*compare_results(expected, actual))


if __name__ == "__main__":
    main()
