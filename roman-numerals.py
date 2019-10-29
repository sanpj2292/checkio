def initialize():
    rom_dict = {}
    rom_dict[1] = 'I'
    rom_dict[5] = 'V'
    rom_dict[10] = 'X'
    rom_dict[50] = 'L'
    rom_dict[100] = 'C'
    rom_dict[500] = 'D'
    rom_dict[1000] = 'M'
    # print(form_roman_numerals(1, 5, 1, rom_dict))
    # form_roman_numerals(5, 10, 1, rom_dict)
    diff = 10
    st = 10
    en = 100
    a = list(range(st+diff, st+4*diff, diff))
    print(f'alist1: {a}')
    a.extend(range((5*diff)+10, en, diff))
    print(f'alist2: {a}')

    # print(rom_dict)


def form_roman_numerals(st, en, diff, roman_dict):
    range(st+diff, st + 4*diff + 1, diff)
    for i in range(st+1, en, diff):
        if (i-st) <= 2*diff:
            print(f'<2*diff: {i}')
            print(roman_dict[st])
            roman_dict[i] = roman_dict[st] * ((i)//diff)
        elif i-st == 3*diff:
            print(f'==3*diff: {i}')
            roman_dict[i] = roman_dict[st] + roman_dict[en]
    return roman_dict


def split_nums(n):
    n_str = str(n)
    l = len(n_str)
    d = 10 ** (l-1)
    print(d)
    s = 0
    i = -1
    sums = []
    num_str = n_str[:]
    while(s < n):
        s += int(num_str[0])*d
        print(f's = {s}')
        sums.append(int(num_str[0])*d)
        i += 1
        if len(num_str) > 1:
            num_str = num_str[1:]
        else:
            num_str = num_str[0]

        print(f'NumList: {num_str}')
        d = int(10 ** (len(num_str) - 1))
        print(f'd: {d}')

    return sums


if __name__ == "__main__":
    print(initialize())
    # print(split_nums(1252))
    # print(split_nums(100))
    # print(split_nums(1))
