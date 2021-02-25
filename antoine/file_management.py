

def read_file(path):
    file1 = open(path, 'r')
    lines = file1.readlines()
    return list(map(lambda l: l.strip(), lines))

def prepare_file(path):
    lines = read_file(path)
    print(lines)
    first_line = lines[0].split(" ")
    allLines = map(lambda x: x.split(" "), lines[1:])
    return [first_line, list(allLines)]

def write_output(lines, output = "output"):
    f = open(output, "w")
    prepared_lines = list(map(lambda line: "".join(str(line)), lines))
    joined_lines = "\n".join(prepared_lines)
    f.write(joined_lines)
    f.close()