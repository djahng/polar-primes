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
    # Array of possible primes
    primes = np.ones(n, dtype=bool)

    # 0 and 1 are not prime numbers
    primes[0] = False
    primes[1] = False

    for i in range(2, n):
        if primes[i]:
            primes[i**2::i] = False

    # Prime numbers are the indices of the True values
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
    primes = []

    for i in range(2, n):
        if is_prime(i):
            primes.append(i)

    return primes


def polar_plot(r, theta, area=0.01, show_grid=True):
    bg_color = '#000000'

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    ax.set_yticklabels([])

    if not show_grid:
        ax.grid(False)
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

    plots = [(100, 1.7), (2500, 1.5), (1000000, 0.01)]

    # Plot it with white background and axes
    for N, n in plots:
        polar_plot(p[:N], p[:N], area=n)

    # Plot it again, make it look nice
    for N, n in plots:
        polar_plot(p[:N], p[:N], area=n, show_grid=False)
