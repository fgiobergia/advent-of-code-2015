from hashlib import md5 

def find_hash(salt, goal):
    i = 0
    goal_str = "0"*goal
    while True:
        bin_str = bytes(f"{salt}{i}", "utf8")
        if md5(bin_str).hexdigest()[:goal] == goal_str:
            return i
        i += 1

if __name__ == "__main__":
    salt = "ckczppom"
    print(find_hash(salt, 5))
    print(find_hash(salt, 6))
