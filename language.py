class Classes(object):
    def __init__(self):
        self.start_of_class = 0
        self.end_of_class = 0
        self.class_lines = []

    def find_start_and_end_of_class(self):
        empty_class_lines_index = 0
        for line in lines:
            # If the line is indented ignore it so that it can find the start and end of the class
            if not line[:4] == '    ':
                if line[:5] == 'class':
                    self.start_of_class = empty_class_lines_index
                elif line == '}':
                    self.end_of_class = empty_class_lines_index

            empty_class_lines_index += 1

        self.save_class_data()

    def save_class_data(self):
        for line in lines[self.start_of_class + 1: self.end_of_class]:
            self.class_lines.append(line[4:])


class Functions(object):
    def __init__(self, class_lines):
        self.lines = class_lines
        self.start_of_first = self.lines.index("void first() {")
        self.end_of_first = find_next_closing_bracket(self.start_of_first, lines)
        self.first_function_lines = self.lines[self.start_of_first + 1: self.end_of_first - 1]

    def run_function_with_lines(self, function_lines):
        from findSuperClass import FindSuperClass
        function_lines = [i[4:] for i in function_lines]
        index_line_num = 0
        # Loops over the lines in the first function
        for line in function_lines:
            # Checks if the function has a superclass
            if '.' in line:
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
            else:
                if line[:2] == 'if':
                    from controlFlow import IfStatements
                    if_statement = IfStatements()
                    # process_statements returns whether the statement should run
                    if if_statement.process_statement(line):
                        # Runs the if statement
                        end_of_statement = find_next_closing_bracket(index_line_num, function_lines)
                        print index_line_num, end_of_statement
                elif line[:4] == 'while':
                    pass

            index_line_num += 1


class Variables(object):
    def __init__(self, lines_to_search):
        self.ints = {}
        self.strings = {}
        self.lines_to_search = lines_to_search
        self.save_vars()

    def find_variable_with_name(self, name):
        return_value = ''
        if str(name) in self.strings:
            return_value = self.strings[str(name)]
        elif str(name) in self.ints:
            return_value = self.ints[str(name)]
        return return_value

    def save_vars(self):
        for line in self.lines_to_search:
            # Searches for the different types of variables
            if line[:3] == 'int':
                # Splits the int into the name and value
                name, value = line.replace('int', '').replace(' ', '').split('=')
                # Adds the name and value to the dictionary of ints
                self.ints.update({name: value})
            if line[:6] == 'String':
                # Splits the string into the name and value
                name, value = line.replace('String', '').replace(' ', '').replace('"', '').split('=')
                # Adds the name and value to the dictionary of strings
                self.strings.update({name: value})


def find_next_closing_bracket(opening_bracket, lines_to_process):
    closing_bracket = 0
    print lines_to_process
    for line_num in range(len(lines_to_process)):
        if lines[line_num] == '}':
            if line_num > opening_bracket:
                closing_bracket = line_num
                break

    return closing_bracket


def clean_program():
    empty_lines = []
    for line_num in range(len(lines)):
        lines[line_num] = lines[line_num].replace('\n', '')
        # Lists all of the blank lines
        if lines[line_num] == '' or lines[line_num][0] == '#':
            empty_lines.append(line_num)
    # Reverses the list of empty lines to avoid index changes
    empty_lines = list(reversed(empty_lines))
    # Deletes all of the empty lines
    for empty_line in empty_lines:
        del lines[empty_line]


# Opens the program
with open('helloWorld.txt') as program:
    # Stores all the lines in the array "lines"
    lines = program.readlines()
    clean_program()

# Makes sure it only runs once
if __name__ == "__main__":
    classes = Classes()
    classes.find_start_and_end_of_class()
    variables = Variables(classes.class_lines)
    read_functions = Functions(classes.class_lines)
    read_functions.run_function_with_lines(read_functions.first_function_lines)

