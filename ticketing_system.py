# TICKETING SYSTEM

'''
You are making a ticketing system.
The price of a single ticket is $100.
For children under 3 years old, the ticket is free.

Your program needs to take the ages of 5 passengers as input and output the total price for their tickets.
'''

# while loop - continue
# meaning skipping the one who meets the condition

# declare variable
total = 0
i = 0

# while i is less than 5 do the code under it
while i < 5:
    # get the input of the user
    age = int(input())
    # add i to plus one each iteration
    i += 1
    
    # condition where the age is 3, skip it using continue
    if age < 3:
        continue
    # otherwise add 100 pesos each passenger in bus
    total = total + 100
    
print(total)
      