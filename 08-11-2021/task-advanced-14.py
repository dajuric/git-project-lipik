def check_oib(oib):
    OIB_LEN = 11

    rem = 0
    for digit in oib[:-1]:
        rem += int(digit)
        rem %= 10
        if rem == 0:
            rem = 10
        rem *= 2
        rem %= 11

    ctrlDigit = OIB_LEN - rem
    if ctrlDigit == 10:
        ctrlDigit = 0

    return ctrlDigit == int(oib[-1])


oib = input('Unesi OIB: ')
print(check_oib(oib))