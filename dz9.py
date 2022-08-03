from random import choice

ss = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!@#$%^&*()_-=+\/.,><?;:{}[]'


def generate_password(m):
    a = ''.join(choice(ss) for i in range(m))
    return a


def main(n, m):
    k = []
    h = ''
    for i in range(n):
        if i != 0:
            while h in k:
                h = generate_password(m)
            k.append(h)
        else:
            h = generate_password(m)
            k.append(h)
    return k
main()