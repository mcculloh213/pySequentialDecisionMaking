import copy
import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("Proj04.qIteration", "Q-Iteration", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def q_iteration(det, mdp, error):
    qp = dict([(s, dict([(a, 0) for a in mdp.action(s)])) for s in mdp.states])          # Q' = {S1: {a1: 0, ...} ...}
    q = dict([(s, dict([(a, 0) for a in mdp.action(s)])) for s in mdp.states])           # Q  = {S1: {a1: 0, ...} ...}
    gamma = mdp.gamma                                                                    # Get mdp discount
    log.logger.info("Running Q Iteration")
    i = 1                                                                                # Iterator
    while True:
        log.logger.info("Q Iteration, loop {0}".format(i))
        q = copy.deepcopy(qp)
        delta = 0
        for s in mdp.states:                                                             # s
            log.logger.info("    S={0}".format(s))
            rwd = mdp.rewards.get(s)                                                     # R(s)
            log.logger.info("      Reward={0}".format(rwd))
            qmax = []                                                                    # Q(s',a')
            for a in mdp.action(s):                                                      # a
                log.logger.info("        Action in focus: {0}".format(a))
                trmodel = mdp.transition(s, a)
                summation = 0
                for duple in trmodel:                                                    # s' = d[1], p(s'|s,a) = d[0]
                    log.logger.info("            S'={0}".format(duple[1]))
                    for ap in mdp.action(duple[1]):
                        log.logger.info("            A'={0}".format(ap))
                        qmax.append(q.get(duple[1]).get(ap))
                        log.logger.info("            Q(s',a')={0}".format(q.get(duple[1]).get(ap)))
                    qm = max(qmax)                                                       # max_a' Q(s',a')
                    summation += (duple[0] * qm)                                         # s(P(s'|s,a) * max_a'Q(s',a'))
                qp[s][a] = rwd + (gamma * summation)                                     # Update Q'[s,a]
                delta = max(delta, abs(qp[s][a] - q[s][a]))
                log.logger.info("delta={0}, Q'(s,a) - Q(s,a)={1}".format(delta, abs(qp[s][a] - q[s][a])))
        if delta < error * (1 - gamma) / gamma:                                          # Break condition -------
            log.logger.info("Break condition met at iteration {0}. delta = {1}".format(i, delta))
            break
        i += 1
    return q
