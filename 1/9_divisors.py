import bisect

from sympy import primerange # clippy no simpy
k = 0 # why is this k
upperupper_limit = 1000000000 # 1 billion
last_number = 0 # last calculated number with 9 divisors
upper_limit = int(input("GIVE NUMBR"))
if 1 > upper_limit or upper_limit > upperupper_limit:
    raise ValueError("Deleting System32. . .")
limit_1 = int(upper_limit ** (1/8)) # 9 divisors <=> n^8
sqrt_n = upper_limit ** (1/2) # 9 divisors <=>  p^2 * q^2, p, q primes
prime_list = list(primerange(2, int(sqrt_n)+1)) # generate all prime numbers up to sqrt of n
for i in range(2, limit_1+1): # calculate all numbers uding first method 1 IS PRIME I DON'T CARE WHAT YOU SAY
    k += 1
for i, p in enumerate(prime_list):
    max_q = sqrt_n / p  # calculate max q value for every p
    primes = bisect.bisect_right(prime_list, max_q) # Wow! i can't believe python has a function exactly for this niche use case!
    valid_count = max(0, primes - (i + 1))
    k += valid_count

print(k)

# ⣟⢿⣟⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣒⣒⣂⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀
# ⠻⣄⠹⣯⡀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⢀⡦
# ⠀⠘⢦⡈⠻⢶⡶⠶⠶⠶⠶⠶⣦⡄⠀⠀⢰⡶⠶⠶⠶⠶⠤⠤⠶⠋⢀⡴⠏⠀
# ⠀⠀⠀⠙⢦⡘⢿⣟⠛⠛⠛⠛⠛⠁⠀⠀⢸⡇⣶⣶⣶⣶⣶⣶⣶⡚⠁⠀⠀⠀
# ⠀⠀⠀⠀⠀⠹⣆⠻⣷⣄⣀⣀⣀⠀⠀⠀⢸⡇⠘⠻⠟⠗⠒⠒⠲⠶⠶⠶⣷⠆
# ⠀⠀⠀⠀⠀⠀⠈⠳⣌⣉⣉⣉⣻⡇⠀⠀⠈⢻⠏⠉⠉⠉⠉⣹⣿⠟⣠⡾⠋⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡟⢹⡇⠀⠀⠀⠀⢀⣀⣀⣠⣾⠟⣡⡶⠋⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⡇⠀⠀⣠⠞⠋⣭⣭⣭⣥⠞⠋⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⣇⣤⠞⢁⡤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠼⠏⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀

# BigPhish Pha Ze Khan BigPhish ART OF CHOKE BigPhish J Kovv BigPhish Tu Vistzz
# BigPhish Brao Kih BigPhish Ki Riy Gaon BigPhish Frao Zin BigPhish NEO BigPhish
# i main japan aviation in war thunder