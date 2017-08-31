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
        output_array = output_original.split('+')
        output = output_array[0]
        if len(output_array) > 1:
            running_output = ''
            for item in output_array:
                if '"' in item:
                    if item[0] == ' ':
                        item = item[1:]
                    if item[-1] == ' ':
                        item = item[:-1]
                    item = item.replace('"', '')
                    running_output += item
                else:
                    from lanauge import Variables
                    variables = Variables()
                    running_output += variables.find_variable_with_name(item.replace(' ', ''))
            output = '"' + running_output + '"'

        # Checks if the output is a string or a variable
        if output[0] == '"':
            # Removes the double quotes
            output = output.replace('"', '')
            # Prints the output
            print 'Output at', str(str(time.time()) + ':'), output
        else:
            from lanauge import Variables
            variables = Variables()
            # Finds the Variable with the given name and prints it
            print 'Output at', str(str(time.time()) + ':'), variables.find_variable_with_name(output)
