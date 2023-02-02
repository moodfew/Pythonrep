filename = 'learning_python.txt'

print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n--- Looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())


print("\n")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
