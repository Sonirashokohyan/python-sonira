ourClass = ["yusof", "bozorg", "oranos"]
ourClass.append("sonira")
print(ourClass)


afghanistan = ["kabul", "kunar"]
afghanistan.clear()


ourClass = ["yusof", "bozorg", "oranos"]
x = ourClass.copy()
print(x)


countries = ["afghanistan", "pakistan", "iran"]
x = countries.count("pakistan")
print(x)


class1 = ["sonira", "yusof", "oranos"]
class2 = ["behshta", "marwa"]
class1.extend(class2)
print(class1)

countries = ["afghanistan", "pakistan", "iran"]
x = countries.index("iran")
print(x)



head = ["eyes", 'nose', "ears", "mouth"]
head.insert(2, "face")
print(head)

head = ["eyes", 'nose', "ears", "mouth"]
head.pop(2)
print(head)


class2 = ["behshta", "marwa"]
class2.remove("marwa")
print(class2)

girls = ["zahra", "khojesta", "marwa", "freshta"]
girls.sort()
print(girls)

girls = ["zahra", "khojesta", "marwa", "freshta"]
girls.reverse()
print(girls)

girls = ["zahra", "khojesta", "marwa", "freshta"]
print(girls[-1::-1])