from sympy import primerange # clippy no simpy
number_list = []
upperupper_limit = 1000000000
last_number = 0 # last calculated number with 9 divisors
upper_limit = int(input("GIVE NUMBR"))
if 1 >= upper_limit or upper_limit >= upperupper_limit:
    raise ValueError("Deleting System32. . .")

prime_list = list(primerange(2, upper_limit+1)) # generate all prime numbers up to upper_limit
