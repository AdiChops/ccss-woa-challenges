import math

if __name__ == "__main__":
    num = 100
    fact = str(math.factorial(num))

    sum = 0
    for i in fact:
        sum += int(i)

    print(f'The sumtorial of {num} is {sum}')
