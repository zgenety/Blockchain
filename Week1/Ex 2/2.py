def rsa_fun(p, q, en_text) -> list:
    txt = ' '.join(format(ord(x), 'b') for x in en_text)
    txt = int(txt.replace(" ", ""), 2)
    n = p * q

    e = 2
    for i in range(2, 10000):
        e = i
        if nod(e, p - 1) == 1 and nod(e, q - 1) == 1:
            break

    d = pow(e, -1, (p - 1) * (q - 1))

    t = (txt ** e) % n
    r = (t ** d) % n
    return [n, e, d, t, r]


def nod(a, b) -> int:
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b


text = "a"
ar = rsa_fun(53, 59, text)

print("n = {}, e = {}, d = {}".format(ar[0], ar[1], ar[2]))
print("text = {}".format(text))
text = ''.join(format(ord(x), 'b') for x in text)
print("text bin= {}\nen_text = {}\nde_text = {}".format(text, str(bin(ar[3]))[2::], str(bin(ar[4]))[2::]))
