PRESET = 0
POLYNOMIAL = 0x1021

def _initial(c):
    crc = 0
    c = c << 8
    for j in range(8):
        if (crc ^ c) & 0x8000:
            crc = (crc << 1) ^ POLYNOMIAL
        else:
            crc = crc << 1
        c = c << 1
    return crc

_tab = [_initial(i) for i in range(256)]

def _update_crc(crc, c):
    cc = 0xff & c

    tmp = (crc >> 8) ^ cc
    crc = (crc << 8) ^ _tab[tmp & 0xff]
    crc = crc & 0xffff
    print (crc)

    return crc

def crc(str):
    crc = PRESET
    # start crc with two zero bytes
    for _ in range(2):
        crc = _update_crc(crc, 0)
    for c in str:
        crc = _update_crc(crc, ord(c))
    return crc


def crcb(*i):
    crc = PRESET
    for _ in range(2):
        crc = _update_crc(crc, 0)
    for c in i:
        crc = _update_crc(crc, c)
    return crc

crc('123456789')