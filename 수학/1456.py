import math

def find_primes_up_to(max_num):
    sieve = [True] * (max_num+1)
    sieve[0] = sieve[1] = False
    
    for start in range(2, int(math.sqrt(max_num))+1):
        if sieve[start]:
            for multiple in range(start*start, max_num+1, start):
                sieve[multiple]= False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def count_almost_primes(a,b):
    limit = int(math.sqrt(b))+1
    primes = find_primes_up_to(limit)
    count = 0
    
    for prime in primes:
        power = prime * prime
        while power <= b:
            if power >= a:
                count +=1
            if power > b // prime:
                break
            
            power *= power
    
    return count

def main():
    a, b = map(int, input().split())
    result = count_almost_primes(a,b)
    print(result)

main()