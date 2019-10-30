
import re


class Stack:
    def __init__(self):
        self.q = []

    def insert(self, i):
        self.q.append(i)

    def peak(self):
        return self.q[-1]

    def pop(self):
        last = self.peak()
        self.q.pop()
        return last

    def length(self):
        return len(self.q)


def is_balanced(s):
    stack = Stack()
    if re.match(r'[\[{(\]})]', s):
        ref = {']': '[', '}': '{', ')': '('}
        for i, c in enumerate(s):
            if re.match(r'[\[{(]', c):
                # left braces match
                stack.insert(c)
                pass
            elif re.match(r'[\]})]', c):
                #
                if (stack.length() > 0 and ref[c] == stack.peak()):
                    stack.pop()
                else:
                    return False
    return stack.length() == 0


if __name__ == "__main__":
    # print(is_balanced('((5+3)*2+1)'))
    print(is_balanced('[1+1]+(2*2)-{3/3}'))
    print(is_balanced('(({[(((1)-2)+3)-3]/3}-3)'))
    print(is_balanced('(3+{1-1)}'))
    print(is_balanced('2+3'))
    print(is_balanced('(((1+(1+1))))]'))
    print(is_balanced(']'))
