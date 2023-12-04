from aocd import data, submit, lines #, numbers

def part1():
    stacks, instructions = data.split('\n\n')
    stack_list = [[] for i in range(9)]
    for line in stacks.split('\n')[:-1]:
        print(line)
        for i, j in enumerate(line[1::4]):
            if j != ' ':
                stack_list[i].append(j)

    print(stack_list)
    
    for instruction in instructions.split('\n'):
        x, y, z = list(map(int, instruction.split(' ')[1::2]))
        for _ in range(x):
            stack_list[z-1].insert(0, stack_list[y-1].pop(0))
    
    return ''.join(x[0] for x in stack_list)

def part2():
    stacks, instructions = data.split('\n\n')
    stack_list = [[] for i in range(9)]
    for line in stacks.split('\n')[:-1]:
        print(line)
        for i, j in enumerate(line[1::4]):
            if j != ' ':
                stack_list[i].append(j)

    print(stack_list)
    
    for instruction in instructions.split('\n'):
        x, y, z = list(map(int, instruction.split(' ')[1::2]))
        temp = stack_list[y-1][:x]
        stack_list[y-1] = stack_list[y-1][x:]
        stack_list[z-1] = temp + stack_list[z-1]
    
    return ''.join(x[0] for x in stack_list)


if __name__ == '__main__':
    print(f"Part 1: {(p1:=part1())}")
    #submit(p1)
    print(f"Part 1: {(p2:=part2())}")
    submit(p2)