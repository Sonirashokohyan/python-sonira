# access list
Afghanistan = ["kabul", "baghlan", "kunar", "bamyan"]
print(Afghanistan[0])
print(Afghanistan[1:4])
print(Afghanistan[:3])
print(Afghanistan[1:])
print(Afghanistan[-1:-3:-1])
print(Afghanistan[::2])


#change list
Afghanistan = ["kabul", "baghlan", "kunar", "bamyan"]
Afghanistan[0] = "logar"
print(Afghanistan)


girls = ["zahra", "freshta", 'zarghona', "parwana"]
girls[0:2] = "benafsha", "hangama"
print(girls)


girls = ["zahra", "freshta", 'zarghona', "parwana"]
girls[2:] = "nadima", "frohar"
print(girls)


girls = ["zahra", "freshta", 'zarghona', "parwana"]
girls[1:3] = "sonira", 'oranos', "husna", "rayesa"
print(girls)


#add list

tajikistan = []
tajikistan.append("vahdat")
tajikistan.append("dushanbe")
tajikistan.append("kulab")
print(tajikistan)


tajikstan = ["vahdat", "dushanbe", "kulab", "khujand"]
tajikistan.insert(1, "badakhshan")
print(tajikistan)

evenStudents = ["bozorg", "yusof", 'sonira', "oranos"]
oddStudents = ["x", "y", "z"]
evenStudents.extend(oddStudents)
print(evenStudents)

# remove list
Afghanistan = ["kabul", "baghlan", "kunar", "bamyan"]
Afghanistan.remove("kabul")
print(Afghanistan)


tajikstan = ["vahdat", "dushanbe", "kulab", "khujand"]
tajikistan.pop()
print(tajikistan)

