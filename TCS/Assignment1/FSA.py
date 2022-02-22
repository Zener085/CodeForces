states: list
alpha: list
init: str
fin: list
func: list
check_warning: bool
check_error: bool
File: open()
number_states: dict


def input_states() -> list:
    """read states from the file"""
    with open("fsa.txt", 'r') as file:
        return file.readline().split("[")[1][:-2].split(",")


def input_alpha() -> list:
    """read alphabet from the file"""
    with open("fsa.txt", 'r') as file:
        return file.readlines()[1].split("[")[1][:-2].split(",")


def input_init() -> str:
    """read initial state from the file"""
    with open("fsa.txt", 'r') as file:
        return file.readlines()[2].split("[")[1][:-2]


def input_final() -> list:
    """read final states from the file"""
    with open("fsa.txt", 'r') as file:
        return file.readlines()[3].split("[")[1][:-2].split(",")


def input_function() -> list:
    """read functions from the file"""
    with open("fsa.txt", 'r') as file:
        func_ = file.readlines()[4].split("[")[1][:-2].split(",")

    for i in range(len(func_)):  # split commands in 1 function
        func_[i] = func_[i].split(">")

    return func_


def input_all() -> None:
    """input all states from the terminal"""
    global states, alpha, init, fin, func

    # input finite set of states
    states = input_states()

    # input letters for the alphabet
    alpha = input_alpha()

    # input initial state
    init = input_init()

    # input final state
    fin = input_final()

    # input transition function
    func = input_function()


def check_errors() -> str:
    """Returns error if it exists or return nothing"""
    global states, alpha, init, fin, func, check_error

    for f in func:
        # Error 1
        if f[0] not in states:
            return "Error\nE1: A state '" + f[0] + "' is not in the set of states"
        elif f[2] not in states:
            return "Error\nE1: A state '" + f[2] + "' is not in the set of states"

        # Error 3
        if f[1] not in alpha:
            return "Error\nE3: A transition '" + f[1] + "' is not represented in the alphabet"

    # Error 2
    if 0 in number_states.values():
        return "Error\nE2: Some states are disjoint"

    # Error 4
    if init not in states:
        return "Error\nE4: Initial state is not defined"

    # Error 5
    if not init or len(func) == 0 or len(states) == 0:
        return "Error\nE5: Input file is malformed"

    return ""


def is_complete() -> bool:
    global states, alpha, init, fin, func, number_states
    number_states = {}

    for state in states:
        number_states[state] = 0
        for f in func:
            if f[0] == state:
                number_states[state] += 1

    return True if len(set(number_states.values())) == 1 else False


def check_warnings() -> None:
    global check_warning, File
    # Warning 1
    if "" in fin:
        File.write("Warning:\n")
        File.write("W1: Accepting state is not defined\n")

    # Warning 2
    if check_warning:
        if "" not in fin:
            File.write("Warning:\n")
        File.write("W2: Some states are not reachable from the initial state\n")

    # Warning 3
    if ...:
        if "" not in fin and not check_warning:
            File.write("Warning:\n")
        File.write("W3: FSA is nondeterministic")


if __name__ == "__main__":
    input_all()
    with open("results.txt", 'r') as File:
        if len(check_errors()):
            File.write(check_errors())
        else:
            File.write("FSA is " + "complete" if is_complete() else "incomplete" + "\n")
            File.write(check_warnings())
