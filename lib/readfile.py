import csv
import lib.excepterrors as ee
import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("Proj04.readFile", "readFile", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def readFile(fpath):
    """
    Open, read, classify, and return transition data.
    :param fpath: path to file
    :return: det, transitions
    """
    try:
        det = -1                                                                    # Deterministic bit
        log.logger.info("Opening file {0}".format(fpath))
        f = open(fpath, 'r')                                                        # Open file
        log.logger.info("Reading data using CSV module")
        data = csv.reader(f)                                                        # Read as a CSV
        log.logger.info("Cohersing data into a usable format")
        dataset = list(data)                                                        # Coherse data into a list of arrays
        if len(dataset[0]) == 4:                                                    # Classify data as deterministic
            det = 1                                                                 # det = 1 -> data is deterministic
            log.logger.info("Passed data is deterministic")
            log.logger.info("Cleaning data.")
            for i in range(0, len(dataset)):                                        # Clean data
                for j in [0, 2]:
                    dataset[i][j] = int(dataset[i][j])                              # State numbers: String -> Integer
                dataset[i][3] = float(dataset[i][3])                                # Probability: String -> Float
        elif len(dataset[0]) == 8:                                                  # Classify data as non-deterministic
            det = 0                                                                 # det = 0 -> data is ndeterministic
            log.logger.info("Passed data is non-deterministic")
            log.logger.info("Cleaning data")
            for i in range(0, len(dataset)):                                        # Clean data
                for j in [0, 2, 4, 6]:
                    dataset[i][j] = int(dataset[i][j])                              # State numbers: String -> Integer
                for j in [3, 5, 7]:
                    dataset[i][j] = float(dataset[i][j])                            # Probability: String -> Float
        else:                                                                       # det = -1 -> data is unclassifiable
            log.logger.info("Passed data cannot be classified")
            raise AssertionError                                                    # Raise error
        log.logger.info("DONE -- Returning dataset")
        return det, dataset                                                         # Return dataset
    except FileNotFoundError as e:                         # EXCEPTION:
        ee.excepterrors(e, "No such file: {0}".format(fpath))                       # param:fpath does not exist
    except ValueError as e:                                # EXCEPTION:
        ee.excepterrors(e, "Could not coherse data correctly")                      # Could not correctly coherse data
    except AssertionError as e:                            # EXCEPTION:
        ee.excepterrors(e, "Improper data {0} passed.".format(fpath))               # param:fpath cannot be used


def deterministic_transitions(dataset):
    nonterminals = []                                                               # Instantiate non-terminal nodes
    for i in range(0, len(dataset)):                                                # Gather non-terminal nodes
        if dataset[i][0] not in nonterminals:
            nonterminals.append(dataset[i][0])
    trx = {}
    for i in nonterminals:
        action = {}
        for j in range(0, len(dataset)):
            if dataset[j][0] == i:
                action[dataset[j][1]] = (dataset[j][3], dataset[j][2])
        trx[i] = action
    return trx


def nondeterministic_transitions(dataset):
    nonterminals = []
    for i in range(0, len(dataset)):
        if dataset[i][0] not in nonterminals:
            nonterminals.append(dataset[i][0])
    trx = {}
    for i in nonterminals:
        action = {}
        for j in range(0, len(dataset)):
            if dataset[j][0] == i:
                action[dataset[j][1]] = [(dataset[j][3], dataset[j][2]),
                                         (dataset[j][5], dataset[j][4]),
                                         (dataset[j][7], dataset[j][6])]
        trx[i] = action
    return trx
