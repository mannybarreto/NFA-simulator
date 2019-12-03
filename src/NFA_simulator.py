from NFA import *

if __name__ == "__main__":
    entered_transitions = []

    while True:
        print('Enter start and accept states in following format: START=q0;ACCEPT=q2,q1')
        start_and_accept = input('Start & Accept States: ').split(';')

        if len(start_and_accept) != 2:
            print('Improperly formatted input')
        else:
            try:
                start_state = start_and_accept[0].replace('START=', '')
                accept_states = start_and_accept[1].replace('ACCEPT=', '').split(',')
            except:
                print('Improperly formatted input')
            finally:
                break

    print('Input transition states in the following format or type DONE when complete: q0:a->q1 or q0->q2')
    while True:
        transition = input('Transition: ')

        if transition == 'DONE':
            break

        # TODO(mannybarreto): check if transition is properly formatted

        entered_transitions.append(transition)

    automata = NFA(start=start_state, accepts=accept_states, transitions=entered_transitions)