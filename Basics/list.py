
# List:

friend = ["Nishant","Gurdeep", "Animesh", "Hemant", "Madhur"]

print(friend[2])        # Animesh

friend[2] = "AnniDon"

print(friend[2])        # AnniDon
print(friend[0:5])      # ['Nishant', 'Gurdeep', 'AnniDon', 'Hemant', 'Madhur']

friend.append("Krishan")
print(friend)               # ['Nishant', 'Gurdeep', 'AnniDon', 'Hemant', 'Madhur', 'Krishan']

friend.insert(5,"Kaushal")
print(friend)               # ant', 'Gurdeep', 'AnniDon', 'Hemant', 'Madhur', 'Kaushal', 'Krishan']

l = [1, 54, 24, 36, 11, 5]
# l.sort()
l.reverse()
print(l)                    # [5, 11, 36, 24, 54, 1]


