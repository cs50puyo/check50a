import click
import os
import subprocess
import sys


def generate_results(input, output, py_file):
    with open(input) as infile:
        with open(output, 'w') as outfile:
            subprocess.call(['python', py_file],
                            stdin=infile,
                            stdout=outfile)


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

    with open(expected) as expected, open(actual) as actual:
        expected_str = ''
        actual_str = ''
        for e, a in zip(expected.read(), actual.read()):
            expected_str += e
            actual_str += a
            if e != a:
                print('Incorrect!')
                print('Expected output:')
                print(expected_str)
                print()
                print('Actual output:')
                print(actual_str)
                sys.exit(1)

    print('Solution is correct!')


if __name__ == "__main__":
    main()
