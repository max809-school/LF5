def countTo100():
    i = 1
    while i <= 100:
        print("[Count to 100] ", i, "/100")
        i += 1


def countTo0():
    i = 100
    while i >= 1:
        print("[Count to 0] ", i, "/100")
        i -= 1


def sumAndMedianOfRange(start, end):
    summe = 0
    count = 0
    i = start
    while i <= end:
        summe += i
        count += 1
        i += 1

    if count > 0:
        mittelwert = summe / count
    else:
        mittelwert = 0

    print("[Summe und Mittelwert von Range] Summe:", summe)
    print("[Summe und Mittelwert von Range] Mittelwert:", mittelwert)


def squareOfRange():
    start = 1
    end = 100
    i = start
    while i <= end:
        print("[Quadrat von Range] ", i, "² =", i**2)
        i += 1


def factorial(n):
    num = 1
    while n > 1:
        num *= n
        n -= 1

    print("[Fakultät] ", num)


if __name__ == "__main__":
    countTo100()
    countTo0()
    sumAndMedianOfRange(1, 100)
    squareOfRange()
    factorial(6)
