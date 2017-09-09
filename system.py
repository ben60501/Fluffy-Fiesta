import time


class System(object):
    def __init__(self):
        self.func = ''
        self.parameters = ''

    def preform_action(self, action):
        self.func = action.split('(')[0]
        self.parameters = action.split('(')[1]
        self.parameters = self.parameters.replace(')', '')
        self.find_function()

    def find_function(self):
        if self.func == 'print':
            self.print_output(self.parameters)

    def print_output(self, output_original):
        # Splits the output at the pluses if there are any
        output_array = output_original.split('+')
        output = output_array[0]
        # Checks if there is a plus in the print statement
        if len(output_array) > 1:
            # Store the current output as it loops over each thing to add
            running_output = ''
            # Loops over each thing to add
            for item in output_array:
                # Checks if it is a string or a variable
                if '"' in item:
                    # Removes the spaces before and after the "
                    if item[0] == ' ':
                        item = item[1:]
                    if item[-1] == ' ':
                        item = item[:-1]
                    # Removes the quotation marks
                    item = item.replace('"', '')
                    running_output += item
                else:
                    from language import Variables
                    variables = Variables()
                    # Gets the value of the variable and adds it to the running output
                    running_output += variables.find_variable_with_name(item.replace(' ', ''))
            # Adds " to the running output so it can be processed like it is a string in the print statement
            output = '"' + running_output + '"'

        # Checks if the output is a string or a variable
        if output[0] == '"':
            # Removes the double quotes
            output = output.replace('"', '')
            # Prints the output
            print 'Output at', str(str(time.time()) + ':'), output
        else:
            from language import Variables
            variables = Variables()
            # Finds the Variable with the given name and prints it
            print 'Output at', str(str(time.time()) + ':'), variables.find_variable_with_name(output)
