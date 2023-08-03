select = input("1 or 2: ")

if select == "1":
    with open("input_day1.txt") as f:
        floor = 0
        floor_changes = {"(": 1, ")": -1}
        for c in f.read():
            floor += floor_changes.get(c, 0)

    print(floor)

if select == "2":
    with open("input_day1.txt") as f:
        floor, pos = 0
        floor_changes = {"(": 1, ")": -1}
        for c in f.read():
            floor += floor_changes.get(c, 0)
            pos += 1
            if floor < 0:
                print(pos)
                break
