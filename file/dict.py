info={
    "key":"value",
    "name: ":"Sajid Ahamed",
    "ID: ":11221252,
    "Department:":"CSE",
    "Cgpa: ":3.26,
    "Adult:":True,
    "Learning:":"coding"
}
print(type(info))
print(info["name: "])
print(info["Adult:"])
print(info["Cgpa: "])

student={
    "name:":"Momota ahsana mim",
     "sub":{
         "physics:":92,
         "Chemistry":81,
         "Maths ":88
     }
     }
print(student["name:"],["sub"])
print(len(list(student.keys())))
print(student.values())
print(student.get("physics"))