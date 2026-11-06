def square_numbers(start, end):
    odd = ""
    even = ""

    for i in range(start, end + 1):
        square = i * i

        if square % 2 == 0:
            even = even + str(square) + " "
        else:
            odd = odd + str(square) + " "

    print("Even squares:", even)
    print("Odd squares:", odd)


square_numbers(1, 10)
    
