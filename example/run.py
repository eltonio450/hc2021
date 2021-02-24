from shared.file_management import prepare_file, write_output

[config, data] = prepare_file("./input/a_example")

#config est la premiere ligne, data les uivantes

print("-----config------")
print(config)

print("-----data------")
print(data)

def myAlgo(config, data):
    return  [["1"], [2, 2, 2], [3, 3, 3]]

lines = myAlgo(config, data)

print("------output------")
print(lines)

write_output(lines)