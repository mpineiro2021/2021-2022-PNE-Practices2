import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-ex1.json").read_text()

# Create the object person from the json string
people = json.loads(jsonstring)
for person in people:
    firstname = person['Firstname']
    lastname = person['Lastname']
    age = person['Age']
    phoneNumbers = person['PhoneNumbers']
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(firstname, lastname)
    termcolor.cprint("Age: ", 'green', end="")
    print(age)
    termcolor.cprint("Phone numbers: ", 'green', end="")
    print(len(phoneNumbers))


    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])