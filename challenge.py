name = input("Please enter your name: ")
number = input("Please enter a number: ")

# TODO: Make sure the number is an integer

number = int(number)

# TODO: Print out the User's name and the number entered,

print("Hello {}!\nThe number {}...".format(name,number))
# making sure the two statements are on separate lines of output.


# TODO: Compare the number the user gave with the different
# FizzBuzz conditions. 
# *********************
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."
# *********************

is_fizz = number % 3 == 0
is_buzz = number % 5 == 0

if is_fizz and is_buzz:
    print("is a FizzBuzz number.")
elif is_buzz:
    print("is a Buzz number.")
elif is_fizz:
    print("is a Fizz number.")
else:
    print("is neither a Fizzy or a Buzzy number.")
    




















