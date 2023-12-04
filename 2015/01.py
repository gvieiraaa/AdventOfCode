from aocd import data, submit

print(data)

resultA = data.count("(") - data.count(")")
# submit(resultA)

# PART 2

floor = 0
dict = {"(":1,")":-1}
for i, k in enumerate(data[0:]):
	floor = floor + dict[k]
	if floor == -1:
		submit(i+1)
		break