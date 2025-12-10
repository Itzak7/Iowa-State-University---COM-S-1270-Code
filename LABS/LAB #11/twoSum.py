def twoSumLoops(Num,Answer):
    for i in range(len(Num)):
        for j in range(i + 1, len(Num)):
            if Num[i] + Num[j] == Answer:
                return [i, j]
    return None


def twoSumDict(Num,Answer):
    X = {}
    for i in range(len(Num)):
        Y = Answer - Num[i]
        if Y in X:
            return [X[Y], i]
        X[Num[i]] = i
    return None


def twoSumLoopsAll(Num,Answer):
    X = []
    for i in range(len(Num)):
        for j in range(i + 1, len(Num)):
            if Num[i] + Num[j] == Answer:
                X.append([i, j])
    return X


def twoSumDictAll(Num,Answer):
    X = {}
    Y = []
    for i in range(len(Num)):
        value = Num[i]
        need = Answer - value
        if need in X:
            for Z in X[need]:
                Y.append([Z, i])
        if value not in X:
            X[value] = []
        X[value].append(i)
    return Y


def main():
    Number = [1,2,3,4,5,7,9]
    Answer = 10
    print(twoSumLoops(Number,Answer))
    print(twoSumDict(Number,Answer))
    print(twoSumLoopsAll(Number,Answer))
    print(twoSumDictAll(Number,Answer))


if __name__ == "__main__":
    main()

