# Boolean Logic Gates Types
class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def __call__(self):
        # get name of class 
        node_type = self.__class__.__name__
        if self.value is None:
            return f'{node_type}({self.name})'
        else:
            return f'{node_type}({self.name})={self.value}'
    
    @property
    def node_type(self):
        return self.__class__.__name__
 
class And(Node):
    def __init__(self, name):
        super().__init__(name)

class Or(Node):
    def __init__(self, name):
        super().__init__(name)

class Not(Node):
    def __init__(self, name):
        super().__init__(name)

class Xor(Node):
    def __init__(self, name):
        super().__init__(name)

class Input(Node):
    def __init__(self, name):
        super().__init__(name)

class Output(Node):
    def __init__(self, name):
        super().__init__(name)
