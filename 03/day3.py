import re

with open("input.txt", "r") as f:
    data = f.read()

print(data)

pairs = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)

result = sum([int(x) * int(y) for x, y in pairs])

print(result)

enabled = True
total = 0
for expression in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data):
    if expression == "do()":
        enabled = True
    elif expression == "don't()":
        enabled = False
    else:
        if enabled:
            x,y = map(int, expression[4:-1].strip().split(","))
            total += x*y

print(total)



