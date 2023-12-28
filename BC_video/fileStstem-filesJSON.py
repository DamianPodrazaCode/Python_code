import json

filename = 'test.json'
outD = dict(name='Damian', age=46, pet='dog')
s = json.dumps(outD) #konwertuje dict na str
print(type(s), s)

#to file
with open(filename, 'w') as file:
    json.dump(outD, file) #dump to file

#from string
inD = json.loads(s) #load dict fro str
print(type(inD), inD)

#from file
filename = 'example.json'
with open(filename, 'r') as file:
    fileLoad = json.load(file)
print(type(fileLoad))
print(fileLoad)
