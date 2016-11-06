# Programming Assignment 04 -- Sequential Decision Making
## About
CSE 3521 Introduction to Artificial Intelligence Programming Assignment 04 : Sequential Decision Making
This lab demonstrates Sequential Decision Making by implementing Value Iteration and Q-Iteration algorithms.
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