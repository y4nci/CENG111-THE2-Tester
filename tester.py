import random
from tester_evaluator import *
from the2 import *

with open("answers.txt", "r") as file:
    raw_answers = [eval(i[:-1]) for i in file]

with open("cases.txt", "r") as file:
    cases = [eval(i[:-1]) for i in file]

file = open("false_cases.txt", "r+")
file.truncate(0)
file.write("FALSE CASES:\n")


def accuracy(f, index):     # Do not change anything.
    random.seed(111)
    output = get_data()
    right_cases = 0
    index += 1
    answer = raw_answers[10 * index:10 * index + 10]
    for i in range(10):
        output[6] = f(output)
        if output[6] == answer[i]:
            right_cases += 1

    if right_cases == 10:
        result = "TRUE"
        print("CASE {}: {}".format(index, result))
        return 1
    else:
        result = "FALSE"
        print("CASE {}: {}".format(index, result))
        file.read()
        file.writelines(["\n***********\n\nCASE {}: \n".format(index), "  -  " + str(cases[index]), "\nEXPECTED OUTPUTS: \n"] +
                        ["  -  " + str(i) + "\n" for i in answer])
        return 0


right = 0
total = 0
for i in range(25):    # This number can be anything in range (1, 500). It determines the number of sample cases.
    right += accuracy(new_move, i)
    total += 1

print("\n*************", "\n TOTAL: %{} ".format(100 * right / total), "\n*************")

file.close()

with open("DONOTTOUCH.txt", "w") as file:
    file.write("0")
