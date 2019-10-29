def initialize():
    rom_dict = {}
    rom_dict[1] = 'I'
    rom_dict[5] = 'V'
    rom_dict[10] = 'X'
    rom_dict[50] = 'L'
    rom_dict[100] = 'C'
    rom_dict[500] = 'D'
    rom_dict[1000] = 'M'
    diff = 1
    st = 1
    en = 10
    i = 0
    while i < 4:
        en_1 = st + 4*diff
        is_true = en < en_1
        if is_true:
            en_1 = en
        # Range Formation
        a = list(range(st+diff, en_1, diff))
        a.extend(range((5*diff)+diff, en, diff))
        # Dictionary of Important Roman Numerals
        roman = form_roman_numerals(a, diff, rom_dict)
        st *= 10
        en = 10*en if i < 2 else 3999
        diff *= 10
        i += 1
    return roman


def form_roman_numerals(rng, diff, r_dict):
    st = rng[0] - diff
    en = rng[-1] + diff
    mid = 5*diff
    for i, n in enumerate(rng):
        if i < 2:
            r_dict[n] = r_dict[st] * (n // diff)
        elif i == 2:
            r_dict[n] = f'{r_dict[st]}{r_dict[mid]}'
        elif i > 2 and i < 6:
            r_dict[n] = f'{r_dict[5*diff]}{r_dict[st] * ((n-mid)//diff)}'
        else:
            r_dict[n] = f'{r_dict[st]}{r_dict[en]}'
    return r_dict


def split_nums(n):
    # Splits numbers according to their units
    n_str = str(n)
    l = len(n_str)
    d = 10 ** (l-1)
    s = 0
    i = -1
    sums = []
    num_str = n_str[:]
    while(s < n):
        if int(num_str[0]) != 0:
            s += int(num_str[0])*d
            sums.append(int(num_str[0])*d)
        i += 1
        if len(num_str) > 1:
            num_str = num_str[1:]
        else:
            num_str = num_str[0]
        d = int(10 ** (len(num_str) - 1))
    return sums


def get_roman_numeral(num, r_d):
    num_list = split_nums(num)
    rom_list = [r_d[n] for n in num_list]
    return ''.join(rom_list)


if __name__ == "__main__":
    roman_dict = initialize()
    # print(get_roman_numeral(1234, roman_dict))
    print(get_roman_numeral(14, roman_dict))
    print(get_roman_numeral(602, roman_dict))
    # print(get_roman_numeral(602, roman_dict))
    print(split_nums(602))
