class State:
    def __init__(self, name, accept):
        self.name = name
        self.transitions = {}
        self.accept = accept
    
    def add_transition(self, symbol, transition_state):
        self.transitions[symbol].append(transition_state)

class NFA:
    def __init__(self, start, accepts, transitions):
        self.start = State(start)
        self.states = {}