_MAX_ASCII = 175
_MIN_ASCII = 33
_LAST_ASCII = _MAX_ASCII - _MIN_ASCII

def decode_SnDn(dataS, dataSn, dataD, dataDn):
    whole = get_double_value(dataS, dataSn)
    decimal = get_double_value(dataD, dataDn)
    return get_float(whole, decimal)

def decode_SD(dataS, dataD):
    whole = get_value(dataS)
    decimal = get_value(dataD)
    return get_float(whole, decimal)

def get_value(data):
    return int(ord(data) - _MIN_ASCII)

def get_double_value(dataSD, dataN):
    return int((get_value(dataSD) * _LAST_ASCII) + get_value(dataN))

def get_float(whole, decimal):
    value = str(whole) + "." + str(decimal)
    return float(value)

def str_decode(data):
    SnDn = []
    size = len(data)
    for a in range(size):
        SnDn.append(data[a:a+1])
    if size == 2:
       return decode_SD(SnDn[0],SnDn[1])
    elif size == 4:
        return decode_SnDn(SnDn[0], SnDn[1], SnDn[2], SnDn[3])
    else:
        print("Error")