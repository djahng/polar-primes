import time
import numpy as np
import matplotlib.pyplot as plt


def primes_sieve_supercharged(n):
    sieve = np.ones(n // 2, dtype=np.bool)

    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = False

    return np.concatenate(([2], 2 * np.nonzero(sieve)[0][1::] + 1))


def primes_sieve(n):
    primes = np.ones(n, dtype=bool)
    primes[0] = primes[1] = False

    for i in range(2, n):
        if primes[i]:
            primes[i**2::i] = False

    return np.flatnonzero(primes)


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False

    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False

    return True


def primes_naive(n):
    primes = [2]

    for i in range(3, n):
        if is_prime(i):
            primes.append(i)

    return primes


def polar_plot(r, theta, area=0.01):
    bg_color = '#000000'

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    ax.grid(False)
    ax.set_yticklabels([])
    ax.set_facecolor(bg_color)
    fig.patch.set_facecolor(bg_color)
    c = ax.scatter(r, theta, marker="o", s=area)
    plt.show()


def timer(f, n=1000):
    t_start = time.time()
    r = f(n)
    t_end = time.time()

    print(f'Found {len(set(r))} primes in {t_end-t_start} seconds.')
    print(f'Head: {r[:10]}')
    print(f'Tail: {r[-10:]}')


if __name__ == '__main__':
    num_primes = 1000000

    p = primes_sieve_supercharged(num_primes)

    plots = [(100, 1.5), (2500, 1.5), (1000000, 0.005)]

    for N, n in plots:
        polar_plot(p[:N], p[:N], area=n)
