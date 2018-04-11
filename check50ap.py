import click
import os

@click.command()
@click.argument('assignment')
@click.argument('exercise')
def main(assignment, exercise):
    path = os.path.join('assignments', assignment, exercise)
    print(path)

if __name__ == "__main__":
    main()
