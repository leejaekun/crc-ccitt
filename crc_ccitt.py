# https://stackoverflow.com/questions/25239423/crc-ccitt-16-bit-python-manual-calculation
#
# CRC-CCITT (Xmodem) 방법  
#
from functools import reduce    # only for python3
POLYNOMIAL = 0x1021
PRESET = 0

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

_tab = [ _initial(i) for i in range(256) ]

def _update_crc(crc, c):
    cc = 0xff & c

    tmp = (crc >> 8) ^ cc
    crc = (crc << 8) ^ _tab[tmp & 0xff]
    crc = crc & 0xffff
    # print (crc)  # 변경되는 값을 연속으로 업데이트 하며 보여줌.
    # 맨 마지막 값이 진짜 값이므로... 필요한 것은 마지막 한개만 필요함.

    return crc

def crc(str):
    crc = PRESET
    for c in str:
        crc = _update_crc(crc, ord(c))
    return crc

def crcb(*i):
    crc = PRESET
    # 여기서 i 는 tuple 
    for c in i:
        crc = _update_crc(crc, c)
    return crc


def crcbLst(i):
    crc = PRESET
    # 여기서 i는 list
    for c in i:
        crc = _update_crc(crc, c)
    return crc

#
# 토론 글에 올려진 내용인데... 잘 모르겠음.
#
def crc16_ccitt(crc, data):
    msb = crc >> 8
    lsb = crc & 255
    for c in data:
        x = ord(c) ^ msb  # 원래 코드 
        x ^= (x >> 4)
        msb = (lsb ^ (x >> 3) ^ (x << 4)) & 255
        lsb = (x ^ (x << 5)) & 255
    return (msb << 8) + lsb


#######################################################################################
# 입력 / 출력 확인 https://www.lammertbies.nl/comm/info/crc-calculation
#######################################################################################
# 가변 개수의 인수 정의 방법  # https://hcnoh.github.io/2019-01-27-python-arguments-asterisk
tp = crcb(0x05,  0x27, 0x10, 0x64) # 입력받은 데이타 16진수값임 03 03 + 05 27 10 64 + 90 42
print('CRC-CCIT(Xmodem) tuple : {}'.format(hex(tp)))

# 리스트 형식으로 넘겨주는 방법 
data = [0x05,  0x27, 0x10, 0x64]
value = crcbLst(data)
#######################################################################################
#  HEX LIST 출력 
# https://stackoverflow.com/questions/18783962/printing-a-python-list-with-hex-elements
print('Input List : [{}]'.format(', '.join(hex(x) for x in data)))  
#######################################################################################

print('CRC-CCIT(Xmodem) list  : {}'.format(hex(value)))

#######################################################################################
# 정답은 CRC-CCIT(Xmodem) : 0x9042
#######################################################################################

#######################################################################################
# 리스트인 문자로 입력된 HEX값에서 INT값을 출력하는 방법 
# https://stackoverflow.com/questions/51261055/python-convert-tuple-hex-strings-into-integer/51261214
#######################################################################################
myList = ['0x05',  '0x27', '0x10', '0x64']
print(myList[0] + ' --> ' + str(reduce(lambda x, y: (x<<8) + int(y,16), [0]+myList[0:1:1])))
print(myList[1]+ myList[2] + ' --> ' + str(reduce(lambda x, y: (x<<8) + int(y,16), [0]+myList[1:3:1])))
print(myList[3] + ' --> ' + str(reduce(lambda x, y: (x<<8) + int(y,16), [0]+myList[3:4:1])))

