import click
import os
import subprocess


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

    generate_results(input, 'expected.txt', solution)
    generate_results(input, 'actual.txt', exercise)


if __name__ == "__main__":
    main()
