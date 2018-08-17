## an assortment of code relating to "code challenges"
def num_teachers(**kwargs):
    counter = 0
    for key, value in kwargs.items():
        counter += 1
        print(key, value)
    return counter


print(num_teachers(**{"dslkf": "efsdf", "dskfs": "dkljhf"}))
#####################
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(
            name_1="Alex",
            name_2="Gray",
            name_3="Harper",
            name_4="Phoenix",
            name_5="Remy",
            name_6="Val"
        )


########################
def multiply(*args):
    total = 1
    for num in args:
        total *= num
    
    return total

print(multiply(2,2,2,2))
##########################
def combo(*args):
    print(args)
    x_list = args[0]
    y_list = args[1]
    output = []
    for i, v in enumerate(x_list):
        output.append((v, y_list[i]))
    return output

tuple_list1 = "cba"
list2 = "abc"
print(combo(tuple_list1, list2))

###################################

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(topic):
    output = []
    for course in COURSES:
        if topic & COURSES[course]:
            output.append(course)
    return output


print(covers({"conditions", "input"}))

def covers_all(set_list):
    output = []
    for course in COURSES:
        if set_list & COURSES[course] == set_list:
            output.append(course)
    return output

print(covers_all({"conditions", "input"}))