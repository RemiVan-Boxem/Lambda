class LambdaTerm():
    "A Classic Lambda Term"

    def __init__(self, atom, functions = 0):
        self.atom = atom
        self.functions = functions

    class Atom(LambdaTerm):
        ?
