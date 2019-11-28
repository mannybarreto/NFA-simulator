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
        self.states[start] = self.start[start]

if __name__ == "__main__":
    start_and_accept = input('Enter start and accept states in following format: START=q0;ACCEPT=q2,q1').split(';')
    entered_transitions = []

    if len(start_and_accept) != 2:
        raise ValueError('Input was invalid')

    try:
        start_state = start_and_accept[0].replace('START=', '')
        accept_states = start_and_accept[1].replace('ACCEPT=', '').split(',')
    except:
        raise ValueError('Improperly formatted input')

    print('Input transition states in the following format or type DONE when complete: q0:a->q1 or q0->q2')
    while True:
        transition = input('Transition: ')

        if transition is 'DONE':
            break

        entered_transitions.append(transitions)

    automata = NFA(start=start_state, accepts=accept_states, transitions=entered_transitions)
