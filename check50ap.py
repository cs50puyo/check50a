import click
import os
import subprocess

@click.command()
@click.argument('assignment')
@click.argument('exercise')
def main(assignment, exercise):
    path = os.path.join('solutions', assignment, exercise)
    subprocess.call(['python', path])

if __name__ == "__main__":
    main()
