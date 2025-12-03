def find_max():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    print("The maximum number is:", maximum)

find_max()
