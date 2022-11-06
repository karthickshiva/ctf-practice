from random import sample

x = list(range(16))
with open("key", "w") as f:
    for i in range(50000):
        f.write(str(hex(sample(x, 1)[0]))[2:])
