_MAX_ASCII = 175
_MIN_ASCII = 33
_LAST_ASCII = _MAX_ASCII - _MIN_ASCII

__ERROR_RANGE = 0.00000000001

def codeDN(data):
    whole, decimal = code(data)
    return get_doble_ascii(whole,decimal)

def codeSnDn(data):
    whole, decimal = code(data)

    dataW = int(whole / _LAST_ASCII)
    whole = whole - (_LAST_ASCII * dataW)
    dataD = int(decimal / _LAST_ASCII)
    decimal = decimal - (_LAST_ASCII * dataD)

    return (get_doble_ascii(dataW,whole) + 
    get_doble_ascii(dataD,decimal))

def code(data):
    whole = int(data)
    decimal = convert_decimal(data, whole)
    return whole, decimal

def convert_decimal(double, whole):
    size = len(str(double)) - (len(str(whole))+1)
    double = double - whole + __ERROR_RANGE
    for a in range(0, 10 * size, 10):
        double = double * 10
    return int(double)

def get_doble_ascii(DataW, DataD):
    return get_ascii(DataW)+get_ascii(DataD)

def get_ascii(val):
    return chr(int(val)+_MIN_ASCII)