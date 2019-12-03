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
            
            if split_transition[0] not in self.states.keys():
                self.states[split_transition[0]] = State(name = split_transition[0], accept = split_transition[0] in accepts)

            if split_transition[2] not in self.states.keys():
                self.states[split_transition[2]] = State(name = split_transition[2], accept = split_transition[2] in accepts)

            self.states[split_transition[0]].add_transition(split_transition[1], self.states[split_transition[2]])

        for state in self.states:
            print(self.states[state])