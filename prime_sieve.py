def eratosthenes_sieve(N):
    # Increment once in order to remove redundancy
    N += 1
    prime = [True] * (N)
    primes_tab = [2]
    for c in range(3, N, 2):
        if prime[c] == True:
            primes_tab.append(c)
            # Mark all multiples of c as composite
            for mul_c in range(c*c, N, c):
                prime[mul_c] = False
    return primes_tab

if __name__ == '__main__':
    eratosthenes_sieve(500)
