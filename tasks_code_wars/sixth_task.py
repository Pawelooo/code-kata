# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
def duplicate_encode(word):
    new = ''
    used = []
    for w in word:
        if w in used:
            new += ')'
        else:
            num = 0
            for n in word:
                if w.lower() == n.lower():
                    num += 1
            new += '(' if num == 1 else ')'
            used.append(w.lower())

    return new


