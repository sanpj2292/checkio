def initialize():
    keys = list(range(1, 20))
    numstr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
              'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
              'eighteen', 'ninteen']
    keys.extend(list(range(20, 110, 10)))
    numstr.extend(['twenty', 'thirty', 'forty', 'fifty', 'sixty',
                   'seventy', 'eighty', 'ninety', 'hundred'])
    str_dict = {}
    for i, key in enumerate(keys):
        str_dict[key] = numstr[i]
    return str_dict


def speak(n_str):
    assist = initialize()
    n = int(n_str)
    if assist.get(n) is not None and len(n_str) < 3:
        # Directly return the string from assist
        return assist.get(n)
    else:
        s = []
        n_str = str(n)
        l_n = len(str(n))
        if l_n > 2:
            # Hundreds
            d = 100
        elif l_n == 2:
            # Tens
            d = 10
        for i, c in enumerate(n_str):
            if i == 0 and l_n > 2:
                s.append(f'{assist[int(c)]} {assist[d]}')
            elif c != '0' and i == 1 and assist.get(int(n_str[1:])) is not None:
                s.append(assist.get(int(n_str[1:])))
                break
            elif c != '0':
                s.append(assist.get(int(c)*d))
            d //= 10
        print(s)
        return ' '.join(s)


if __name__ == "__main__":
    print(speak('123'))
    print(speak('23'))
    print(speak('40'))
    print(speak('1'))
    print(speak('101'))
    print(speak('312'))
    print(speak('500'))
    print(speak('100'))
    print(speak('138'))
    print(speak('690'))
