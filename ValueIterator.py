import sys
import lib.excepterrors as ee
import lib.mdp
import lib.logger as lg
import lib.policy
import lib.preprocess
import lib.readfile
import lib.valueIteration

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("Proj04", "ValueIterator", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    # log.logger.info("State Description file: {0}".format(sys.argv[1]))
    desfile = "./data/place_descriptions.txt"  # sys.argv[1]
    # log.logger.info("Transition file: {0}".format(sys.argv[2]))
    trxfile = "./data/rand_transitions.txt"  # sys.argv[2]
    log.logger.info("Processing state descriptions")
    states, rewards = lib.preprocess.processDescriptions(desfile)
    log.logger.info("Processing transitions")
    det, trx = lib.readfile.readFile(trxfile)
    log.logger.info("Generating actions")
    policy = lib.policy.Policy
    actions = []
    for p in policy:
        actions.append(p.name)
    if det == 1:
        log.logger.info("Transition data is deterministic")
        log.logger.info("Generating transition dictionary, deterministic format")
        transitions = lib.readfile.deterministic_transitions(trx)
        log.logger.info("Creating Deterministic Markov Decision Process model")
        # TODO: Model the terminal states
        mdp = lib.mdp.MarkovDecisionProcess(1, states, transitions, rewards, actions, [1, 3, 9, 10], 0.9)
        utility = lib.valueIteration.value_iteration(True, mdp, 0.001)
        print(utility)
    elif det == 0:
        log.logger.info("Transition data is non-deterministic")
        log.logger.info("Generating transition dictionary, non-deterministic format")
        transitions = lib.readfile.nondeterministic_transitions(trx)
        mdp = lib.mdp.MarkovDecisionProcess(1, states, transitions, rewards, actions, [1, 3, 9, 10], 0.9)
        utility = lib.valueIteration.value_iteration(False, mdp, 0.001)
        print(utility)
    else:
        log.logger.info("Data couldn't be processed. AssertionError has been raised.")
