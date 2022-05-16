number = 10
print(number, id(number))
number = 12
print(number, id(number))

text = "Africa"
print(text, id(text))
text += " is hot"
print(text, id(text))

#mutable
list = [1,2,3]
print(list, id(list))
list.append(4)
print(list, id(list))
#mutable
list2 = list
print(list2, id(list2))
list2.append(5)
print(list, id(list))
print(list2, id(list2))
#.append - nie zmieni pierwotnej listy
list3 = list.copy()
print(list, id(list))
print(list3, id(list3))
list3.append(6)
print(list, id(list))
print(list3, id(list3))