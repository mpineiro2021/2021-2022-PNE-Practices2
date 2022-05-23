import json
import termcolor
from pathlib import Path

# -- Read the json file
json_string = Path("person1.json").read_text()   # leetodo el fichero en string

# Create the object person from the json string
person = json.loads(json_string)  #importamos el modulo json para trabajar con él, y hacemos un diccionario con la info del fichero json
# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# -- Read the Firstname
firstname = person['Firstname']
lastname = person['Lastname']
age = person['Age']

# Print the information on the console, in colors
print()
termcolor.cprint("Name: ", 'green', end="")
print(firstname, lastname)
termcolor.cprint("Age: ", 'green', end="")
print(age)