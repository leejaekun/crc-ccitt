from pythonCRC import crc

crccalc = crc()
crccalc.setCRC8()  # Let's calculate the CRC8 of a value
crccalc.data = "05 27 10 64"
crccalc.compute()
print(crccalc.result)
