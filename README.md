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

Copy the exercises provided by the students in the root directory of the project, and depending on the _assignment_ and _exercise_ you want to check,
you can run the following command:
```
$ python check50ap.py assignment exercise_XX.py
```

Where `assignment` is the name of the assignment and `exercise_XX.py` is the `XX` exercise of the assignment.
For example, if you want to check `exercise_03.py` from `selections` assignment, you have to run:
```
$ python check50ap.py selections exercise_03.py
```
