name = input("What's your name? ")

name = name.title()

# TODO: Ask the user by name if they understand Python while loops

response = input("{}, do you understand Python while loops?\n (Enter yes/no)  ".format(name))

# TODO: Write a while statement that checks if the user doesn't understand while loops
# TODO: Since the user doesn't understand while loops, let's explai

while response.lower() != 'yes':
    
    print("Okay {}, while loops in Python repeat as long as a certain Boolean condition is met.".format(name))
    response = input("\n{}, now do you understand Python while loops?\n (Enter yes/no)   ".format(name))
  
# TODO: Outside the while loop, congratulate the user for understanding while loops

print("\nThat's great, {}. I'm pleased that you understand Python while loops now. Excellent job!".format(name))
