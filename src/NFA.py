import re

class State:
    def __init__(self, name, accept):
        self.name = name
        self.transitions = {}
        self.accept = accept
    
    def add_transition(self, symbol, transition_state):
        if symbol not in self.transitions.keys():
            self.transitions[symbol] = []
        self.transitions[symbol].append(transition_state)
    
    def __str__(self):
        return f'State: {self.name}; Accept?: {self.accept}; Transitions: {self.transitions}'

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
            
            initial_state, symbol, transition_state = split_transition

            if initial_state not in self.states.keys():
                self.states[initial_state] = State(name = initial_state, accept = initial_state in accepts)

            if transition_state not in self.states.keys():
                self.states[transition_state] = State(name = transition_state, accept = transition_state in accepts)

            self.states[initial_state].add_transition(symbol, self.states[transition_state])