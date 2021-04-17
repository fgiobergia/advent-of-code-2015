if __name__ == "__main__":
    with open("day01.input") as f:
        directions = f.readline()
    print(directions.count("(")-directions.count(")"))

    curr_pos = 0
    for pos, i in enumerate(directions):
        if i == "(":
            curr_pos += 1
        else:
            curr_pos -= 1
        if curr_pos < 0:
            break

    print(pos+1)
