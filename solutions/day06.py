import re
import numpy as np

if __name__ == "__main__":
    ops = []
    with open("day06.input") as f:
        # turn on 489,959 through 759,964
        for line in f.readlines():
            match = re.match(r"(toggle|turn (?:on|off)) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})", line)
            if not match:
                raise Exception("incorrect file syntax")
            action, *coords = match.groups()
            from_x, from_y, to_x, to_y = map(int, coords)
            ops.append((action, from_x, from_y, to_x, to_y))
    
    m = np.zeros((1000, 1000), dtype=np.int8)
    for action, from_x, from_y, to_x, to_y in ops:
        if action == "toggle":
            m[from_x:to_x+1, from_y:to_y+1] = 1 - m[from_x:to_x+1, from_y:to_y+1]
        else:
            m[from_x:to_x+1, from_y:to_y+1] = action == "turn on"
    
    print(m.sum())

    m = np.zeros((1000, 1000), dtype=np.int8)
    for action, from_x, from_y, to_x, to_y in ops:
        if action == "toggle":
            m[from_x:to_x+1, from_y:to_y+1] += 2
        elif action == "turn on":
            m[from_x:to_x+1, from_y:to_y+1] += 1
        else:
            m[from_x:to_x+1, from_y:to_y+1] -= 1
            m[m<0] = 0
    
    print(m.sum())