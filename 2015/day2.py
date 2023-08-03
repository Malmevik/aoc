

select = input("1 or 2: ")

if select == "1":
    with open("input_day2_01.txt") as f:
        lines = f.read().split("\n")
        total = 0
        for line in lines:
            dimensions = list(map(int, line.split("x")))
            sides = [dimensions[0] * dimensions[1], dimensions[1] * dimensions[2], dimensions[2] * dimensions[0]]
            sides.sort()
            total += sum(sides) * 2 + sides[0]
        print(total)  

if select == "2":
    with open("input_day2_01.txt") as f:
        lines = f.read().split("\n")
        total = 0

        for line in lines:
            dimensions = list(map(int, line.split("x")))
            dimensions.sort()
            total += dimensions[0] * 2 + dimensions[1] * 2 + dimensions[0] * dimensions[1] * dimensions[2]

        print(total)
        


