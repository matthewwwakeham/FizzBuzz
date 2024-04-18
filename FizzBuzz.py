def FizzBuzz(input):
    
    string = ""

    input = <-- number_goes_here -->

    if input % 3 == 0 and input % 5 == 0:
        return string + "FizzBuzz"
    if input % 3 == 0:
        return string + "Fizz"
    if input % 5 == 0:
        return string + "Buzz"
    else:
        return input
    
print(FizzBuzz(input))
