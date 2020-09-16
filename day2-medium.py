first = 1
num = 4000000000000
next_sum = 2
fevenacci = 0
while next_sum < num:
    if next_sum % 2 == 0:
        fevenacci += next_sum
    temp = next_sum
    next_sum += first
    first = temp

if __name__ == "__main__":
    print(fevenacci)
