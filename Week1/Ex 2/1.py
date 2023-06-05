def rsa_fun(p, q, en_text) -> list:
    n = p * q

    e = 2
    for i in range(2, 10000):
        e = i
        if nod(e, p - 1) == 1 and nod(e, q - 1) == 1:
            break

    d = pow(e, -1, (p - 1) * (q - 1))

    t = (en_text ** e) % n
    r = (t ** d) % n
    return [n, e, d]


def nod(a, b) -> int:
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b


print(rsa_fun(53, 59, 13))
