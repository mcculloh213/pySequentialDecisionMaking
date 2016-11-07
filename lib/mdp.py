import lib.logger as lg
import lib.policy

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("Proj04.mdp", "MarkovDecisionProcess",
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class MarkovDecisionProcess:
    """
    Markov Decision Process class.
    """
    def __init__(self, initial, states, transitions, rewards, actions, terminal, gamma):
        """
        Initialize Deterministic Markov Decision Process
        :param initial: Initial state
        :param states: State list
        :type states: list
        :param transitions: Transition model
        :type transitions: dict (JSON)
        :param rewards: Reward model
        :type rewards: dict
        :param actions: Policy
        :param terminal: Terminal states
        :param gamma: Discount
        """
        self.__initial = initial
        self.__current = initial
        self.__actions = actions
        self.__terminal = terminal
        self.__gamma = gamma
        self.__states = states
        self.__rewards = rewards
        self.__transitions = transitions

    @property
    def states(self):
        return self.__states

    @property
    def terminal(self):
        return self.__terminal

    @property
    def rewards(self):
        return self.__rewards

    @property
    def actions(self):
        return self.__actions

    @property
    def gamma(self):
        return self.__gamma

    def __eval(self, state, action):
        """
        Evaluate transition function T: S x A --> P x S
        :param state: Representation of a state in the defined problem. Param:state must be a key in the transitions
                      dict.
        :type state: object
        :param action: Policy. Must be a subkey of a state key in self.__transitions
        :type action: object
        :return: A list of possible transitions
        """
        return self.__transitions.get(state).get(action)

    def transition(self, state, action=None):
        """
        Transition function
        :param state: Representation of a state in the defined problem
        :type state: object
        :param action: Policy.
        :type action: object
        :return: A list of possible transitions for each action
        """
        plan = []
        if action is None:                                                     # Terminal state
            plan.append((0.0, state))                                              # Return cstate
        else:                                                                  # Non-terminal state
            plan.append(self.__eval(state, action))                                # Append (probability, nstate)
            if not isinstance(plan[0], tuple):
                plan = plan[0]
        return plan

    def reward(self, state):
        """
        Reward model for given param:state. Supports empty reward, though it should never be empty.
        :param state: Representation of a state in the defined problem. This is a key in the key-value pair of
                      self.__rewards. Default is None, so always pass a state.
        :type state: object
        :return: The reward of the passed param:state
        """
        return self.__rewards.get(state)

    def action(self, state):
        """
        Return valid actions based on the passed param:state. If the state is terminal, return None.
        :param state: Representation of a state in the defined problem.
        :type state: object
        :return: List of actions that can be taken based on the passed param:state
        """
        act = self.__actions
        if state in self.__terminal:
            act = [None]
        return act
