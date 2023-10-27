def length(number, length) -> bool:
    flag = True
    if len(number) != length:
        flag = False
    return flag

def just_str(x) -> bool:
    flag = True
    if str(x).isalpha() == False:
        flag = False
    return flag

def just_number(id) -> bool:
    flag = True
    if str(id).isdigit() == False:
        flag = False
    return flag

def str_int(x) -> bool:
    flag = True
    if str(x).isalnum() == False:
        flag = False
    return flag
