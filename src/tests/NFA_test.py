from NFA import *

import pytest

def test_State():
    state_one = State(name = 'q', accept = True)
    state_two = State(name = 'z', accept = False)
    state_one.add_transition(symbol = '0', transition_state = state_two)

    assert state_one.get_transitions('0') == [state_two]

def test_NFA_solver():
    is_even = NFA(start = 'q0', accepts = ['q0'], transitions = ['q0:0->q0', 'q0:1->q1', 'q1:1->q1', 'q1:0->q0'])

    assert is_even.validate_string('10')
    assert is_even.validate_string('0')
    assert is_even.validate_string('1010111001100')
    assert not is_even.validate_string('01')

    ends_with_00_or_11 = NFA(start = 'q0', accepts = ['q3'], \
        transitions = ['q0:0->q0','q0:1->q0','q0:0->q1','q0:1->q2','q1:0->q3','q2:1->q3'])
    assert ends_with_00_or_11.validate_string('0100111100')
    assert ends_with_00_or_11.validate_string('10011101011')
    assert not ends_with_00_or_11.validate_string('11001010101')

def test_get_negation():
    is_even = NFA(start = 'q0', accepts = ['q0'], transitions = ['q0:0->q0', 'q0:1->q1', 'q1:1->q1', 'q1:0->q0'])
    is_odd = is_even.get_negation()

    assert not is_odd.validate_string('10')
    assert not is_odd.validate_string('0') 
    assert not is_odd.validate_string('1010111001100')
    assert is_odd.validate_string('01')
