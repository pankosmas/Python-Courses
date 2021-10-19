# This mini project finds and prints all primes from 0 to 200.
# We examine the use of for loops, break command and the
# transformation of lists to tuples. Lists and tuples are both
# sequences, the main difference is that tuples cannot be modified
# and as a consequence, there are not functions like append, pop etc

primes_list = []

for N in range(2, 101):
    for i in range(2, N):
        if N % i == 0:
            break
    else:
        # else is referring to for loop.
        primes_list.append(N)

primes = tuple(primes_list)
print(primes)
print(len(primes))

# descriptive list creation
# if even and multiplier of 3

my_list = [number for number in range(100) if number % 2 == 0 and number % 3 == 0]
print(my_list)
