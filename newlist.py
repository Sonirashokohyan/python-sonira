ourClass = ["me", "sir", "my twin brothers", "my friends", "others"]
if "me" in ourClass:
    print("yes 'me' is in ourclass")
else:
    print("no")

ourClass[3] = "girls"
print(ourClass)

ourClass.append("zahra")
print(ourClass)

class1 = ["son", "mon", "farzana"]
class2 = ["zagra", "mero", "oranos"]
class1.extend(class2)
print(class1)