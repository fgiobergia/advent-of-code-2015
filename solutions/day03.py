if __name__ == "__main__":
    with open("day03.input") as f:
        instructions = f.readline()

    visited = set()
    curr = (0,0)
    for ins in instructions:
        visited.add(curr)
        curr = ( curr[0] + (ins == "^") - (ins == "v"), curr[1] + (ins == ">") - (ins == "<") )

    print(len(visited))

    visited = set()
    curr_a = (0,0)
    curr_b = (0,0)
    for pos, ins in enumerate(instructions):
        visited.add(curr_a)
        visited.add(curr_b)
        if pos % 2:
            curr_a = ( curr_a[0] + (ins == "^") - (ins == "v"), curr_a[1] + (ins == ">") - (ins == "<") )
        else:
            curr_b = ( curr_b[0] + (ins == "^") - (ins == "v"), curr_b[1] + (ins == ">") - (ins == "<") )
    print(len(visited))
