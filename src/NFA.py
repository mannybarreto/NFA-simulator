import re

class State:
    def __init__(self, name, accept):
        self.name = name
        self.transitions = {}
        self.accept = accept
    
    def add_transition(self, symbol, transition_state):
        self.transitions[symbol].append(transition_state)

class NFA:
    def __init__(self, start, accepts, transitions):
        self.start = State(name = start, accept = start in accepts)
        self.states = {}
        self.states[start] = self.start
        for transition in transitions:
            if ':' in transition:
                split_transition = tuple(re.split(':|->', transition))
            else:
                split_transition = re.split('->', transition)
                split_transition = (split_transition[0], None, split_transition[1])
            states[split_transition[0]].add_transition(split_transition[1], split_transition[2])