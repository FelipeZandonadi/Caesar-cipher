from string import ascii_letters

alfabeto = ascii_letters + "0123456789"

print(len(alfabeto))
p = 999999
if p >= len(alfabeto):
    p = p - ((p//len(alfabeto))*len(alfabeto))
print(p)
print(alfabeto[p])
