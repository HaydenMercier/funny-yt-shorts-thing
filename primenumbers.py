import numpy as np
import matplotlib.pyplot as plt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(n_max):

    primes = []
    for i in range(2, n_max + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def plot_primes_polar(n_max):
    primes = get_primes(n_max)
    theta = np.array([p for p in primes])
    r = theta.copy()

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    ax.scatter(np.deg2rad(theta), r, s=2, c='k')
    ax.set_title(f"Polar Plot of Prime Numbers up to {n_max}")
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_xticks(np.deg2rad(np.arange(0, 360, 45)))
    ax.set_xticklabels(['0°', '45°', '90°', '135°', '180°', '225°', '270°', '315°'])

    yticks = np.arange(0, n_max, n_max // 5)
    ax.set_yticks(yticks)
    ax.set_yticklabels([f"{int(y)}" for y in yticks])
    ax.grid(True)
    plt.show()

plot_primes_polar(100000)