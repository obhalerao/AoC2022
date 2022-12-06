lines = [l.strip() for l in open("../input.txt").readlines()]

line = lines[0]
for i in range(0, len(line)-3):
    l = line[i:i+4]
    if len(set(list(l))) == len(list(l)):
        print(i+4)
        break