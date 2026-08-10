num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("The number is not a Prime Number")
            break
    else:
        print("The number is a Prime Number")
else:
    print("The number is not a Prime Number")