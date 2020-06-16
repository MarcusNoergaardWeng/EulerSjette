import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def get_primes_below_n(n):
    primes = []
    for i in range(2,n):
        if(is_prime(i)):
            primes.append(i)
    return primes

# O(n^2) complexity
def find_highest_consecutive_prime_sum(limit):
    # A sum of at least two terms must exist
    # Thus, we only look at primes below half the limit (truncated)
    primes = get_primes_below_n(limit)

    # Iterate through starting primes
    max_chain = 1
    max_prime_sum = 2

    index_outer = 0

    while index_outer < len(primes):
        prime = primes[index_outer]
        current_prime_sum = prime

        #print("In outer loop. Current prime is: " + str(prime))

        index = index_outer + 1
        counter = 1

        while index < len(primes):
            counter += 1
            current_prime_sum += primes[index]
            if(current_prime_sum > limit):
                break
            #print("In inner loop. Current inner prime is: " + str(primes[index]) + ". Current sum is: " + str(current_prime_sum))

            if(is_prime(current_prime_sum)):
                #print("A consecutive prime sum was found. The sum is: " + str(current_prime_sum) + ". The chain counter is " + str(counter))
                if(counter > max_chain):
                    max_chain = counter
                    max_prime_sum = current_prime_sum
                    #print("A new record chain was found.")
            
            index += 1
        index_outer += 1
    #print("The highest had a counter of " + str(max_chain) + ". The consecutive prime sum was " + str(max_prime))
    return (max_chain, max_prime_sum)

find_highest_consecutive_prime_sum(1000000)
# Counter of 543, sum of 997651