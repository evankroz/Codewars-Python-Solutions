from collections import defaultdict

def permutational_primes(n_max, k_perms):
    if n_max < 2:
        return [0, 0, 0]
    
    sieve = [True] * (n_max + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n_max ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i : n_max + 1 : i] = [False] * len(sieve[i*i : n_max + 1 : i])
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    
    digit_groups = defaultdict(list)
    for prime in primes:
        key = ''.join(sorted(str(prime)))
        digit_groups[key].append(prime)
    
    eligible_primes = []
    for group in digit_groups.values():
        if (len(group) - 1) == k_perms:
            eligible_primes.append(min(group))
    
    if not eligible_primes:
        return [0, 0, 0]
    else:
        count = len(eligible_primes)
        smallest = min(eligible_primes)
        largest = max(eligible_primes)
        return [count, smallest, largest]
    
#some very small help from perplexity labs