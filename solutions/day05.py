from collections import defaultdict

def is_nice(string):
    count_vowels = 0
    has_sequence = False
    has_forbidden = False
    for i in range(len(string)):
        count_vowels += string[i] in {'a','e','i','o','u'}
        has_sequence |= i < len(string)-1 and string[i] == string[i+1]
        has_forbidden |= i < len(string)-1 and string[i:i+2] in {"ab","cd","pq","xy"}
    return count_vowels > 2 and has_sequence and not has_forbidden

def is_new_nice(string):
    repeats = defaultdict(set)
    has_repeated = False
    for i in range(len(string)):
        has_repeated |= i+2 < len(string) and string[i] == string[i+2]
        if i+1 < len(string):
            repeats[string[i:i+2]].update({i, i+1})
    return has_repeated and len([ v for v in repeats.values() if len(v) > 3] )



if __name__ == "__main__":
    with open("day05.input") as f:
        strings = [ line.strip() for line in f.readlines() ]

    print(len([ string for string in strings if is_nice(string)]))
    print(len([ string for string in strings if is_new_nice(string)]))
