import RSAProcesses
import PrivateKey
import PublicKey

if __name__ == '__main__':
    print("-------------------")
    print("---Algoritmo RSA---")
    print("-------------------\n")
    magnitude_order = int(input("Ingrese el orden de magnitud de los números primos a utilizar: "))
    print("Se va a generar los dos números primos p y q.\n")
    p = RSAProcesses.random_prime(magnitude_order)
    while True:
        q = RSAProcesses.random_prime(magnitude_order)
        if p != q:
            break
    print("Los primos generados fueron:\n")
    print("p = ", p)
    print("q = ", q, "\n")
    n = p * q
    print("Por lo tanto el módulo será:\n")
    print("n = ", n, "\n")
    print("Ahora, se calcula el valor de la función phi(n):\n")
    phi_n = (p-1)*(q-1)
    print("Phi(n) = ", phi_n, "\n")
    print("Se escoje un exponente de cifrado:\n")
    e = RSAProcesses.encrypt_exponent(phi_n)
    print("e = ", e, "\n")
    print("A continuación se calcula el exponente de descifrado:\n")
    d = RSAProcesses.decrypt_exponent(e, phi_n)
    print("d = ", d, "\n\n")


