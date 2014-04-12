BASE_ALPH = tuple("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
BASE_DICT = dict((c, v) for v, c in enumerate(BASE_ALPH))
BASE_LEN = len(BASE_ALPH)

def base62_decode(string):
    tnum = 0
    for char in string:
        tnum = tnum * BASE_LEN + BASE_DICT[char]
    return tnum


def base62_encode(num):
    if not num:
        return BASE_ALPH[0]
    num = int(num)
    encoding = ""
    while num:
        num, rem = divmod(num, BASE_LEN)
        encoding = BASE_ALPH[rem] + encoding
    return encoding