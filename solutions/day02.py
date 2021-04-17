if __name__ == "__main__":
    with open("day02.input") as f:
        presents = [ [ int(x) for x in line.split("x") ] for line in f.readlines() ]

    print(sum(2*(a*b+a*c+b*c)+min(a*b,c*b,a*c) for a,b,c in presents))
    print(sum(2*min(a+b,a+c,b+c)+a*b*c for a,b,c in presents))
