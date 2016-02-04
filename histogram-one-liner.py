o = ["dog", "cat", "cat", "cat", "fish", "dog"]

print [(x, len([y for y in o if x == y])) for x in set(o)]
