import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("Proj04.valueIteration", "value-Iteration", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def value_iteration(det, mdp, error):
    utilp = dict([(s, 0) for s in mdp.states])                                                # U' = {S1: 0, ..., Sn: 0}
    util = dict([(s, 0) for s in mdp.states])                                                 # U  = {S1: 0, ..., Sn: 0}
    gamma = mdp.gamma                                                                         # Get MDP discount
    log.logger.info("Running value iteration")
    i = 1                                                                                     # Increment
    while True:                                                                               # Loop ------------------
        log.logger.info("Value Iteration, loop {0}".format(i))
        util = utilp.copy()                                                                   # U = U'
        delta = 0                                                                             # Set initial delta
        for s in mdp.states:                                                                  # Bellman Equation
            rwd = mdp.rewards.get(s)                                                          # Reward of current state
            bellmansum = []                                                                   # Summation P(s'|s,a)U(s')
            actions = mdp.action(s)                                                           # Valid actions
            for a in actions:
                trmodel = mdp.transition(s, a)                                                # Transition model
                summation = 0                                                                 # summation (P1U1 + ...)
                if det:                                                                       # Deterministic model
                    for duple in trmodel:
                        bellmansum.append((duple[0] * util[duple[1]]))
                else:                                                                         # Non-Deterministic model
                    if len(trmodel) > 1:                                                          # Non-terminal state
                        for act in trmodel:
                            for duple in act:
                                bellmansum.append((duple[0] * util[duple[1]]))
                    else:                                                                         # Terminal state
                        for duple in trmodel:
                            bellmansum.append((duple[0] * util[duple[1]]))
            utilp[s] = rwd + (gamma * max(bellmansum))
            log.logger.info("State {0}: Utility = {1}".format(s, utilp[s]))
            delta = max(delta, abs(utilp[s] - util[s]))                                       # Recalculate delta
            log.logger.info("delta = {0}".format(delta))
        i += 1                                                                                # Increment
        if delta < error * (1 - gamma) / gamma:                                               # Break condition -------
            log.logger.info("Break condition met at iteration {0}. delta = {1}".format(i, delta))
            break
    return util
