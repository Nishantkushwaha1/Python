
# SETS:-

# d = {} ----> empty dictionary

s = set()       #---> empty sets

print(type(s))          # <class 'set'>

s = {1, 5, 34, 56, 5, 5, 5}
print(s)                        # {56, 1, 34, 5}

# Set Methods

s.add(212)
print(s)                        # {1, 34, 5, 212, 56}

s.remove(34)
print(s)                        # {1, 5, 212, 56}


#union

s1 = {1, 45, 6, 78}
s2 = {7, 8, 1, 78}

print(s1.union(s2))                 # {1, 6, 7, 8, 45, 78}
print(s1.intersection(s2))          # {1, 78}

