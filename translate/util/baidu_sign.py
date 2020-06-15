import math

__all__ = ['generate_token']


def encode_by_key(num, key):
    t = 0
    while t < len(key) - 2:
        a = key[t + 2]
        if ord(a) >= ord('a'):
            a = ord(a) - 87
        else:
            a = int(a)

        if key[t + 1] == '+':
            a = num >> a
        else:
            a = num << a

        if '+' == key[t]:
            num = num + a & 4294967295
        else:
            num = num ^ a

        t += 3
    return num


def substr(string, start, length):
    end = start + length
    if start < 0:
        end = length
    return string[start:end]


def generate_token(text, gtk):
    if len(text) > 30:
        text = substr(text, 0, 10) + substr(text, math.floor(len(text) / 2) - 5, 10) + substr(text, -10, len(text))

    gtk_list = gtk.split('.')
    prefix = int(gtk_list[0])
    suffix = int(gtk_list[1])
    s = []
    v = 0

    while v < len(text):
        a = ord(text[v])

        if 128 > a:
            s.append(a)
        else:
            if 2048 > a:
                s.append(a >> 6 | 192)
            else:
                if 55296 == (64512 & a) and v + 1 < text.length and 56320 == (64512 & ord(text[v + 1])):
                    a = 65536 + ((1024 & a) << 10) + (1023 & ord(text[++v]))
                    s.append(a >> 18 | 240)
                    s.append(a >> 12 & 63 | 128)
                else:
                    s.append(a >> 12 | 224)

                s.append(a >> 6 & 63 | 128)

            s.append(63 & a | 128)
        v += 1

    key1 = '+-a^+6'
    key2 = "+-3^+b+-f"
    p = prefix

    b = 0
    while b < len(s):
        p += s[b]
        p = encode_by_key(p, key1)
        b += 1

    p = encode_by_key(p, key2)
    p ^= suffix

    if p < 0:
        p = (2147483647 & p) + 2147483648

    p %= 1e6
    p = int(p)

    return str(p) + '.' + str(p ^ prefix)
