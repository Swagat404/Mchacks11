import re

# Your original string with entries
a=open("final.json","r")

original_string = a.read()

# Use regular expression to add commas between each entry
json_string = re.sub(r'}{', '},{', original_string)

# Add square brackets to make it a valid JSON array
json_string = '[' + json_string + ']'
b=open("finalcorrected.json","w")
b.write(json_string)

print(json_string)
