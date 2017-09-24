class IfStatements:
    def __init__(self):
        pass

    def process_statement(self, if_statement):
        should_run = False
        if 'and' in if_statement or 'or' in if_statement:
            self.compare_values_of_compound_statements()
        else:
            should_run = self.compare_values_of_single_statement(if_statement)

        return should_run

    def compare_values_of_single_statement(self, if_statement):
        should_run = False
        if_statement = if_statement.replace('if', '').replace(' ', '').replace('{', '')
        if '==' in if_statement:
            values = if_statement.split('==')
            print values
            if values[0] == values[1]:
                should_run = True
            else:
                should_run = False
        elif '!=' in if_statement:
            print 'Not Equal'
        elif '>=' in if_statement:
            print 'Greater or Equal'
        elif '<=' in if_statement:
            print 'Less or Equal'
        elif '>' in if_statement:
            print 'Greater'
        elif '<' in if_statement:
            print 'Less'

        return should_run

    def compare_values_of_compound_statements(self):
        pass
