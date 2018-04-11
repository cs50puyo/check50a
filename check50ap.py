import click
import os
import subprocess

@click.command()
@click.argument('assignment')
@click.argument('exercise')
def main(assignment, exercise):
    path = os.path.join('solutions', assignment, exercise)
    input = os.path.join('inputs', assignment, exercise[:-2] + 'txt')
    with open('expected.txt', 'w') as outfile:
        with open(input) as infile:
            subprocess.call(['python', path],
                            stdin=infile,
                            stdout=outfile)

if __name__ == "__main__":
    main()
