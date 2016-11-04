import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("Proj04.valueIteration", "value-Iteration", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def value_iteration(mdp, error):
    utilp = dict([(s, 0) for s in mdp.states])                                                # U' = {S1: 0, ..., Sn: 0}
    util = dict([(s,0) for s in mdp.states])                                                  # U  = {S1: 0, ..., Sn: 0}
    rwd = mdp.rewards                                                                         # Get MDP state Rewards
    trx = mdp.transitions                                                                     # Get MDP Transition model
    gamma = mdp.gamma                                                                         # Get MDP discount
    log.logger.info("Running value iteration")
    i = 1                                                                                     # Increment
    while True:                                                                               # Loop ------------------
        log.logger.info("Value Iteration, loop {0}".format(i))
        util = utilp.copy()                                                                   # U = U'
        delta = 0                                                                             # Set initial delta
        for s in mdp.states:
            utilp[s] = rwd(s) + gamma * max([sum([p * util[s1] for (p, s1) in trx(s, a)])     # Bellman Equation
                                        for a in mdp.actions(s)])
            log.logger("State {0}: Utility = {1}".format(s, utilp[s]))
            delta = max(delta, abs(utilp[s] - util[s]))                                       # Recalculate delta
            log.logger.info("delta = {0}".format(delta))
        i += 1                                                                                # Increment
        if delta < error * (1 - gamma) / gamma:                                               # Break condition -------
            log.logger.info("Break condition met at iteration {0}. delta = {1}".format(i, delta))
            break
    return util
