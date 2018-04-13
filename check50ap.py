import click
import os
import subprocess
import sys
import tempfile

from clint.textui import colored, puts
from os import listdir
from os.path import isfile, join


def generate_results(py_file, input=None):
    if input is None:
        proc = subprocess.Popen(['python', py_file],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    else:
        with open(input) as infile:
            proc = subprocess.Popen(['python', py_file],
                                    stdin=infile,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
    out, err = proc.communicate()

    return out.decode(), err.decode()


def report_results(expected_str, actual_str):
    if expected_str == actual_str:
        puts(colored.green('Solution is correct!'))
    else:
        puts(colored.red('Incorrect!'))
        print(f'Expected output:\n{expected_str}\n'\
              f'Actual output:\n{actual_str}')


def get_files_from_path(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    files.sort()
    return files


def print_header_report(case, input=None):
    print('=====================')
    print(f'Running case {case}:')
    if input is not None:
        with open(input) as input:
            for line in input.read().splitlines():
                print(line, end='\t')
            print()


def print_footer():
    print('=====================')
    print()


def remove_silently(filename):
    try:
        os.remove(filename)
    except OSError:
        pass


def report_case(case, assignment, exercise, input):
    solution = join('solutions', assignment, exercise)
    input = join('inputs', assignment, exercise[:-3], input)

    print_header_report(case, input)
    expected_out, _ = generate_results(solution, input)
    actual_out, _ = generate_results(exercise, input)
    report_results(expected_out, actual_out)
    print_footer()


def get_seed(seed_file):
    with open(join('inputs', 'random', seed_file)) as seed_file:
        seed = eval(seed_file.read())

    return seed


def write_file_with_fixed_seed(filename, tpm_filename, seed):
    random_header = f'import random\nrandom.seed({seed})\n'

    with open(filename) as f:
        f_str = f.read()
        with open(tpm_filename, 'w') as tmp:
            tmp.write(random_header + f_str)


def report_random_case(seed, case, assignment, exercise, input=None):
    solution = join('solutions', assignment, exercise)
    if input:
        input = join('inputs', assignment, exercise[:-3], input)

    tmp_solution = f'sol_{seed[:-4]}_{exercise}'
    tmp_exercise = f'exe_{seed[:-4]}_{exercise}'
    seed = get_seed(seed)

    write_file_with_fixed_seed(solution, tmp_solution, seed)
    write_file_with_fixed_seed(exercise, tmp_exercise, seed)

    print_header_report(case, input)
    expected_out, _ = generate_results(tmp_solution, input)
    actual_out, _ = generate_results(tmp_exercise, input)
    report_results(expected_out, actual_out)
    print_footer()

    remove_silently(tmp_solution)
    remove_silently(tmp_exercise)


@click.command()
@click.option('--random', is_flag=True)
@click.argument('assignment')
@click.argument('exercise')
def main(random, assignment, exercise):
    path = join('inputs', assignment, exercise[:-3])
    random_path = join('inputs', 'random')
    inputs = get_files_from_path(path)

    if random:
        seeds = get_files_from_path(random_path)
        if len(inputs) in (0, 1):
            for case, seed in enumerate(seeds, 1):
                if inputs:
                    report_random_case(seed, case, assignment, exercise, inputs[0])
                else:
                    report_random_case(seed, case, assignment, exercise)
    else:
        for case, input in enumerate(inputs, 1):
            report_case(case, assignment, exercise, input)


if __name__ == "__main__":
    main()
