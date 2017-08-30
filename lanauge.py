class Functions(object):
    def __init__(self):
        self.start_of_first = lines.index("void first() {")
        self.end_of_first = find_next_closing_bracket(self.start_of_first)
        self.first_function = lines[self.start_of_first + 1: self.end_of_first]

    def first(self):
        from findSuperClass import FindSuperClass
        # Loops over the lines in the first function
        for line in self.first_function:
            # Splits the line at the period to separate the super class from the function
            super_class_string = line.split('.')[0]
            super_class_function_string = line.split('.')[1]
            # Find the super class with the string of the super class name
            super_class_finder = FindSuperClass()
            super_class = super_class_finder.with_name(super_class_string)
            try:
                super_class.preform_action(super_class_function_string)
            except Exception as e:
                print str(e)


class Variables(object):
    def __init__(self):
        self.ints = {}
        self.strings = {}
        self.start_of_vars = lines.index("vars {")
        self.end_of_vars = find_next_closing_bracket(self.start_of_vars)
        self.vars = lines[self.start_of_vars + 1: self.end_of_vars]
        self.store_strings()

    def find_variable_with_name(self, name):
        return self.strings[str(name)]

    def store_strings(self):
        for var in self.vars:
            # Looks for the Variables with the keyword "String"
            if var[:6] == 'String':
                # Splits the string to get the name of the Variable
                var_name = var.split('(')[1].split(')')[0]
                # Splits the string to get the value of the Variable
                var_val = var.split('=')[1].replace(' ', '').replace('"', '')
                self.strings.update({var_name: var_val})

    def store_ints(self):
        pass


def find_next_closing_bracket(opening_bracket):
    closing_bracket = 0
    for line_num in range(len(lines)):
        if lines[line_num] == '}':
            if line_num > opening_bracket:
                closing_bracket = line_num
                break

    return closing_bracket

# Opens the program
with open('helloWorld.txt') as program:
    # Stores all the lines in the array "lines"
    lines = program.readlines()
    empty_lines = []
    # Removes \n from each line
    for line_num in range(len(lines)):
        lines[line_num] = lines[line_num].replace('\n', '')
        lines[line_num] = lines[line_num].replace('    ', '')
        # Lists all of the blank lines
        if lines[line_num] == '':
            empty_lines.append(line_num)
    # Reverses the list of empty lines to avoid index changes
    empty_lines = list(reversed(empty_lines))
    # Deletes all of the empty lines
    for empty_line in empty_lines:
        del lines[empty_line]

read_functions = Functions()
read_functions.first()
