"""
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.
"""

def mutate_string(string, position, character):
    l, i = list(), 0
    while i < len(string):
      if (i == position):
        l += [character]
      else:
        l += [string[i]]
      i += 1
    return ''.join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
