import json

filename = 'json.txt'
outD = dict(name='Damian', age=46, pet='dog')
s = json.dumps(outD) #konwertuje dict na str
print(type(s), s)

#to file
with open(filename, 'w') as file:
    json.dump(outD, file) #dump to file
