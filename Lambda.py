class LambdaTerm():
    "A Classic Lambda Term"

class Atom(LambdaTerm):
    "A Simple Atom"
    def __init__(self, value):
        self.value = value
        
class Abstraction(LambdaTerm):
    "An Abstraction, QED"
    def __init__(self, name, body):
        self.name = name
        self.body = body

        class Application(LambdaTerm):
    "An Application thing"
    def __init__(self, lta, ltb): #ltX : LambdaTerm X
        self.lambdaterma : LambdaTerm = lta
        self.lambdatermb : LambdaTerm = ltb 
