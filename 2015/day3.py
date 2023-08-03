select = input("1 or 2: ")

if select == "1":
    with open("input_day3.txt") as f:
        sX, sY = 0, 0
        dirX, dirY = {"^": 1, "v": -1}, {"<": 1, ">": -1}
        loc = set()
        loc.add((sX, sY))
        for c in f.read():
            sX += dirX.get(c, 0)
            sY += dirY.get(c, 0)
            loc.add((sX, sY))
        print(len(loc))


if select == "2":
    with open("input_day3.txt") as f:
    
        sl = [[0,0],[0,0]]
        dirX, dirY = {"^": 1, "v": -1}, {"<": 1, ">": -1}
        loc = set()
        loc.add((sl[0][0],sl[0][1]))
        for i, c in enumerate(f.read()):
            si = i % 2            
            sl[si][0] += dirX.get(c, 0)
            sl[si][1] += dirY.get(c, 0)
            loc.add((sl[si][0], sl[si][1]))            
        print(len(loc))
