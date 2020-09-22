total = 0
squared = 0
for i in range(1, 1000001, 1):
    total += i
    squared += i*i

diff = (total*total) - squared
if __name__ == "__main__":
    print(diff)
