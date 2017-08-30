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
            print 'Should Print'
            self.print_output(self.parameters)

    def print_output(self, output):
        # Checks if the output is a string or a variable
        if output[0] == '"':
            # Removes the double quotes
            output = output.replace('"', '')
            # Prints the output
            print 'Output at', str(str(time.time()) + ':'), output
        else:
            from lanauge import Variables
            variables = Variables()
            print variables.find_variable_with_name(output)
