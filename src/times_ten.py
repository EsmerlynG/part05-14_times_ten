# Write your solution here
def times_ten(start_index: int, end_index: int):
    numbers = {}

    for num in range(start_index, end_index + 1):
        numbers[num] = num * 10

    return numbers

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)
    