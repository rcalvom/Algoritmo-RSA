from random import randint

k = 20


def fermat_test(value):
    for i in range(1, k):
        a = randint(2, value - 1)
        if pow(a, value - 1, value) != 1:
            return False
    return True


def random_prime(magnitude_order):
    flag = False
    while not flag:
        n = randint(pow(10, magnitude_order - 1), pow(10, magnitude_order))
        flag = fermat_test(n)
    return n


def encrypt_exponent(phi_n):
    while True:
        e = randint(2, phi_n - 1)
        if euclidean_algorithm(e, phi_n) == 1:
            return e


def decrypt_exponent(e, phi_n):
    d = extended_euclidean_algorithm(e, phi_n)
    if d > 0:
        return d
    else:
        return d + phi_n


def euclidean_algorithm(a, b):
    if a < b:
        temp = a
        a = b
        b = temp
    while True:
        int(a / b)
        remainder = a % b
        a = b
        b = remainder
        if remainder <= 0:
            return a


def extended_euclidean_algorithm(number, module):
    processes = []
    d = 0
    while True:
        processes.append([])
        processes[len(processes) - 1].append(module)
        processes[len(processes) - 1].append(number)
        quotient = int(module / number)
        processes[len(processes) - 1].append(quotient)
        remainder = module % number
        processes[len(processes) - 1].append(remainder)
        module = number
        number = remainder
        if remainder <= 0:
            break
    basis_a = processes[len(processes)-2][0]
    factor_a = 1
    basis_b = processes[len(processes)-2][1]
    factor_b = processes[len(processes)-2][2]
    i = 3
    while len(processes) - i >= -1:
        basis_b = basis_a
        factor_a = -factor_b
        basis_a = processes[len(processes) - i][0]
        factor_b = int((basis_a * factor_a - 1)/basis_b)
        i = i + 1
    return factor_a


