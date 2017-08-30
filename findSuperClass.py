class FindSuperClass(object):
    def __init__(self):
        pass

    def with_name(self, name):
        class_to_return = None
        if name == 'System':
            from system import System
            class_to_return = System()
        return class_to_return
