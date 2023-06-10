"""global facts
global is_changed

is_changed = True
facts = [["plant","mango"],["eating","mango"],["seed","sprouts"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "seed":
            assert_fact(["plant",A1[1]])
        if A1[0] == "plant":
            assert_fact(["fruit",A1[1]])
        if A1[0] == "plant" and ["eating",A1[1]] in facts:
            assert_fact(["human",A1[1]])

print(facts)"""


def backward_chaining(knowledge_base, query):
    if query in knowledge_base:
        return True
    else:
        for rule in knowledge_base:
            consequent, antecedents = rule
            if query == consequent:
                result = True
                for antecedent in antecedents:
                    result = result and backward_chaining(knowledge_base, antecedent)
                if result:
                    return True
        return False

# Knowledge base rules
knowledge_base = [
    ("crime(sell_weapons(Robert, Country), American)", []),
    ("enemy(Country, America)", []),
    ("owns(Country, missiles)", []),
    ("sold(Robert, missiles, Country)", []),
]

# Query
query = "crime(sell_weapons(Robert, Country), American)"

# Perform backward chaining
result = backward_chaining(knowledge_base, query)

# Print the result
if result:
    print("Robert has committed a crime by selling weapons to Country A.")
else:
    print("Robert has not committed a crime by selling weapons to Country A.")