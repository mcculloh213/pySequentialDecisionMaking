import lib.logger as lg
import lib.policy

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("Proj04.mdp", "MarkovDecisionProcess",
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class MarkovDecisionProcess:
    """
    Markov Decision Process pseudo-abstract class.
    """
    def __init__(self, initial, actions, terminal, gamma):
        self.__initial = initial
        self.__current = initial
        self.__actions = actions
        self.__terminal = terminal
        self.__states = list()
        self.__rewards = {}
        self.__gamma = gamma

    @property
    def current(self):
        return self.__current

    @property
    def gamma(self):
        return self.__gamma

    @property
    def states(self):
        return self.__states

    @property
    def rewards(self):
        return self.__rewards

    @property
    def reward(self, state=None):
        """
        Reward model for given param:state. Supports empty reward, though it should never be empty.
        :param state: Representation of a state in the defined problem. This is a key in the key-value pair of
                      self.__rewards. Default is None, so always pass a state.
        :return: The reward of the passed param:state
        """
        return self.__rewards.get(state)

    @property
    def transition(self, state, action=None):
        """
        Transition model for param:given state and param:action. This needs to be overridden by a functional MDP.
        :param state:
        :param action:
        :return:
        """
        raise NotImplementedError

    @property
    def action(self, state):
        """
        Return valid actions based on the passed param:state. If the state is terminal, return None.
        :param state: Representation of a state in the defined problem.
        :return: List of actions that can be taken based on the passed param:state
        """
        return self.__actions if (state in self.__terminal) else None


class DeterministicMDP(MarkovDecisionProcess):
    """
    Deterministic Markov Decision Process class.
    """
    def __init__(self, initial, states, actions, terminal, gamma):
        MarkovDecisionProcess.__init__(self, initial, actions, terminal, gamma)
        pass

    def __eval(self, state, action):
        index = self.__states.index(state)


    @property
    def transition(self, state, action=None):
        plan = []
        if action is None:                                                     # Terminal state
            plan.append((0.0, state))                                              # Return cstate
        else:                                                                  # Non-terminal state
            pass
        return plan


class NonDeterministicMDP(MarkovDecisionProcess):
    """
    Non-Deterministic Markov Decision Class
    """
