from NFA import *

def test_State:
    state_one = State(name = 'q', accept = True)
    state_two = State(name = 'z', accept = False)
    state_one.add_transition(symbol = '0', transition_state = state_two)

    assert state_one.get_transitions('0') == [state_two]
