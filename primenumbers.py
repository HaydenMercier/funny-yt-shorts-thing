import numpy as np
import matplotlib.pyplot as plt


def get_primes(n_max):
    nums = []
    sieve = [True] * (n_max + 1)
    for p in range(2, n_max + 1):
        if sieve[p] and p % 2 == 1:
            nums.append(p)
            for i in range(p, n_max + 1, p):
                sieve[i] = False
    return nums


def get_multiples(n_max, number):
    nums = []
    for i in range(1, n_max + 1):
        if i % number == 0:
            nums.append(i)
    return nums


def get_squares(n_max):
    nums = []
    for i in range(1, n_max + 1):
        nums.append(i**2)
    return nums


def get_cubes(n_max):
    nums = []
    for i in range(1, n_max + 1):
        nums.append(i**3)
    return nums


def plot_num_polar(n_max, word, number):
    if word.lower() == "prime" or word.lower() == "primes":
        phrase = "prime numbers"
        nums = get_primes(n_max)
    elif word.lower() == "multiple" or word.lower() == "multiples":
        phrase = f"multiples of {number}"
        nums = get_multiples(n_max, number)
    elif word.lower() == "square" or word.lower() == "squares":
        phrase = f"square numbers"
        nums = get_squares(n_max)
    elif word.lower() == "cube" or word.lower() == "cubes":
        phrase = f"cube numbers"
        nums = get_cubes(n_max)
    else:
        print("Invalid input. Please choose a valid option.")
        return

    theta = np.deg2rad(nums)
    r = np.array(nums)
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    ax.scatter(theta, r, s=2, c='k')
    ax.set_title(f"Polar Plot of {phrase} up to {n_max}")
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_xticks(np.deg2rad(np.arange(0, 360, 45)))
    ax.set_xticklabels(['0°', '45°', '90°', '135°', '180°', '225°', '270°', '315°'])
    
    yticks = np.arange(0, n_max, n_max // 5)
    ax.set_yticks(yticks)
    ax.set_yticklabels([f"{int(y)}" for y in yticks])
    ax.grid(True)
    plt.show()


word = input("What types of numbers would you like to plot? ")
if word.lower() == "multiple" or word.lower() == "multiples":
    number = int(input("Of? "))
else:
    number = 0
n_max = int(input("Up until? "))
plot_num_polar(n_max, word, number)