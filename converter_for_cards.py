while True:
    inpt = input("Code: ")
    if inpt == "1":
        tmp = []
        for _ in range(17):
            tmp.append([input()])
        tmp = str(tmp)
        print("[", end="")
        for i in range(1, len(tmp), 35):
            print(tmp[i:(i + 35)])
    else:
        break
