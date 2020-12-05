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
    def can_beta_r(self):
        return False

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

    def can_beta_r(self):
        if isinstance(self.lambdaterma, Abstraction):
            return True
        else:
            return self.lambdaterma.can_beta_r() or self.lambdatermb.can_beta_r()

    def __str__(self):
        if isinstance(self.lambdaterma, Abstraction) and isinstance(self.lambdatermb, Abstraction):
            return ("(" + str(self.lambdaterma) + ")" + "(" + str(self.lambdatermb) + ")")
        elif isinstance(self.lambdaterma, Abstraction):
            return ("("+ str(self.lambdaterma) + ")"+ str(self.lambdatermb))
        elif isinstance(self.lambdatermb, Abstraction):
            return (str(self.lambdaterma) + "("+ str(self.lambdatermb) + ")")
        else:
            return (str(self.lambdaterma) + str(self.lambdatermb))
    def __repr__(self):
        return str(self)
