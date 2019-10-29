# N = a+ a+1 +  a+2 + a+3 + .... + a+l
def consec_sum_cnt(N):
    l = 0
    cnt = 0
    while(l*(l+1)/2 < N):
        a = (N/(l+1)) - (l/2)
        if a - int(a) == 0:
            print(a)
            cnt += 1
        l += 1
    return cnt


if __name__ == "__main__":
    print(consec_sum_cnt(42))
