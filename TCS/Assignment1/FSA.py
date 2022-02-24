import copy
from typing import Union

states = []  # list of states
alpha = []  # alphabet
init = ""  # initial state
fin = []  # list of final states
func = []  # list of transitions
warning = True  # using for writing more than 1 warning


def check_error5(number_of_string: int = 5) -> Union[None, list]:
    """Check if there is E5 in input file
    :param number_of_string number of string it needs to read from the input file"""
    if number_of_string < 5:  # check normal conditions
        with open("fsa.txt", 'r') as file:
            try:  # trying to read the current line
                if number_of_string == 1:
                    alphabet = file.readlines()[number_of_string].split("[")
                    if alphabet[0][-1] != '=':
                        with open("result.txt", 'w') as e:
                            e.write("Error:\nE5: Input file is malformed")
                            exit()
                    return alphabet[1][:-2].split(",")

                if number_of_string == 4:
                    return file.readlines()[number_of_string].split("[")[1][:-1].split(",")

                return file.readlines()[number_of_string].split("[")[1][:-2].split(",")

            except IndexError:
                with open("result.txt", 'w') as e:
                    e.write("Error:\nE5: Input file is malformed")
                    exit()
    else:
        with open("fsa.txt", 'r') as file:
            try:  # try to read more strings than they should be
                file.readlines()[number_of_string].split("[")[1][:(-2)].split(",")
                with open("result.txt", 'w') as e:
                    e.write("Error:\nE5: Input file is malformed")
                    exit()
            except IndexError:
                return


def input_states() -> list:
    """read states from the file"""
    return check_error5(0)


def input_alpha() -> list:
    """read alphabet from the file"""
    return check_error5(1)


def input_init() -> str:
    """read initial state from the file"""
    return check_error5(2)[0]


def input_final() -> list:
    """read final states from the file"""
    return check_error5(3)


def input_function() -> list:
    """read functions from the file"""
    func_ = check_error5(4)

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

    # check if we have more strings than we need
    check_error5()


def error1() -> Union[bool, str]:
    """Check if there is error 1"""
    global init, states, func

    if init not in states:
        return init

    for f in func:
        if f[0] not in states:
            return f[0]
        elif f[2] not in states:
            return f[2]

    return False


def error2() -> bool:
    """Check if there is error 2"""
    global states, func
    copy_states = copy.deepcopy(states)

    for f in func:
        if f[0] != f[2] and f[2] in copy_states:
            copy_states.remove(f[2])

    return True if len(copy_states) else False


def error3() -> Union[bool, str]:
    """Check if there is error 3"""
    global func, alpha

    for f in func:
        if f[1] not in alpha:
            return f[1]

    return False


def error4() -> bool:
    """Check if there is error 4"""
    global init

    return True if init == "" else False


def check_errors() -> str:
    """Returns error if it exists or return nothing"""
    global states, alpha, init, fin, func

    # Error 4
    if error4():
        return "Error:\nE4: Initial state is not defined"

    # Error 1
    if error1():
        return "Error:\nE1: A state '" + error1() + "' is not in the set of states"

    # Error 3
    if error3():
        return "Error:\nE3: A transition '" + error3() + "' is not represented in the alphabet"

    # Error 2
    if error2():
        return "Error:\nE2: Some states are disjoint"

    return ""


def is_complete() -> bool:
    global alpha, func

    number_states = {}

    for f in func:
        if f[0] in number_states:
            number_states[f[0]] += 1
            continue
        number_states[f[0]] = 1

    number_states = set(number_states.values())
    if len(number_states) == 1 and list(number_states)[0] == len(alpha):
        return True

    return False


def warning1() -> bool:
    """check if there is the first warning"""
    global fin

    return True if "" in fin and len(fin) == 1 else False


def warning2() -> bool:
    """check if there is the second warning"""
    global states, func

    for f in func:
        if f[0] not in states or f[2] not in states:
            return True

    return False


def warning3() -> bool:
    """check if there is the third warning"""
    global func
    part_states = []

    for f in func:
        if (f[0], f[1]) in part_states:
            return True
        part_states.append((f[0], f[1]))

    return False


def check_warnings() -> None:
    """check all warnings and print them if they exist"""
    global warning

    # Warning 1
    if warning1():
        warning = False
        File.write("Warning:\n")
        File.write("W1: Accepting state is not defined\n")

    # Warning 2
    if warning2():
        if warning:
            File.write("Warning:\n")
        warning = False
        File.write("W2: Some states are not reachable from the initial state\n")

    # Warning 3
    if warning3():
        if warning:
            File.write("Warning:\n")
        warning = False
        File.write("W3: FSA is nondeterministic")


if __name__ == "__main__":
    input_all()
    with open("result.txt", 'w') as File:
        if len(check_errors()):
            File.write(check_errors())
        else:
            File.write("FSA is " + ("complete" if is_complete() else "incomplete") + "\n")
            check_warnings()
