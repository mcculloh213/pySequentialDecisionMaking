import csv
import lib.excepterrors as ee
import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("Proj04.preprocess", "processDescription", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def processDescriptions(fpath):
    """
    Given the context of the problem, I'm making the assumption that all state descriptions will be in the same format
    as ./data/place_descriptions.txt, which are as follows:

                                    {state number, state name, imgfile, reward, msg}

    The state name, imgfile, and message may be safely discarded -- the goal is to get the state number to enumerate the
    states, and get the reward for usage in value/Q iteration.
    In the same vein of thought, the length of each line of variables will either be 4 or 5. For this function, the
    the length doesn't play much importance, because the missing variable is <msg>. The important data will be in
    locations 0 and 3.
    State number acts as a foreign key between the description and transition files.
    :param fpath: file path to state description file as defined above.
    :return: [[states]^T, [rewards]^T] s.t. states[0] => rewards[0] , ..., states[n] => rewards[n]
    """
    try:
        f = open(fpath, 'r')                                                   # Open param:filepath
        data = csv.reader(f)                                                   # Read f as a CSV file
        dataset = list(data)                                                   # Coherse the CSV data into a list

    except FileNotFoundError as e:
        ee.excepterrors(e, "msg")
