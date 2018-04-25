# check50ap
This is a tool used to facilitate reviewing the assignments sent in
the programming course CS50 AP Puyo.

## Installation
You can follow the next steps in order to install this cli:

1. Clone the repository
```
$ git clone https://github.com/cs50puyo/check50ap.git
```
2. Create a virtual environment insider the project directory:
```
$ cd check50ap
$ python3 -m venv .venv
```

3. Activate the virtual environment:
```
$ source .venv/bin/activate
```

4. Install `pip-tools` to manage dependencies:
```
$ pip install pip-tools
```

5. Install dependencies using `pip-sync`:
```
$ pip-sync
```

## Usage
Before using the cli, make sure your virtual environment is
activated. If not, run the following command:
```
$ source .venv/bin/activate
```

Copy the exercises provided by the students in the root directory of the project.

### Exercises that don't use the random module
#### Exercises that require input from user
When the exercise requires input from the user, depending on the
_assignment_ and _exercise_ you want to check, you can run the
following command:
```
$ python check50ap.py assignment exercise_XX.py
```

Where `assignment` is the name of the assignment and `exercise_XX.py` is the `XX` exercise of the assignment.
For example, if you want to check `exercise_03.py` from `selections` assignment, you have to run:
```
$ python check50ap.py selections exercise_03.py
```

#### Exercises that don't require input from user
When the exercise does not require input from the user, depending on the
_assignment_ and _exercise_ you want to check, use the optional argument
`--no-input` as follows:
```
$ python check50ap.py --no-input assignment exercise_XX.py
```
Where `assignment` is the name of the assignment and `exercise_XX.py` is the `XX` exercise of the assignment.
For example, if you want to check `exercise_01.py` from `print-statement` assignment, you have to run:
```
$ python check50ap.py --no-input print-statement exercise_01.py
```

### Exercises that use the random module
#### Exercises that require input from user
When the exercise requires the use of the built-in module `random`, and it requires
input from user, use the optional argument `--random` as follows:
```
$ python check50ap.py --random assignment exercise_XX.py
```

For example, if you want to check `exercise_11.py` from `loops` assignment, you have to run:
```
$ python check50ap.py --random loops exercise_11.py
```
#### Exercises that don't require input from user
When the exercise requires the use of the built-in module `random`, and it does not require
input from user, use the optional arguments `--random` and `--no-input` as follows:
```
$ python check50ap.py --random --no-input assignment exercise_XX.py
```

For example, if you want to check `exercise_06.py` from `selections` assignment, you have to run:
```
$ python check50ap.py --random --no-input selections exercise_06.py
```
