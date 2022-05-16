a = b = c = 10
print(a, b, c, id(a), id(b),id(c))
a = 20
print(a, b, c, id(a), id(b),id(c))

a = b = c = [1,2,3]
print(a, b, c, id(a), id(b),id(c))
a += [4]
print(a, b, c, id(a), id(b),id(c))

x = 10
y = 10
print(id(x), id(y))

y += 1
y -= 1

print(id(x), id(y))

y += 1234567890
y += 1234567899
y -= 1234567890
y -= 1234567899

print(id(x), id(y))