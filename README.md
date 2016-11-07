# Programming Assignment 04 -- Sequential Decision Making
## About
CSE 3521 Introduction to Artificial Intelligence Programming Assignment 04 : Sequential Decision Making
This lab demonstrates Sequential Decision Making by implementing Value Iteration and Q-Iteration algorithms.
To run the Value Iteration algorithm, enter:
```shell
$ python ValueIterator.py "path/to/state/description.txt" "path/to/transition/file.txt"
```
To run the Q-Iteration algorithm, enter
```shell
$ python QIterator.py "path/to/state/description.txt" "path/to/transition/file.txt"
```
Finally, this lab only works on Python 3.x, because `policy.py` uses the `enum` class, which was introduced in Python 3.x.
### Library -- `./lib`
* excepterrors
    Handle and log errors and exceptions to `./logs/ERRORS.log`
* logger
    Python logger class
* mdp
    Markov Decision Process class used in Value/Q Iteration
* policy
    Pseudo-enumeration of problem policies
* preprocess
    Function to process state descriptions, returning state enumerations and state rewards
* qIteration
    Q Iteration algorithm
* readfile
    Read transition file, return classification as deterministic or non-deterministic, and transition data
* valueIteration
    Value Iteration algorithm