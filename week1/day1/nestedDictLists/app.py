# 1

from distutils.command.build_scripts import first_line_re


x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students)

sports_directory["soccer"][0] = "Andres"
print(sports_directory)


# 2

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(dict):
    for key in dict:
        print(key)


iterateDictionary(students)

# 3

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary2(first, dict):
    for i in range(len(dict)):
        print(dict[i][first])


iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)


# 4

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict, locate, instruct):
    print(str(len(some_dict[locate])) + " Locations")
    for i in range(len(some_dict[locate])):
        print(some_dict[locate][i])
    print("======================")
    print(str(len(some_dict[instruct])) + " Instructors")
    for x in range(len(some_dict[instruct])):
        print(some_dict[instruct][x])


printInfo(dojo, "locations", "instructors")
