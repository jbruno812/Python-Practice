# Write a function that returns the Max of exactly 4 numbers passed to it
#     Name the function get_max
a = 3
b = 2
c = 5
d = 1
def get_max(a,b,c,d):
    list = [a,b,c,d]
    return max(list)
get_max(a,b,c,d)


# Write a function that returns the Max of exactly 4 numbers passed to it
#     Name the function get_max
a = 3
b = 2
c = 5
d = 1
def get_max(a,b,c,d):
    list = [a,b,c,d]
    return max(list)
get_max(a,b,c,d)


# Write a function that returns the range of tens that the number is between.
#    For example, the number 4 would return, "This  number is between 0 and 10", 
#    17 would return, "This number is between 10 and 20"
#    Name the function get_between_ten
def get_between_10(x):
    if 0 <= x <= 10:
        print( "This number is between 0 and 10")
    elif 10 <= x <= 20:
        print("This number is between 10 and 20")
get_between_10(4)
get_between_10(17)


# Write a function that takes zero or more numbers and 
#    prints a response for each number indicating whether or not it is a prime number
#    Name the function is_prime
def is_prime(x):
    if (x <= 1): 
        return False
  
    for i in range(2, x): 
        if (x % i == 0): 
            return False
        
    return True

is_prime(13)