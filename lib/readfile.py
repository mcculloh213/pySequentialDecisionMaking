import csv
import lib.excepterrors as ee
import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("Proj04.readFile", "readFile", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def readFile(fpath):
    try:
        log.logger.log("Opening file {0}".format(fpath))
        f = open(fpath, "r")                                                        # Open file
        log.logger.log("Reading data using CSV module")
        data = csv.reader(f)                                                        # Read as a CSV
        log.logger.log("Cohersing data into a usable format")
        dataset = list(data)                                                        # Coherse data into a list of arrays
        log.logger.log("DONE -- Returning dataset")
        return dataset                                                              # Return dataset
    except FileNotFoundError as e:                         # EXCEPTION:
        ee.excepterrors(e, "No such file: {0}".format(fpath))                       # param:fpath does not exist
