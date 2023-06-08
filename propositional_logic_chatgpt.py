class Proposition:
    def __init__(self, name):
        self.name = name

    def evaluate(self, model):
        raise NotImplementedError("Subclasses must implement evaluate() method.")


class Variable(Proposition):
    def evaluate(self, model):
        return model[self.name]


class UnaryOperator(Proposition):
    def __init__(self, operand):
        super().__init__(None)
        self.operand = operand

    def evaluate(self, model):
        raise NotImplementedError("Subclasses must implement evaluate() method.")


class Not(UnaryOperator):
    def evaluate(self, model):
        return not self.operand.evaluate(model)


class BinaryOperator(Proposition):
    def __init__(self, left, right):
        super().__init__(None)
        self.left = left
        self.right = right

    def evaluate(self, model):
        raise NotImplementedError("Subclasses must implement evaluate() method.")


class And(BinaryOperator):
    def evaluate(self, model):
        return self.left.evaluate(model) and self.right.evaluate(model)


class Or(BinaryOperator):
    def evaluate(self, model):
        return self.left.evaluate(model) or self.right.evaluate(model)


# Example usage:
# Create proposition variables
p = Variable("p")
q = Variable("q")
r = Variable("r")

# Create a complex proposition
complex_proposition = And(p, Or(q, Not(r)))

# Create a model (truth assignment) for the variables
model = {"p": True, "q": False, "r": True}

# Evaluate the complex proposition using the model
result = complex_proposition.evaluate(model)

# Print the result
print(result)
