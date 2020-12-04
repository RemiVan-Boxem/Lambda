class LambdaTerm():
    """A Classic Lambda Term"""

class Atom(LambdaTerm):
    """A Simple Atom"""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self)

class Abstraction(LambdaTerm):
    """An Abstraction, QED"""
    def __init__(self, name : str, body : LambdaTerm):
        self.name : str = name
        self.body : LambdaTerm = body
    def __str__(self):
        return str("λ" + str(self.name) + "." + str(self.body))
    def __repr__(self):
        return str(self)

class Application(LambdaTerm):
    """An Application thing"""
    def __init__(self, lta : LambdaTerm, ltb : LambdaTerm):
        self.lambdaterma : LambdaTerm = lta
        self.lambdatermb : LambdaTerm = ltb
    def __str__(self):
        if isinstance(self.lambdaterma, Abstraction) and isinstance(self.lambdatermb, Abstraction) == True:
            return ("(" + str(self.lambdaterma) + ")" + "(" + str(self.lambdatermb) + ")")
        elif isinstance(self.lambdaterma, Abstraction) == True:
            return ("("+ str(self.lambdaterma) + ")"+ str(self.lambdatermb))
        elif isinstance(self.lambdatermb, Abstraction) == True:
            return (str(self.lambdaterma) + "("+ str(self.lambdatermb) + ")")
        else:
            return (str(self.lambdaterma) + str(self.lambdatermb))
    def __repr__(self):
        return str(self)
