import copy
import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("Proj04.valueIteration", "value-Iteration", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def value_iteration(det, mdp, error):
    """
    Value Iteration algorithm using Bellman's equation.
    :param det: Boolean value -- true if data is deterministic, false otherwise
    :type det: bool
    :param mdp: Markov Decision Process class
    :type mdp: lib.mdp.MarkovDecisionProcess
    :param error: Percent error tolerance
    :type error: float
    :return:
    """
    utilp = dict([(s, 0) for s in mdp.states])                                                # U' = {S1: 0, ..., Sn: 0}
    util = dict([(s, 0) for s in mdp.states])                                                 # U  = {S1: 0, ..., Sn: 0}
    gamma = mdp.gamma                                                                         # Get MDP discount
    log.logger.info("Running value iteration")
    i = 1                                                                                     # Increment
    policy = {}
    while True:                                                                               # Loop ------------------
        log.logger.info("Value Iteration, loop {0}".format(i))
        util = copy.deepcopy(utilp)                                                           # U = U'
        delta = 0                                                                             # Set initial delta
        for s in mdp.states:                                                                  # Bellman Equation
            rwd = mdp.rewards.get(s)                                                          # Reward of current state
            bellmansum = []                                                                   # Summation P(s'|s,a)U(s')
            actions = mdp.action(s)                                                           # Valid actions
            for a in actions:
                trmodel = mdp.transition(s, a)                                                # Transition model
                summation = 0                                                                 # summation (P1U1 + ...)
                for duple in trmodel:
                    bellmansum.append((duple[0] * util[duple[1]]))
            index = bellmansum.index(max(bellmansum))                                         # Get index of max util
            if not det:                                                                       # Normalize index
                if index in range(0, 3):                                                      # i in 0,1,2
                    index = 0
                elif index in range(3, 6):                                                    # i in 3,4,5
                    index = 1
                else:                                                                         # i in 6,7,8
                    index = 2
            policy[s] = actions[index]                                                        # Update policy
            utilp[s] = rwd + (gamma * max(bellmansum))                                        # Update U'
            log.logger.info("State {0}: Utility = {1} Policy = {2}".format(s, utilp[s], policy[s]))
            delta = max(delta, abs(utilp[s] - util[s]))                                       # Recalculate delta
            log.logger.info("delta = {0}".format(delta))
        if delta < error * (1 - gamma) / gamma:                                               # Break condition -------
            log.logger.info("Break condition met at iteration {0}. delta = {1}".format(i, delta))
            break
        i += 1                                                                                # Increment
    return util, policy
