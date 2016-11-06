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
        log.logger.info("Opening file {0}".format(fpath))
        f = open(fpath, 'r')                                                   # Open param:filepath
        log.logger.info("Reading data using CSV module")
        data = csv.reader(f)                                                   # Read f as a CSV file
        log.logger.info("Cohersing data into a usable format")
        dataset = list(data)                                                   # Coherse the CSV data into a list
        log.logger.info("Closing file {0}".format(fpath))
        f.close()                                                              # Close f, dataset obtained
        states = []
        rewards = []
        terminals = []
        log.logger.info("Cleaning data")
        for i in range(0, len(dataset)):
            try:
                states.append(int(dataset[i][0]))                              # Coherse state number to an integer
            except ValueError as e:
                ee.excepterrors(e, "Could not coherse state enumeration {0} to an integer".format(dataset[i][0]))
            try:
                rewards.append(float(dataset[i][3]))                           # Coherse state reward to a float
            except ValueError as e:
                ee.excepterrors(e, "Could not coherse state rewards {0} to a float".format(dataset[i][3]))
        log.logger.info("Generating reward dictionary and terminal states")
        rwd = {}                                                               # Initialize reward dictionary
        for i in range(0, len(states)):
            rwd[states[i]] = rewards[i]
            if (rewards[i] == 1) or (rewards[i] == -1):                        # If reward is a terminal state reward
                terminals.append(states[i])                                        # Append the state to terminal list
        log.logger.info("Done -- Returning state/reward duple")
        return states, rwd, terminals                                          # Return state description/rewards

    except FileNotFoundError as e:
        ee.excepterrors(e, "msg")
