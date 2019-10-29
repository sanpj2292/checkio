
def are_all_same(arr):
    if len(arr) == 0:
        return True
    else:
        arr_set = set(arr)
        if len(arr_set) <= 1:
            return True
        else:
            return False


def secured_password(pwd):
    import re
    if len(pwd) >= 10:
        l_char = re.search(r'[a-z]+', pwd)
        u_char = re.search(r'[A-Z]+', pwd)
        nums = re.search(r'[0-9]+', pwd)
        if (l_char is not None and u_char is not None and nums is not None):
            return True
        else:
            return False
    else:
        return False


def most_wanted_letter(words):
    import re
    ltr_frq = {}
    frq_ltr = {}
    filtered_words = re.findall(r'[a-zA-Z]]+', words)
    text = ''.join(filtered_words)
    for i in text:
        ch = i.lower()
        if ltr_frq.get(ch) is not None:
            ltr_frq[ch] += 1
        else:
            ltr_frq[ch] = 1

        if frq_ltr.get(ltr_frq[ch]) is not None:
            frq_ltr[ltr_frq[ch]].append(ch)
        else:
            frq_ltr[ltr_frq[ch]] = [ch]
    
    # Converting the keyset into list to enable sorting
    frq_list = list(frq_ltr.keys())
    # Sorting the letter frequency list
    frq_list.sort()
    # Greatest count list
    grt_cnt_list = frq_ltr[frq_list[-1]]
    if len(grt_cnt_list) > 1:
        cloned = list(grt_cnt_list)
        grt_cnt_list = sorted(cloned)
    return grt_cnt_list[0]    


def insert_into_dict(dct, el):
    if dct.get(el) is not None:
            dct[el] += 1
        else:
            dct[el] = 1