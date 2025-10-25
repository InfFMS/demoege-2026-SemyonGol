# 1)A - 8
# B - 3
# C - 5
# D - 4
# E - 2
# F - 7
# G - 1
# Ответ: 17+37=52

#2) yxzw

# 3) 186352 Решено в таблице

# 4) 16
# 5) 26 Код ниже
def task_five():
    def bin(N):
        Bin = ''
        while N != 1:
            Bin += str(N % 2)
            N = N // 2
        Bin += str(N)
        Bin = Bin[::-1]
        return Bin

    def dec(N):
        N = N[::-1]
        Dec = 0
        for i in range(len(N)):
            Dec += int(N[i]) * 2 ** i
        return Dec

    def F(N):
        BinN = bin(N)
        if N % 3 == 0:
            BinN = BinN + BinN[len(BinN) - 3:]
        else:
            BinN += bin((N % 3) * 3)
        return dec(BinN)

    i = 1
    while True:
        if F(i) >= 200:
            print(i)
            break
        else:
            i += 1

# 6) 216
# 7) 123937
# 8) 5058