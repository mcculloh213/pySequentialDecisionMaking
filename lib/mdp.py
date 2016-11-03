import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("Proj04.mdp", "MarkovDecisionProcess",
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class MarkovDecisionProcess:
    def __init__(self, initial, actions, terminal, gamma, states=set(), rewards={}):
        self.__initial = initial
        self.__actions = actions
        self.__terminal = terminal
        self.__states = states
        self.__rewards = rewards
        self.__gamma = gamma

    def reward(self, state=None):
        """
        Reward model for given param:state. Supports empty reward, though it should never be empty.
        :param state: Representation of a state in the defined problem. This is a key in the key-value pair of
                      self.__rewards. Default is None, so always pass a state.
        :return: The reward of the passed param:state
        """
        return self.__rewards.get(state)

    def transition(self, state, action=None):
        """
        Transition model for param:given state and param:action
        :param state:
        :param action:
        :return:
        """
