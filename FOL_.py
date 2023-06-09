"""# Import libraries
from aima.logic import expr, FolKB, fol_fc_ask
from aima.utils import expr

# The main entry point for this module
def main():
    # Create an array to hold clauses
    clauses = []
    # Add first-order logic clauses (rules and facts)
    clauses.append(expr("(American(x) & Weapon(y) & Sells(x, y, z) & Hostile(z)) ==> Criminal(x)"))
    clauses.append(expr("Enemy(Nono, America)"))
    clauses.append(expr("Owns(Nono, M1)"))
    clauses.append(expr("Missile(M1)"))
    clauses.append(expr("(Missile(x) & Owns(Nono, x)) ==> Sells(West, x, Nono)"))
    clauses.append(expr("American(West)"))
    clauses.append(expr("Missile(x) ==> Weapon(x)"))
    # Create a first-order logic knowledge base (KB) with clauses
    KB = FolKB(clauses)
    # Add rules and facts with tell
    KB.tell(expr('Enemy(Coco, America)'))
    KB.tell(expr('Enemy(Jojo, America)'))
    KB.tell(expr("Enemy(x, America) ==> Hostile(x)"))
    # Get information from the knowledge base with ask
    hostile = fol_fc_ask(KB, expr('Hostile(x)'))
    criminal = fol_fc_ask(KB, expr('Criminal(x)'))
    # Print answers
    print('Hostile?')
    print(list(hostile))
    print('\nCriminal?')
    print(list(criminal))
    print()

# Tell Python to run the main method
if __name__ == "__main__":
    main()
"""
"""
from pyDatalog import Engine, Constant, Variable, Predicate, List

# Declare the predicates
American = Predicate("American", 1)
Weapon = Predicate("Weapon", 1)
Sells = Predicate("Sells", 3)
Hostile = Predicate("Hostile", 1)
Criminal = Predicate("Criminal", 1)
Enemy = Predicate("Enemy", 2)
Owns = Predicate("Owns", 2)
Missile = Predicate("Missile", 1)

# Create an instance of the engine
engine = Engine()

# Define the knowledge base
engine.assert_fact(American("West"))
engine.assert_fact(Weapon("M1"))
engine.assert_fact(Missile("M1"))
engine.assert_fact(Owns("Nono", "M1"))
engine.assert_fact(Enemy("Nono", "America"))
engine.assert_fact(Enemy("Coco", "America"))
engine.assert_fact(Hostile(x), if_=Enemy(x, "America"))
engine.assert_fact(Criminal(x), if_=American(x) & Weapon(y) & Sells(x, y, z) & Hostile(z))
engine.assert_fact(Sells("West", x, "Nono"), if_=Missile(x) & Owns("Nono", x))

# Query the knowledge base
hostile_query = engine.query(Hostile(x))
criminal_query = engine.query(Criminal(x))

# Check if the queries are satisfied in the knowledge base
is_hostile = len(hostile_query) > 0
is_criminal = len(criminal_query) > 0

# Print the results
print("Hostile?", is_hostile)
print("Criminal?", is_criminal)"""

"""
from prologpy import Variable, Constant, Functor, Program

# Declare the predicates
American = Functor("American", 1)
Weapon = Functor("Weapon", 1)
Sells = Functor("Sells", 3)
Hostile = Functor("Hostile", 1)
Criminal = Functor("Criminal", 1)
Enemy = Functor("Enemy", 2)
Owns = Functor("Owns", 2)
Missile = Functor("Missile", 1)

# Create a new program
program = Program()

# Add clauses to the program
program.add_clause(American(Constant("West")))
program.add_clause(Weapon(Constant("M1")))
program.add_clause(Missile(Constant("M1")))
program.add_clause(Owns(Constant("Nono"), Constant("M1")))
program.add_clause(Enemy(Constant("Nono"), Constant("America")))
program.add_clause(Enemy(Constant("Coco"), Constant("America")))
program.add_clause(Hostile(Variable("X")), Enemy(Variable("X"), Constant("America")))
program.add_clause(Criminal(Variable("X")), American(Variable("X")), Weapon(Variable("Y")),
                   Sells(Variable("X"), Variable("Y"), Variable("Z")), Hostile(Variable("Z")))
program.add_clause(Sells(Constant("West"), Variable("X"), Constant("Nono")),
                   Missile(Variable("X")), Owns(Constant("Nono"), Variable("X")))

# Query the program
hostile_query = program.query(Hostile(Variable("X")))
criminal_query = program.query(Criminal(Variable("X")))

# Print the results
print("Hostile?")
for solution in hostile_query:
    print(solution)

print("Criminal?")
for solution in criminal_query:
    print(solution)
"""
"""
import aima.utils
import aima.logic

# The main entry point for this module
def main():
    # Create an array to hold clauses
    clauses = []
    
    # Add first-order logic clauses (rules and facts)
    clauses.append(aima.utils.expr("(American(x) & Weapon(y) & Sells(x, y, z) & Hostile(z)) ==> Criminal(x)"))
    clauses.append(aima.utils.expr("Enemy(Nono, America)"))
    clauses.append(aima.utils.expr("Owns(Nono, M1)"))
    clauses.append(aima.utils.expr("Missile(M1)"))
    clauses.append(aima.utils.expr("(Missile(x) & Owns(Nono, x)) ==> Sells(West, x, Nono)"))
    clauses.append(aima.utils.expr("American(West)"))
    clauses.append(aima.utils.expr("Missile(x) ==> Weapon(x)"))

    # Create a first-order logic knowledge base (KB) with clauses
    KB = aima.logic.FolKB(clauses)

    # Add additional rules and facts with tell
    KB.tell(aima.utils.expr('Enemy(Coco, America)'))
    KB.tell(aima.utils.expr('Enemy(Jojo, America)'))
    KB.tell(aima.utils.expr("Enemy(x, America) ==> Hostile(x)"))

    # Get information from the knowledge base with ask
    hostile = aima.logic.fol_fc_ask(KB, aima.utils.expr('Hostile(x)'))
    criminal = aima.logic.fol_fc_ask(KB, aima.utils.expr('Criminal(x)'))

    # Print answers
    print('Hostile?')
    print(list(hostile))
    print('\nCriminal?')
    print(list(criminal))
    print()

# Tell Python to run the main method
if __name__ == "__main__":
    main()
"""




"""
from itertools import product


class Symbol:
    def __init__(self, name: str, arity: int):
        self.name = name
        if arity < 0:
            raise Exception("Arity needs to be an integer >= 0.")
        self.arity = arity


class Language:
    def __init__(
        self, function_symbols: set, relation_symbols: set, constant_symbols: set
    ):
        self.function_symbols = function_symbols
        self.relation_symbols = relation_symbols
        self.constant_symbols = constant_symbols
        self.symbols = self.function_symbols.union(
            self.relation_symbols, self.constant_symbols
        )

    def print(self):
        if self.function_symbols:
            print()
            print("Function symbols:")
            print(
                "\n".join(
                    [
                        f"{symbol.name}, of arity {symbol.arity}"
                        for symbol in self.function_symbols
                    ]
                )
            )
        if self.relation_symbols:
            print()
            print("Relation symbols:")
            print(
                "\n".join(
                    [
                        f"{symbol.name}, of arity {symbol.arity}"
                        for symbol in self.relation_symbols
                    ]
                )
            )
        if self.constant_symbols:
            print()
            print("Constant symbols:")
            print("\n".join([symbol.name for symbol in self.constant_symbols]))


class Forall:
    def __init__(self, expression):
        self.expression = expression


class Exists:
    def __init__(self, expression):
        self.expression = expression


class L_Structure:
    def __init__(self, universe: set, language: Language, interpretations: dict):
        if not universe:
            raise Exception("An L-structure must have a non-empty universe.")
        self.universe = universe
        self.language = language
        self.interpretations = interpretations
        try:
            for symbol in self.language.symbols:
                _ = self.interpretations[symbol]
        except:
            raise Exception(
                "Please provide an interpretation for all symbols in the language."
            )
        for symbol in self.language.function_symbols:
            for tuple in cartesian_product(self.universe, symbol.arity):
                if self.interpretations[symbol](tuple) not in self.universe:
                    raise Exception(
                        f"{symbol.name} does not have a valid interpretation."
                    )

    def interpret(self, symbols: set()):
        for symbol in symbols:
            print()
            print(symbol.name + " interpretation:")
            if symbol in self.language.function_symbols:
                print(
                    "\n".join(
                        [
                            f"{symbol.name}{x} = {self.interpretations[symbol](x)}"
                            for x in cartesian_product(self.universe, symbol.arity)
                        ]
                    )
                )
            elif symbol in self.language.relation_symbols:
                print(self.interpretations[symbol])

    def validate(self, sentence):
        if isinstance(sentence, Forall):
            return all(self.validate(sentence.expression(x)) for x in self.universe)
        if isinstance(sentence, Exists):
            return any(self.validate(sentence.expression(x)) for x in self.universe)
        else:
            return sentence

    def is_model_of(self, theory):
        return all([self.validate(sentence) for sentence in theory])


def cartesian_product(set, n):
    if n == 1:
        return set
    else:
        return product(set, repeat=n)


if __name__ == "__main__":
    plus_symbol = Symbol("+", 2)
    inverse_symbol = Symbol("-", 1)
    zero_symbol = Symbol("0", 0)

    group_language = Language(
        function_symbols={plus_symbol, inverse_symbol},
        relation_symbols=set(),
        constant_symbols={zero_symbol},
    )

    universe = {0, 1, 2, 3, 4}
    m = L_Structure(
        universe=universe,
        language=group_language,
        interpretations={
            plus_symbol: lambda x: (x[0] + x[1]) % 5,
            inverse_symbol: lambda y: -y % 5,
            zero_symbol: 0,
        },
    )

    plus = m.interpretations[plus_symbol]
    inverse = m.interpretations[inverse_symbol]
    zero = m.interpretations[zero_symbol]

    theory_of_groups = [
        Forall(
            lambda x: Forall(
                lambda y: Forall(
                    lambda z: plus((x, plus((y, z)))) == plus((plus((x, y)), z))
                )
            )
        ),
        Forall(lambda x: plus((x, inverse(x))) == zero),
        Forall(lambda x: plus((inverse(x), x)) == zero),
        Forall(lambda x: plus((x, zero)) == x),
        Forall(lambda x: plus((zero, x)) == x),
    ]

    print(m.is_model_of(theory_of_groups))


"""