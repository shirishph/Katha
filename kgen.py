f = open("input.tsv", "r")

candidates = [
    "000",
    "111",
    "222",
    "333",
    "444",
    "555",
    "666",
    "777",
    "888",
    "999"
]

inputs = []
for line in f:
    parts = line.strip().split("\t")
    inputs.append(parts)

f.close()

print("inputs: ", inputs)
last_row = inputs[-1]
print(last_row)

total_gen = int(last_row[0]) + 1
print("total_gen: ", total_gen)

gen_story = [None] * total_gen

print("gen_story", gen_story)
for inp in inputs:
    index = int(inp[0])
    print("index: ", index)
    gen_story[int(inp[0])] = inp

print("POST gen_story", gen_story)

"""
for gs in gen_story:
    print("> ", gs)
"""

