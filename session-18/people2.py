import json
import termcolor
from pathlib import Path

# -- Read the json file
json_string = Path("people2.json").read_text()#str

# Create the object person from the json string
person = json.loads(json_string)#dict

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
print()
termcolor.cprint("Name: ", 'green', end="")
print(person['Firstname'], person['Lastname'])
termcolor.cprint("Age: ", 'green', end="")
print(person['age'])

# Get the phoneNumber list
phoneNumbers = person['phoneNumber']

# Print the number of elements int the list
termcolor.cprint("Phone numbers: ", 'green', end='')
print(len(phoneNumbers))

# Print all the phone numbers
for i, num in enumerate(phoneNumbers): #enumerate para que nos pinte los dos numeros de telefono y su valor
    termcolor.cprint("  Phone {}:".format(i), 'blue', end='')
    print(num)