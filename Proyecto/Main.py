from logging import PlaceHolder

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
    print("d = ", d, "\n")
    print("Finalmente se crean las claves pública y privada.\n")
    public_key = PublicKey.PublicKey(n, e)
    print("Clave pública: (", public_key.module, " ,", public_key.exponent, ")")
    private_key = PrivateKey.PrivateKey(n, d)
    print("Clave privada: (", private_key.module, " ,", private_key.exponent, ")")
    print("\n-------------------\n")
    print("Ahora se va a transmitir el mensaje. \n")
    string_array = list(input("Escriba la cadena de caracteres que representa el mensaje a transmitir: "))
    c = []
    string_array.reverse()
    for i in range(0, len(string_array)):
        c.append(pow(ord(string_array[i]), public_key.exponent, public_key.module))
    print("Los códigos que se enviarán como mensaje encriptado son los siguientes: \n")
    k = 1
    for i in c:
        print("C_" + str(k), "=", i)
        k = k + 1
    print("\nAhora se procede a desencriptar haciendo uso de la clave privada: \n")
    k = 1
    message = []
    for i in c:
        value = pow(i, private_key.exponent, private_key.module)
        print("M_" + str(k), "=", value)
        message.append(value)
        k = k + 1
    print("\nY finalmente el mensaje recuperado por parte del receptor es:\n")
    message_string = []
    message.reverse()
    for i in message:
        message_string.append(chr(i))
    print("M =", "".join(message_string))
